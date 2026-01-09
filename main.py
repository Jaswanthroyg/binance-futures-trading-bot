from bot import BasicBot

bot = BasicBot()

def get_user_input():
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    order_type = input("Order type (market / limit): ").lower()
    side = input("Side (buy / sell): ").upper()
    quantity = float(input("Quantity: "))

    price = None
    if order_type == "limit":
        price = float(input("Price: "))

    return symbol, order_type, side, quantity, price


try:
    symbol, order_type, side, quantity, price = get_user_input()

    if order_type == "market":
        result = bot.place_market_order(symbol, side, quantity)

    elif order_type == "limit":
        result = bot.place_limit_order(symbol, side, quantity, price)

    else:
        print("Invalid order type ❌")
        exit()

    print("Order placed successfully ✅")
    print(result)

except Exception as e:
    from logger import logger
    logger.error(str(e))
    print("Error occurred ❌")
    print(e)
