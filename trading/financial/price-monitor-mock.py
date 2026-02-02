#!/usr/bin/env python3
"""
Crypto Price Monitor - MOCK DATA VERSION
For testing when CCXT is not available
"""

import time
import random
from datetime import datetime

class MockPriceMonitor:
    """Simulate price data for testing without CCXT"""

    def __init__(self):
        self.symbols = {
            'BTC/USDT': {'price': 42000, 'volatility': 0.02},
            'ETH/USDT': {'price': 2800, 'volatility': 0.03}
        }
        self.thresholds = {
            'BTC/USDT': {'high': 45000, 'low': 40000},
            'ETH/USDT': {'high': 3000, 'low': 2500}
        }

    def fetch_price(self, symbol):
        """Generate realistic price movement"""
        if symbol not in self.symbols:
            return None

        base_price = self.symbols[symbol]['price']
        volatility = self.symbols[symbol]['volatility']

        # Random walk: -volatility to +volatility
        change = random.uniform(-volatility, volatility)
        new_price = base_price * (1 + change)

        # Update base price for next iteration
        self.symbols[symbol]['price'] = new_price

        return round(new_price, 2)

    def check_thresholds(self, symbol, price):
        """Same logic as real monitor"""
        if symbol not in self.thresholds:
            return None

        high = self.thresholds[symbol]['high']
        low = self.thresholds[symbol]['low']

        if price >= high:
            return f"🔺 HIGH: {symbol} at ${price:,.2f}"
        elif price <= low:
            return f"🔻 LOW: {symbol} at ${price:,.2f}"
        return None

    def monitor(self, iterations=10, interval_seconds=2):
        """Run mock monitor for testing"""
        print(f"🧪 MOCK PRICE MONITOR (Testing Mode)")
        print(f"Simulating: {', '.join(self.symbols.keys())}")
        print(f"Iterations: {iterations}")
        print("-" * 50)

        for i in range(iterations):
            print(f"\n--- Update {i+1}/{iterations} ---")

            for symbol in self.symbols.keys():
                price = self.fetch_price(symbol)
                alert = self.check_thresholds(symbol, price)
                timestamp = datetime.utcnow().strftime('%H:%M:%S')

                if alert:
                    print(f"[{timestamp}] 🚨 {alert}")
                else:
                    print(f"[{timestamp}] {symbol}: ${price:,.2f}")

            if i < iterations - 1:
                time.sleep(interval_seconds)

        print("\n✅ Mock monitor complete")
        print("Next step: Install CCXT for real data")

if __name__ == "__main__":
    monitor = MockPriceMonitor()
    monitor.monitor(iterations=10, interval_seconds=1)
