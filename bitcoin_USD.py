
# -*- coding: utf-8 -*-

import requests

bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
response = requests.get(bitcoin_api_url)
response_json = response.json()
bitcoin_price = response_json['bpi']['USD']['rate']
print('Preço do Bitcoin em USD: ' + bitcoin_price.encode('utf-8'))


