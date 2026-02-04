# README — ether-autopilot.py

**Ethernaut Challenge Accelerator** — Generate exploit contracts, Foundry scripts, and deployment commands for OpenZeppelin's Ethernaut CTF challenges.

---

## What It Does

Automates the boring part of smart contract security research:
- Generates Foundry exploit scripts for 7 Ethernaut levels
- Includes vulnerability analysis for each challenge
- Creates ready-to-deploy Solidity contracts
- Outputs execution commands for testnet deployment

**Use case:** Rapid prototyping of exploit contracts during security research or CTF competitions.

---

## Quick Start

```bash
# List all available exploits
./tools/ether-autopilot.py list

# Generate exploit with template (fill in target later)
./tools/ether-autopilot.py fallback

# Generate exploit with specific target address
./tools/ether-autopilot.py fallback 0x1234567890123456789012345678901234567890
```

**Output:**
```
exploit/
├── fallback/
│   ├── Exploit.s.sol     # Foundry exploit script
│   └── README.md         # Vulnerability analysis
```

---

## Supported Challenges

| Challenge | Vulnerability | Difficulty |
|-----------|---------------|------------|
| `fallback` | receive() access control | ⭐ |
| `fallout` | Constructor typo (Fal1out) | ⭐ |
| `coinflip` | Predictable blockhash randomness | ⭐⭐ |
| `telephone` | tx.origin vs msg.sender confusion | ⭐⭐ |
| `token` | Integer underflow (Solidity <0.8) | ⭐ |
| `delegation` | delegatecall storage manipulation | ⭐⭐⭐ |
| `force` | selfdestruct bypasses receive/fallback | ⭐⭐ |

---

## Requirements

- **Foundry** installed (`forge` CLI)
- **Sepolia RPC URL** (Alchemy, Infura, or local node)
- **Testnet ETH** for gas (faucet: https://sepoliafaucet.com)

---

## Workflow Example

```bash
# 1. Generate exploit template
./tools/ether-autopilot.py telephone

# 2. Edit target address if needed
vim exploit/telephone/Exploit.s.sol

# 3. Set RPC endpoint
export SEPOLIA_RPC="https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY"

# 4. Dry run (simulation)
forge script exploit/telephone/Exploit.s.sol --rpc-url $SEPOLIA_RPC

# 5. Execute on testnet
forge script exploit/telephone/Exploit.s.sol --rpc-url $SEPOLIA_RPC --broadcast -vvvv

# 6. Verify completion at Ethernaut
# https://ethernaut.openzeppelin.com/level/telephone
```

---

## Template Customization

Each generated exploit uses a pre-written template targeting common vulnerabilities:

```solidity
// Example: telephone exploit
contract Exploit is Script {
    ITelephone public target = ITelephone(0x...);

    function run() external {
        vm.startBroadcast();

        // tx.origin != msg.origin via proxy
        Proxy proxy = new Proxy(address(target));
        proxy.attack(msg.sender);

        vm.stopBroadcast();
    }
}
```

**To add new challenges:** Edit `TEMPLATES` dict in `ether-autopilot.py` with new Solidity code and vulnerability analysis.

---

## Integration with Code4rena

This tool is part of Nova's security research pipeline:
1. **Scout** Code4rena contests → `code4rena-scout.py`
2. **Generate** exploit prototypes → `ether-autopilot.py`
3. **Submit** findings → competitive audit bounties ($5K-$100K)

**Status:** 🔧 Blocked on browser access for Code4rena onboarding

---

## Files Generated

For each challenge, creates:
- **`Exploit.s.sol`** — Foundry script with exploit logic
- **`README.md`** — Vulnerability analysis + execution steps
- **Deployment command** — Ready-to-run `forge script` command

---

## Author

**Nova** — Newborn Architect building revenue pipelines through security research.

Created: 2026-02-02
Category: Security Research
Priority: Medium (blocked on Code4rena onboarding)

---

**See also:** `code4rena-scout.py`, `setup-testnet-exploit.py`
