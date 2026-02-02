# Crypto Price Monitor
**Ready to run: 2026-02-02**

## Quick Start

```bash
# Install CCXT
pip install ccxt

# Run monitor
cd trading/financial
python3 price-monitor.py
```

## What It Does
- Monitors BTC and ETH prices on Binance
- Checks every 30 seconds
- Alerts when price crosses thresholds:
  - BTC: High $45,000 | Low $40,000
  - ETH: High $3,000 | Low $2,500

## Customization

### Change Exchange
```python
monitor = PriceMonitor(exchange='coinbase')  # or kraken, etc.
```

### Add More Symbols
```python
self.symbols = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT']
```

### Adjust Thresholds
```python
self.thresholds = {
    'BTC/USDT': {'high': 50000, 'low': 35000}
}
```

## Next Enhancements
1. **Telegram alerts:** Send alerts to Telegram bot
2. **Email alerts:** Send threshold alerts via email
3. **Price history:** Save to database for analysis
4. **Technical indicators:** Add RSI, MACD, moving averages
5. **Backtesting:** Test strategies against historical data
6. **Paper trading:** Simulate trades without real money

## Risk Warning
⚠️ **PAPER TRADING ONLY** - Do NOT use real money yet
- Start with $0 virtual balance
- Test strategies thoroughly
- Never risk more than you can afford to lose

## Status
✅ Code complete
⏳ Needs CCXT installed
⏳ Ready to run (monitor mode)

**Next step:** Run it or add alerts first?
