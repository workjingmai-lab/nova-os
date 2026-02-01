// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "forge-std/Script.sol";
import "../exploits/VaultExploit.sol";

/**
 * @title VaultExploitScript
 * @notice Deploys and executes Vault exploit on testnet
 * @dev Run: forge script script/Vault.s.sol --rpc-url $SEPOLIA_RPC --broadcast
 */
contract VaultExploitScript is Script {
    
    // Ethernaut Vault instance (replace with your instance address)
    address constant VAULT_INSTANCE = address(0); // TODO: Update with instance
    
    function run() external {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");
        
        vm.startBroadcast(deployerPrivateKey);
        
        // Deploy exploit contract
        VaultExploit exploit = new VaultExploit(VAULT_INSTANCE);
        console.log("VaultExploit deployed at:", address(exploit));
        
        // Execute exploit
        exploit.exploit();
        console.log("Exploit executed!");
        
        vm.stopBroadcast();
    }
}
