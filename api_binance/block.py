import requests
import json

block_hash = '00000000000000000000ae234c2137d8df6671e355012da2a7951f51513429fc'
response = requests.get(f'https://blockchain.info/rawblock/{block_hash}')

if response.status_code == 200:
    block_data = json.loads(response.text)
    transactions = block_data['tx']
    print(f'Block {block_hash} contains {len(transactions)} transactions:')
    for tx in transactions:
        print(f'Transaction hash: {tx["hash"]}, '
              f'inputs count: {len(tx["inputs"])}, '
              f'outputs count: {len(tx["out"])}, '
              f'total BTC output: {sum([out["value"] for out in tx["out"]]) / 10**8:.8f}')
else:
    print(f'Request failed with status code {response.status_code}')
