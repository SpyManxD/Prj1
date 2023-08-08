"""
data_analysis.py
This file implements the DataAnalysis class, which is responsible for performing data analysis on market data.
"""

import pandas as pd

class DataAnalysis:
    def __init__(self, market_data: pd.DataFrame):
        """
        Initializes the DataAnalysis class.
        Args:
            market_data (pd.DataFrame): The market data to analyze.
        """
        self.market_data = market_data

    def calculate_moving_average(self, window: int) -> pd.Series:
        """
        Calculates the moving average of the market data.
        Args:
            window (int): The window size for the moving average calculation.
        Returns:
            pd.Series: The moving average series.
        """
        return self.market_data['close'].rolling(window=window).mean()

    def calculate_rsi(self, window: int) -> pd.Series:
        """
        Calculates the relative strength index (RSI) of the market data.
        Args:
            window (int): The window size for the RSI calculation.
        Returns:
            pd.Series: The RSI series.
        """
        diff = self.market_data['close'].diff()
        up = diff.where(diff > 0, 0)
        down = -diff.where(diff < 0, 0)
        avg_gain = up.rolling(window=window).mean()
        avg_loss = down.rolling(window=window).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_bollinger_bands(self, window: int, std_dev: int) -> pd.DataFrame:
        """
        Calculates the Bollinger Bands of the market data.
        Args:
            window (int): The window size for the Bollinger Bands calculation.
            std_dev (int): The number of standard deviations for the Bollinger Bands calculation.
        Returns:
            pd.DataFrame: The Bollinger Bands dataframe.
        """
        rolling_mean = self.market_data['close'].rolling(window=window).mean()
        rolling_std = self.market_data['close'].rolling(window=window).std()
        upper_band = rolling_mean + (std_dev * rolling_std)
        lower_band = rolling_mean - (std_dev * rolling_std)
        bollinger_bands = pd.DataFrame({
            'upper_band': upper_band,
            'lower_band': lower_band
        })
        return bollinger_bands
