#!/usr/bin/env python3
"""
Crypto Price Monitor + Alert System
Track BTC/ETH prices, alert on thresholds
"""

import ccxt
import time
from datetime import datetime

class PriceMonitor:
    def __init__(self, exchange='binance'):
        self.exchange = getattr(ccxt, exchange)()
        self.symbols = ['BTC/USDT', 'ETH/USDT']
        self.thresholds = {
            'BTC/USDT': {'high': 45000, 'low': 40000},
            'ETH/USDT': {'high': 3000, 'low': 2500}
        }

    def fetch_price(self, symbol):
        """Fetch current price for symbol"""
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            return ticker['last']
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")
            return None

    def check_thresholds(self, symbol, price):
        """Check if price crosses thresholds"""
        if symbol not in self.thresholds:
            return None

        high = self.thresholds[symbol]['high']
        low = self.thresholds[symbol]['low']

        if price >= high:
            return f"🔺 HIGH: {symbol} at ${price:,.2f} (above ${high:,})"
        elif price <= low:
            return f"🔻 LOW: {symbol} at ${price:,.2f} (below ${low:,})"
        return None

    def monitor(self, interval_seconds=60):
        """Monitor prices continuously"""
        print(f"🚀 Price Monitor Started: {datetime.utcnow()}")
        print(f"Tracking: {', '.join(self.symbols)}")
        print(f"Interval: {interval_seconds}s")
        print("-" * 50)

        while True:
            for symbol in self.symbols:
                price = self.fetch_price(symbol)
                if price:
                    alert = self.check_thresholds(symbol, price)
                    timestamp = datetime.utcnow().strftime('%H:%M:%S')

                    if alert:
                        print(f"[{timestamp}] 🚨 ALERT: {alert}")
                    else:
                        print(f"[{timestamp}] {symbol}: ${price:,.2f}")

            time.sleep(interval_seconds)

if __name__ == "__main__":
    monitor = PriceMonitor()
    # TODO: Add Telegram/email alerts
    # TODO: Save price history to database
    # TODO: Add technical indicators (RSI, MACD)
    monitor.monitor(interval_seconds=30)
