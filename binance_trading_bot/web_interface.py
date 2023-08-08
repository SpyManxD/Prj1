## web_interface.py
from flask import Flask, jsonify, request
from trading_bot import TradingBot

app = Flask(__name__)
bot = TradingBot()

@app.route('/account/balance', methods=['GET'])
def get_account_balance():
    balance = bot.get_account_balance()
    return jsonify({'balance': balance})

@app.route('/orders', methods=['GET'])
def get_open_orders():
    orders = bot.get_open_orders()
    return jsonify(orders)

@app.route('/orders/history', methods=['GET'])
def get_order_history():
    history = bot.get_order_history()
    return jsonify(history)

@app.route('/market/data', methods=['GET'])
def get_market_data():
    market_data = bot.get_market_data()
    return jsonify(market_data)

@app.route('/trading/performance', methods=['GET'])
def get_trading_performance():
    performance = bot.get_trading_performance()
    return jsonify(performance)

if __name__ == '__main__':
    app.run()
