from pybit.unified_trading import HTTP

api_key = 'dLLU7pY8JjARdZbral'
api_secret = 'EwVNbZkDBN2MtGOsjLiR3J6FCKf6Zl8A75Qi'

session = HTTP(
    testnet=False,
    api_key=api_key,
    api_secret=api_secret,
)

print(session.get_coin_info(symbol="BTCUSDT"))