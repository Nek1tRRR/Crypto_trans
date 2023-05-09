import requests
import json


block_hash = '00000000000000000000ae234c2137d8df6671e355012da2a7951f51513429fc'
response = requests.get(f'https://blockchain.info/rawblock/{block_hash}')

if response.status_code == 200:
    block_data = json.loads(response.text)
    print(block_data)
else:
    print(f'Request failed with status code {response.status_code}')
