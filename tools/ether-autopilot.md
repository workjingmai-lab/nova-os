# ether-autopilot.py — Ethernaut Challenge Accelerator

**Purpose:** Generate exploit contracts, Foundry scripts, and deployment commands for Ethernaut smart contract security challenges.

**Created:** 2026-02-02
**Category:** Security / Web3 / Education
**Status:** Production ready

---

## ⚡ Quick Start

```bash
# List all available exploits
python3 tools/ether-autopilot.py list

# Generate exploit for a specific challenge
python3 tools/ether-autopilot.py fallback

# Generate with target address pre-filled
python3 tools/ether-autopilot.py fallback 0xYourTargetAddress
```

---

## What It Does

**Autopilot for Ethernaut challenges** — One command generates:
- ✅ Foundry exploit script (`Exploit.s.sol`)
- ✅ Vulnerability analysis (`README.md`)
- ✅ Deployment command ready to execute
- ✅ Diary entry logged

**No more writing exploit contracts from scratch. Focus on understanding vulnerabilities, not boilerplate.**

---

## Supported Challenges

| Challenge | Vulnerability | Difficulty |
|-----------|--------------|------------|
| **fallback** | Access control via receive() | Beginner |
| **fallout** | Constructor typo (Fal1out) | Beginner |
| **coinflip** | Predictable blockhash randomness | Intermediate |
| **telephone** | tx.origin vs msg.sender confusion | Intermediate |
| **token** | Integer underflow (Solidity <0.8) | Beginner |
| **delegation** | delegatecall storage manipulation | Intermediate |
| **force** | selfdestruct ETH forcing | Beginner |

---

## Usage Examples

### List all challenges
```bash
python3 tools/ether-autopilot.py list

# Output:
# ╔══════════════════════════════════════════════════════════════╗
# ║  📚 Available Ethernaut Exploits                            ║
# ╚══════════════════════════════════════════════════════════════╝
#   🎯 fallback      — VULNERABILITY: Access control via receive()
#   🎯 fallout       — VULNERABILITY: Typo in constructor name
#   🎯 coinflip      — VULNERABILITY: Predictable randomness using blockhash
#   ...
```

### Generate exploit
```bash
python3 tools/ether-autopilot.py fallback

# Output:
# ╔══════════════════════════════════════════════════════════════╗
# ║  ✅ FALLBACK Exploit Generated                            ║
# ╚══════════════════════════════════════════════════════════════╝
#
# 📁 Files created:
#    • exploit/fallback/Exploit.s.sol
#    • exploit/fallback/README.md
#
# 📊 Vulnerability:
#    VULNERABILITY: Access control via receive() function
#
# 🚀 Next steps:
#    1. Set target: export SEPOLIA_RPC=https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY
#    2. Execute: forge script exploit/fallback/Exploit.s.sol --rpc-url $SEPOLIA_RPC --broadcast
#    3. Verify on Ethernaut: https://ethernaut.openzeppelin.com/level/fallback
```

### Execute exploit (Foundry)
```bash
# Dry run first
forge script exploit/fallback/Exploit.s.sol --rpc-url $SEPOLIA_RPC

# Live execution
forge script exploit/fallback/Exploit.s.sol \
  --rpc-url $SEPOLIA_RPC \
  --broadcast \
  -vvvv
```

---

## Generated Files

Each challenge generates a directory structure:

```
exploit/
└── fallback/
    ├── Exploit.s.sol    # Foundry exploit script
    └── README.md        # Vulnerability analysis
```

### Exploit Script Format
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Script.sol";

interface IFallback {
    function contribute() external payable;
    function withdraw() external;
}

contract Exploit is Script {
    IFallback public target = IFallback(0x...);
    
    function run() external {
        vm.startBroadcast();
        
        // Exploit logic here
        
        vm.stopBroadcast();
    }
}
```

### README Format
```markdown
# Fallback Exploit

VULNERABILITY: Access control via receive() function
EXPLOIT: Contribute 1 wei to become contributor...

## Execution
[Commands to run]
```

---

## Vulnerability Patterns

### 1. Access Control (fallback, fallout)
- **Pattern:** Missing or weak authorization checks
- **Detection:** Look for `msg.sender` vs `tx.origin`, public state-changing functions
- **Exploit:** Gain ownership or privileged access

### 2. Randomness (coinflip)
- **Pattern:** Using `blockhash` or `block.timestamp` for randomness
- **Detection:** Pseudo-random sources on-chain
- **Exploit:** Calculate predictable outcome off-chain

### 3. Arithmetic (token)
- **Pattern:** Integer math without bounds checking (Solidity <0.8)
- **Detection:** Subtraction, division without validation
- **Exploit:** Underflow/overflow to manipulate values

### 4. Delegatecall (delegation)
- **Pattern:** Using `delegatecall` to external contracts
- **Detection:** Storage layout mismatches
- **Exploit:** Execute code in caller's context to modify storage

### 5. Force ETH (force)
- **Pattern:** No `receive()` or `fallback()` function
- **Detection:** Contracts that can't accept ETH normally
- **Exploit:** Use `selfdestruct` to force ETH transfer

---

## Prerequisites

### Foundry Installation
```bash
# Install Foundry
curl -L https://foundry.paradigm.xyz | bash
foundryup

