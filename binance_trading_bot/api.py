"""
api.py
This file implements the BinanceAPI class, which is responsible for interacting with the Binance Futures API using the CCXT library.
"""

import ccxt

class BinanceAPI:
    def __init__(self, api_key: str, secret_key: str):
        """
        Initializes the BinanceAPI class.
        Args:
            api_key (str): The Binance API key.
            secret_key (str): The Binance secret key.
        """
        self.exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret_key
        })

    def get_account_balance(self) -> float:
        """
        Fetches the account balance from the Binance API.
        Returns:
            float: The account balance.
        """
        account_info = self.exchange.fetch_balance()
        return account_info['total']['USDT']

    def get_open_orders(self):
        """
        Fetches the open orders from the Binance API.
        Returns:
            list: The open orders.
        """
        return self.exchange.fetch_open_orders()

    def get_order_history(self):
        """
        Fetches the order history from the Binance API.
        Returns:
            list: The order history.
        """
        return self.exchange.fetch_closed_orders()

    def get_market_data(self, symbol: str):
        """
        Fetches the market data for the specified symbol from the Binance API.
        Args:
            symbol (str): The symbol to fetch market data for.
        Returns:
            list: The market data.
        """
        return self.exchange.fetch_ohlcv(symbol)

    def execute_order(self, symbol: str, order_type: str, price: float, quantity: float):
        """
        Executes an order on the Binance API.
        Args:
            symbol (str): The symbol to execute the order for.
            order_type (str): The type of the order.
            price (float): The price of the order.
            quantity (float): The quantity of the order.
        Returns:
            dict: The executed order.
        """
        return self.exchange.create_order(symbol, order_type, 'buy', quantity, price)

    def cancel_order(self, order_id: str):
        """
        Cancels an order on the Binance API.
        Args:
            order_id (str): The ID of the order to cancel.
        Returns:
            dict: The canceled order.
        """
        return self.exchange.cancel_order(order_id)
