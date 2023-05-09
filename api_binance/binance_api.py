from binance.client import Client
import json
binance_api_key = 'LIo9od4BlNPMlUso943CeSDgFWCw4QAcXyFjKyAKHXG4EFoAXdtxxtxeOjjmI6vB'
binance_api_secret = 'qKpha7hUt1wY704Ll11hCSbsRGO4I2aYx4ar5lZSIBJG9Iw5HUAaL4c32emSISka'

client = Client(binance_api_key, binance_api_secret)
# res=client.get_exchange_info()
res = client.get_all_tickers()
# res = client.get_symbol_info("NEARUSDT")
# res = client.price("NEARUSDT")
with open("res.txt", "w") as f:
    json.dump(res, f, ensure_ascii=False, indent=4)
print()

binance_symbol_info = client.get_symbol_info('BTCUSDT')
print(binance_symbol_info)

#################################################################



