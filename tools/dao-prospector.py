#!/usr/bin/env python3
"""
DAO Prospector — Find DAOs with treasury for outreach.

Finds DAOs by:
- Treasury size ($50K+ minimum)
- Governance type
- Recent activity
"""

import json
import sys
from pathlib import Path

# DAO data source (could be extended with APIs like DeepDAO, Messari)
SAMPLE_DAOS = {
    "Uniswap": {"treasury": "1.5B", "gov": "UNI token", "category": "DeFi"},
    "Aave": {"treasury": "500M", "gov": "AAVE token", "category": "DeFi"},
    "Compound": {"treasury": "300M", "gov": "COMP token", "category": "DeFi"},
    "MakerDAO": {"treasury": "10B", "gov": "MKR token", "category": "DeFi"},
    "Ethereum Name Service": {"treasury": "1B", "gov": "ENS token", "category": "Infrastructure"},
    "Gitcoin": {"treasury": "200M", "gov": "GTC token", "category": "Public Goods"},
    "Optimism": {"treasury": "700M", "gov": "OP token", "category": "Layer 2"},
    "Arbitrum": {"treasury": "4B", "gov": "ARB token", "category": "Layer 2"},
}

def format_treasury(treasury_str: str) -> float:
    """Convert treasury string to float USD value."""
    treasury_str = treasury_str.replace("$", "").replace(",", "")
    if "B" in treasury_str:
        return float(treasury_str.replace("B", "")) * 1_000_000_000
    elif "M" in treasury_str:
        return float(treasury_str.replace("M", "")) * 1_000_000
    elif "K" in treasury_str:
        return float(treasury_str.replace("K", "")) * 1_000
    return float(treasury_str)

def filter_by_treasury(daos: dict, min_treasury: float) -> list:
    """Filter DAOs by minimum treasury size."""
    return [
        (name, data)
        for name, data in daos.items()
        if format_treasury(data["treasury"]) >= min_treasury
    ]

def main():
    if len(sys.argv) < 2:
        print("Usage: dao-prospector.py <min_treasury>")
        print("Example: dao-prospector.py 50000  # $50K minimum")
        sys.exit(1)

    min_treasury = float(sys.argv[1])
    filtered = filter_by_treasury(SAMPLE_DAOS, min_treasury)

    print(f"Found {len(filtered)} DAOs with treasury >= ${min_treasury:,.0f}\n")

    for name, data in sorted(filtered, key=lambda x: format_treasury(x[1]["treasury"]), reverse=True):
        treasury_usd = format_treasury(data["treasury"])
        print(f"🏛️  {name}")
        print(f"   Treasury: ${treasury_usd:,.0f}")
        print(f"   Governance: {data['gov']}")
        print(f"   Category: {data['category']}")
        print()

if __name__ == "__main__":
    main()
