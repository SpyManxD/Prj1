from typing import List
import pandas as pd
from api import BinanceAPI
from data_analysis import DataAnalysis
from strategies import Strategy
from utils import calculate_profit, calculate_percentage_change

class TradingBot:
    def __init__(self, api_key: str, secret_key: str):
        """
        Initializes the TradingBot class.
        Args:
            api_key (str): The Binance API key.
            secret_key (str): The Binance secret key.
        """
        self.api = BinanceAPI(api_key, secret_key)
        self.data_analysis = None
        self.strategy = None

    def execute_strategy(self, strategy: Strategy) -> None:
        """
        Executes the specified strategy.
        Args:
            strategy (Strategy): The strategy to execute.
        """
        # Fetch market data
        market_data = self.api.get_market_data()

        # Perform data analysis
        self.data_analysis = DataAnalysis(market_data)
        self.data_analysis.calculate_indicators()

        # Execute strategy
        self.strategy = strategy
        self.strategy.execute(self.data_analysis)

    def get_account_balance(self) -> float:
        """
        Fetches the account balance.
        Returns:
            float: The account balance.
        """
        return self.api.get_account_balance()

    def get_open_orders(self) -> List[dict]:
        """
        Fetches the open orders.
        Returns:
            List[dict]: The open orders.
        """
        return self.api.get_open_orders()

    def get_order_history(self) -> List[dict]:
        """
        Fetches the order history.
        Returns:
            List[dict]: The order history.
        """
        return self.api.get_order_history()

    def get_market_data(self) -> pd.DataFrame:
        """
        Fetches the market data.
        Returns:
            pd.DataFrame: The market data.
        """
        return self.api.get_market_data()

    def get_trading_performance(self) -> pd.DataFrame:
        """
        Fetches the trading performance.
        Returns:
            pd.DataFrame: The trading performance.
        """
        # Fetch account balance
        initial_balance = self.api.get_account_balance()

        # Fetch order history
        order_history = self.api.get_order_history()

        # Calculate profit and percentage change
        final_balance = self.api.get_account_balance()
        profit = calculate_profit(initial_balance, final_balance)
        percentage_change = calculate_percentage_change(initial_balance, final_balance)

        # Create trading performance dataframe
        trading_performance = pd.DataFrame({
            'timestamp': [pd.Timestamp.now()],
            'profit': [profit],
            'percentage_change': [percentage_change]
        })

        return trading_performance
