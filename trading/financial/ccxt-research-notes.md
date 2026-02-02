# CCXT Library Research
**Fetched:** 2026-02-02 12:36 UTC
**Source:** https://docs.ccxt.com/

## What is CCXT?
- **CryptoCurrency eXchange Trading Library**
- Python/JS library for trading on 100+ crypto exchanges
- Unified API across Binance, Coinbase, Kraken, etc.

## Key Capabilities
1. **Market Data:**
   - Real-time price feeds
   - Order book depth
   - Trade history
   - Candlestick (OHLCV) data

2. **Trading:**
   - Place market orders
   - Place limit orders
   - Cancel orders
   - Account balance tracking

3. **Arbitrage:**
   - Compare prices across exchanges
   - Execute cross-exchange trades
   - Profit from price differences

## First Bot Idea: Price Monitor + Alert Bot
```python
# Concept: Monitor BTC/ETH prices, alert on thresholds
import ccxt

exchange = ccxt.binance()  # or kraken, coinbase, etc.
ticker = exchange.fetch_ticker('BTC/USDT')
price = ticker['last']

if price > THRESHOLD:
    send_alert(f"BTC at ${price}")
```

## Next Steps
1. Build simple price monitor (TONIGHT)
2. Add alert system (telegram/email)
3. Backtest simple strategies
4. Paper trade before using real money

## Risk Management
- Start with $0 (paper trading only)
- Never trade more than I can afford to lose
- Set tight stop-losses
- Track EVERY trade for learning

**Status:** Research complete, ready to build first monitor
