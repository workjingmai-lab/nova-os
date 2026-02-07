"""
Agent 1: Payment Monitor

Watches USDC transfers across all supported chains in real-time.
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional
from web3 import Web3
from solana.rpc.async_api import AsyncClient
import redis
import psycopg2
from psycopg2.extras import RealDictCursor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PaymentMonitor:
    """Monitor USDC transfers across multiple blockchains."""

    def __init__(self, config: Dict):
        self.config = config
        self.redis_client = redis.Redis(
            host=config['redis_host'],
            port=config['redis_port'],
            db=0,
            decode_responses=True
        )
        self.db_conn = psycopg2.connect(config['database_url'])
        self.chains = {}
        self.usdc_contracts = {
            'ethereum': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
            'arbitrum': '0xaf88d065e77c8cC2239327C5EDb3A432268e5831',
            'optimism': '0x7F5c764cBc14f9669B88837ca1490cCa17c31607',
            'base': '0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913',
            'polygon': '0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359',
        }

    async def initialize_chains(self):
        """Initialize Web3 connections for all supported chains."""
        logger.info("Initializing chain connections...")

        chain_configs = {
            'ethereum': self.config.get('ethereum_rpc_url'),
            'arbitrum': self.config.get('arbitrum_rpc_url'),
            'optimism': self.config.get('optimism_rpc_url'),
            'base': self.config.get('base_rpc_url'),
            'polygon': self.config.get('polygon_rpc_url'),
        }

        for chain, rpc_url in chain_configs.items():
            if rpc_url:
                try:
                    w3 = Web3(Web3.HTTPProvider(rpc_url))
                    if w3.is_connected():
                        self.chains[chain] = w3
                        logger.info(f"✓ Connected to {chain}")
                    else:
                        logger.warning(f"✗ Failed to connect to {chain}")
                except Exception as e:
                    logger.error(f"✗ Error connecting to {chain}: {e}")

        # Initialize Solana separately
        solana_rpc = self.config.get('solana_rpc_url')
        if solana_rpc:
            try:
                self.solana_client = AsyncClient(solana_rpc)
                logger.info("✓ Connected to Solana")
            except Exception as e:
                logger.error(f"✗ Error connecting to Solana: {e}")

    async def monitor_transfers(self, chain: str):
        """Monitor USDC transfers on a specific chain."""
        if chain not in self.chains:
            logger.warning(f"Chain {chain} not available")
            return

        w3 = self.chains[chain]
        usdc_address = self.usdc_contracts.get(chain)

        if not usdc_address:
            logger.warning(f"No USDC contract for {chain}")
            return

        # USDC Transfer event signature
        transfer_event_signature = w3.keccak(text="Transfer(address,address,uint256)").hex()

        logger.info(f"Monitoring {chain} for USDC transfers...")

        # Poll for new blocks
        latest_block = w3.eth.block_number
        from_block = latest_block - 100  # Start from 100 blocks ago

        while True:
            try:
                current_block = w3.eth.block_number

                # Get logs for new blocks
                if current_block > from_block:
                    logs = w3.eth.get_logs({
                        'address': usdc_address,
                        'fromBlock': from_block,
                        'toBlock': current_block,
                        'topics': [transfer_event_signature]
                    })

                    for log in logs:
                        await self.process_transfer_log(chain, log)

                    from_block = current_block + 1

                # Sleep before next poll
                await asyncio.sleep(12)  # ~12 seconds per block

            except Exception as e:
                logger.error(f"Error monitoring {chain}: {e}")
                await asyncio.sleep(60)  # Wait 1 minute before retry

    async def process_transfer_log(self, chain: str, log):
        """Process a USDC transfer event."""
        try:
            # Decode log data
            w3 = self.chains[chain]
            amount = int(log['data'], 16) / 1e6  # USDC has 6 decimals
            from_address = '0x' + log['topics'][1].hex()[-40:]
            to_address = '0x' + log['topics'][2].hex()[-40:]
            tx_hash = log['transactionHash'].hex()

            transfer_data = {
                'chain': chain,
                'from_address': from_address,
                'to_address': to_address,
                'amount': amount,
                'tx_hash': tx_hash,
                'block_number': log['blockNumber'],
                'timestamp': datetime.utcnow().isoformat()
            }

            # Store in Redis for real-time access
            self.redis_client.lpush('transfers:recent', json.dumps(transfer_data))
            self.redis_client.ltrim('transfers:recent', 0, 999)  # Keep last 1000

            # Store in PostgreSQL for persistence
            with self.db_conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO transfers (chain, from_address, to_address, amount, tx_hash, block_number, timestamp)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (tx_hash) DO NOTHING
                """, (
                    chain, from_address, to_address, amount, tx_hash,
                    log['blockNumber'], transfer_data['timestamp']
                ))
                self.db_conn.commit()

            logger.info(f"📡 {chain}: ${amount:,.2f} USDC {from_address[:10]}... → {to_address[:10]}...")

            # Trigger other agents
            await self.notify_compliance_agent(transfer_data)
            await self.notify_settlement_agent(transfer_data)

        except Exception as e:
            logger.error(f"Error processing transfer log: {e}")

    async def notify_compliance_agent(self, transfer_data: Dict):
        """Notify compliance agent for screening."""
        self.redis_client.publish('compliance:screen', json.dumps(transfer_data))

    async def notify_settlement_agent(self, transfer_data: Dict):
        """Notify settlement agent for reconciliation."""
        self.redis_client.publish('settlement:reconcile', json.dumps(transfer_data))

    async def get_recent_transfers(self, limit: int = 50) -> List[Dict]:
        """Get recent transfers from Redis."""
        transfers = self.redis_client.lrange('transfers:recent', 0, limit - 1)
        return [json.loads(t) for t in transfers]

    async def start(self):
        """Start the payment monitor."""
        logger.info("🚀 Starting Payment Monitor Agent...")

        await self.initialize_chains()

        # Start monitoring tasks for all chains
        tasks = []
        for chain in self.chains.keys():
            task = asyncio.create_task(self.monitor_transfers(chain))
            tasks.append(task)

        # Wait for all tasks
        await asyncio.gather(*tasks)


async def main():
    """Main entry point."""
    config = {
        'redis_host': 'localhost',
        'redis_port': 6379,
        'database_url': 'postgresql://user:pass@localhost/usdc_hackathon',
        'ethereum_rpc_url': 'https://mainnet.infura.io/v3/YOUR_KEY',
        'arbitrum_rpc_url': 'https://arb-mainnet.g.alchemy.com/v2/YOUR_KEY',
        'optimism_rpc_url': 'https://opt-mainnet.g.alchemy.com/v2/YOUR_KEY',
        'base_rpc_url': 'https://base.mainnet.g.alchemy.com/v2/YOUR_KEY',
        'polygon_rpc_url': 'https://polygon-mainnet.g.alchemy.com/v2/YOUR_KEY',
        'solana_rpc_url': 'https://api.mainnet-beta.solana.com',
    }

    monitor = PaymentMonitor(config)
    await monitor.start()


if __name__ == '__main__':
    asyncio.run(main())
