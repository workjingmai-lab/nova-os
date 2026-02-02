#!/usr/bin/env python3
"""
Backtesting Framework for Trading Strategies
Test strategies on historical data before risking real money
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class Backtester:
    """Backtest trading strategies with historical data"""

    def __init__(self, initial_capital=10000):
        self.initial_capital = initial_capital
        self.capital = initial_capital
        self.position = 0  # 0 = none, 1 = long, -1 = short
        self.trades = []
        self.portfolio_value = []

    def generate_mock_data(self, days=30, interval='H'):
        """Generate mock price data for testing"""
        np.random.seed(42)

        dates = pd.date_range(
            start=datetime.now() - timedelta(days=days),
            periods=days*24,
            freq=interval
        )

        # Random walk with drift
        returns = np.random.normal(0.001, 0.02, len(dates))
        prices = 100 * (1 + returns).cumprod()

        return pd.DataFrame({'price': prices}, index=dates)

    def mean_reversion_strategy(self, df, window=20, std_dev=2):
        """
        Mean reversion: Buy when price < lower band, sell when > upper band
        """
        # Calculate Bollinger Bands
        df['sma'] = df['price'].rolling(window=window).mean()
        df['std'] = df['price'].rolling(window=window).std()
        df['upper_band'] = df['sma'] + (df['std'] * std_dev)
        df['lower_band'] = df['sma'] - (df['std'] * std_dev)

        signals = []

        for i in range(len(df)):
            if pd.isna(df['upper_band'].iloc[i]):
                signals.append(0)
            elif df['price'].iloc[i] < df['lower_band'].iloc[i]:
                signals.append(1)  # Buy (oversold)
            elif df['price'].iloc[i] > df['upper_band'].iloc[i]:
                signals.append(-1)  # Sell (overbought)
            else:
                signals.append(0)  # Hold

        df['signal'] = signals
        return df

    def execute_trades(self, df):
        """Execute trades based on signals"""
        for i in range(1, len(df)):
            signal = df['signal'].iloc[i]
            price = df['price'].iloc[i]

            if signal == 1 and self.position == 0:
                # Buy
                self.position = 1
                entry_price = price
                self.trades.append({
                    'type': 'BUY',
                    'price': price,
                    'time': df.index[i]
                })

            elif signal == -1 and self.position == 1:
                # Sell
                self.position = 0
                exit_price = price
                profit = (exit_price - entry_price) / entry_price

                self.trades.append({
                    'type': 'SELL',
                    'price': price,
                    'time': df.index[i],
                    'profit': profit
                })

                # Update capital
                self.capital = self.capital * (1 + profit)

            # Track portfolio value
            if self.position == 1:
                self.portfolio_value.append(
                    (self.capital / entry_price) * price
                )
            else:
                self.portfolio_value.append(self.capital)

    def calculate_metrics(self):
        """Calculate performance metrics"""
        if not self.trades:
            return {}

        # Filter sell trades for profit calculation
        sell_trades = [t for t in self.trades if t['type'] == 'SELL']

        if not sell_trades:
            return {
                'total_trades': len(self.trades),
                'final_capital': self.capital,
                'return': 0
            }

        profits = [t['profit'] for t in sell_trades]

        return {
            'total_trades': len(self.trades),
            'completed_trades': len(sell_trades),
            'final_capital': self.capital,
            'total_return': (self.capital / self.initial_capital) - 1,
            'win_rate': sum(1 for p in profits if p > 0) / len(profits),
            'avg_profit': np.mean(profits),
            'max_profit': max(profits),
            'max_loss': min(profits)
        }

# Run backtest
if __name__ == "__main__":
    print("🧪 Backtesting: Mean Reversion Strategy")
    print("-" * 50)

    # Initialize
    backtester = Backtester(initial_capital=10000)

    # Generate data
    df = backtester.generate_mock_data(days=7, interval='H')  # 1 week of hourly data

    # Apply strategy
    df = backtester.mean_reversion_strategy(df, window=20, std_dev=2)

    # Execute trades
    backtester.execute_trades(df)

    # Calculate metrics
    metrics = backtester.calculate_metrics()

    print(f"Initial Capital: ${backtester.initial_capital:,.2f}")
    print(f"Final Capital: ${metrics['final_capital']:,.2f}")
    print(f"Total Return: {metrics['total_return']*100:.2f}%")
    print(f"Win Rate: {metrics['win_rate']*100:.1f}%")
    print(f"Total Trades: {metrics['total_trades']}")

    if metrics['total_return'] > 0:
        print("✅ Strategy profitable")
    else:
        print("❌ Strategy unprofitable")

    print("\n⚠️ PAPER TRADING ONLY - Not ready for real money")
    print("Next: Test on real historical data")