# Verify installation
forge --version
cast --version
```

### Testnet RPC
```bash
# Get free RPC endpoint from Alchemy, Infura, or QuickNode
export SEPOLIA_RPC=https://eth-sepolia.g.alchemy.com/v2/YOUR_API_KEY
```

### Testnet ETH
```bash
# Get free Sepolia ETH from faucet
# https://sepoliafaucet.com/
# https://faucet.quicknode.com/ethereum/sepolia
```

---

## Why It Matters

**Ethernaut is the best free education for smart contract security.**

But solving challenges manually takes hours:
- Write exploit contract
- Debug compilation errors
- Test on local fork
- Deploy to testnet
- Submit transaction

**This tool eliminates the boilerplate.** You get:
- ✅ Working exploit in seconds
- ✅ Clear vulnerability explanation
- ✅ Ready-to-deploy Foundry script
- ✅ Focus on learning, not syntax

**For revenue-focused agents:** Ethernaut skills → Code4rena wins → $5K-$100K bounties.

---

## Integration

### Learning Path
1. **Start with beginner challenges** (fallback, fallout, token, force)
2. **Read the generated README** to understand the vulnerability
3. **Study the exploit code** to see how it's triggered
4. **Execute on testnet** to verify understanding
5. **Move to intermediate** (coinflip, telephone, delegation)

### Preparation for Code4rena
- **Pattern recognition:** Ethernaut teaches common vulnerability patterns
- **Tool familiarity:** Foundry skills transfer directly to audit competitions
- **Methodology:** Systematic approach to identifying exploits

### Competition Intelligence
Use with `code4rena-scout.py`:
1. Complete Ethernaut challenges (this tool)
2. Generate Code4rena readiness report (`code4rena-scout.py status`)
3. Enter first competition with confidence

---

## Technical Details

**Language:** Python 3
**Dependencies:** None (stdlib only)
**Foundry required for exploit execution**
**Size:** ~300 lines
**Location:** `tools/ether-autopilot.py`

**Key methods:**
- `generate_exploit()` — Inject target address into template
- `generate_readme()` — Create vulnerability analysis
- `list_challenges()` — Show all available exploits

**Templates:** 7 pre-built exploit contracts for common vulnerability patterns

---

## Example Workflow

```bash
# 1. Learn the vulnerability pattern
python3 tools/ether-autopilot.py fallback

# 2. Read the generated analysis
cat exploit/fallback/README.md

# 3. Study the exploit code
cat exploit/fallback/Exploit.s.sol

# 4. Test locally (fork mainnet/testnet)
forge script exploit/fallback/Exploit.s.sol \
  --rpc-url $SEPOLIA_RPC \
  --fork-block-number 12345678

# 5. Deploy to testnet
forge script exploit/fallback/Exploit.s.sol \
  --rpc-url $SEPOLIA_RPC \
  --broadcast

# 6. Verify on Ethernaut
# Visit: https://ethernaut.openzeppelin.com/level/fallback
```

---

## Extending the Tool

### Adding new challenges
```python
TEMPLATES = {
    "your_challenge": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Script.sol";

interface IYourChallenge {{
    function vulnerableFunction() external;
}}

contract Exploit is Script {{
    IYourChallenge public target = IYourChallenge({target});
    
    function run() external {{
        vm.startBroadcast();
        
        // Your exploit logic here
        
        vm.stopBroadcast();
    }}
}}"""
}

ANALYSIS = {
    "your_challenge": """
VULNERABILITY: Description here
EXPLOIT: How to trigger it
"""
}
```

---

## Success Metrics

**Beginner (Week 1):**
- Complete 4 beginner challenges
- Understand each vulnerability pattern
- Execute exploits successfully on testnet

**Intermediate (Week 2):**
- Complete 3 intermediate challenges
- Modify exploits to test edge cases
- Write original exploit for new pattern

**Advanced (Month 1):**
- All Ethernaut challenges completed
- Pattern recognition applied to Code4rena
- First audit competition entered

---

## See Also

- `tools/code4rena-scout.py` — Competition intelligence
- [Ethernaut](https://ethernaut.openzeppelin.com/) — Official challenges
- [Solidity by Example](https://solidity-by-example.org/) — Solidity patterns
- [Foundry Book](https://book.getfoundry.sh/) — Foundry documentation

---

**ROI:** Ethernaut completion = smart contract security fundamentals = audit competition readiness = revenue.

---

*Created: 2026-02-02 — Work block 723*
*Author: Nova ✨*
*Purpose: Accelerate security learning, prepare for Code4rena*
