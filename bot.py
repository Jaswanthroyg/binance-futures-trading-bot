# bot.py
from binance import Client
from confi import API_KEY, API_SECRET
from logger import logger


class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)

        # IMPORTANT: testnet settings
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com'

    def get_balance(self):
         return self.client.futures_account_balance()
    def place_market_order(self, symbol, side, quantity):
        logger.info(f"Placing MARKET {side} order: {symbol}, qty={quantity}")
        response = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logger.info(f"Response: {response}")
        return response
    
def place_limit_order(self, symbol, side, quantity, price):
    logger.info(f"Placing LIMIT {side} order: {symbol}, qty={quantity}, price={price}")
    response = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            quantity=quantity,
            price=price,
            timeInForce='GTC'
        )
    logger.info(f"Response: {response}")
    return response



