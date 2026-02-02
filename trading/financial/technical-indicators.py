#!/usr/bin/env python3
"""
Technical Indicators for Trading
RSI, MACD, Moving Averages
"""

import pandas as pd
import numpy as np

class TechnicalIndicators:
    """Calculate technical indicators for price data"""

    @staticmethod
    def sma(prices, period=20):
        """Simple Moving Average"""
        return prices.rolling(window=period).mean()

    @staticmethod
    def ema(prices, period=20):
        """Exponential Moving Average"""
        return prices.ewm(span=period, adjust=False).mean()

    @staticmethod
    def rsi(prices, period=14):
        """
        Relative Strength Index
        >70 = overbought (sell signal)
        <30 = oversold (buy signal)
        """
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    @staticmethod
    def macd(prices, fast=12, slow=26, signal=9):
        """
        Moving Average Convergence Divergence
        MACD line = Fast EMA - Slow EMA
        Signal line = EMA of MACD
        Histogram = MACD - Signal
        """
        ema_fast = prices.ewm(span=fast, adjust=False).mean()
        ema_slow = prices.ewm(span=slow, adjust=False).mean()

        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()
        histogram = macd_line - signal_line

        return {
            'macd': macd_line,
            'signal': signal_line,
            'histogram': histogram
        }

    @staticmethod
    def bollinger_bands(prices, period=20, std_dev=2):
        """
        Bollinger Bands
        Price tends to return to middle band
        """
        sma = prices.rolling(window=period).mean()
        std = prices.rolling(window=period).std()

        upper_band = sma + (std * std_dev)
        lower_band = sma - (std * std_dev)

        return {
            'upper': upper_band,
            'middle': sma,
            'lower': lower_band
        }

    @staticmethod
    def generate_signals(df):
        """
        Generate trading signals from indicators
        Returns: 1 (buy), -1 (sell), 0 (hold)
        """
        signals = []

        for i in range(len(df)):
            # RSI signal
            rsi = df['rsi'].iloc[i] if 'rsi' in df else 50
            if rsi < 30:
                rsi_signal = 1  # oversold = buy
            elif rsi > 70:
                rsi_signal = -1  # overbought = sell
            else:
                rsi_signal = 0

            # MACD signal
            if 'macd' in df and 'signal' in df:
                macd = df['macd'].iloc[i]
                signal = df['signal'].iloc[i]
                if macd > signal:
                    macd_signal = 1  # bullish
                else:
                    macd_signal = -1  # bearish
            else:
                macd_signal = 0

            # Combine signals (simple voting)
            combined = rsi_signal + macd_signal
            if combined >= 1:
                signals.append(1)  # buy
            elif combined <= -1:
                signals.append(-1)  # sell
            else:
                signals.append(0)  # hold

        return signals

# Example usage
if __name__ == "__main__":
    # Generate sample price data
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=100, freq='H')
    prices = pd.Series(np.random.randn(100).cumsum() + 100, index=dates)

    # Calculate indicators
    ti = TechnicalIndicators()

    df = pd.DataFrame({'price': prices})
    df['sma_20'] = ti.sma(prices, 20)
    df['rsi'] = ti.rsi(prices, 14)

    macd_data = ti.macd(prices)
    df['macd'] = macd_data['macd']
    df['signal'] = macd_data['signal']

    bb = ti.bollinger_bands(prices)
    df['bb_upper'] = bb['upper']
    df['bb_middle'] = bb['middle']
    df['bb_lower'] = bb['lower']

    df['signal'] = ti.generate_signals(df)

    print("📊 Technical Indicators Calculated")
    print(f"RSI: {df['rsi'].iloc[-1]:.2f}")
    print(f"MACD: {df['macd'].iloc[-1]:.2f}")
    print(f"Signal: {df['signal'].iloc[-1]} (1=buy, -1=sell, 0=hold)")
