# -*- coding: utf-8 -*-

import requests

url = 'https://www.mercadobitcoin.net/api/ETH/ticker/'

response = requests.get(url)

data = response.json()

preco = float(data['ticker']['last'])

print("Preço atual do Bitcoin: R${:.2f}".format(preco))

# Calculando proporção de 50 reais em Bitcoin
proporcao_50 = 50 / preco
print("Com R$50 você pode comprar {:.8f} Bitcoins".format(proporcao_50))

# Calculando proporção de 100 reais em Bitcoin
proporcao_100 = 100 / preco
print("Com R$100 você pode comprar {:.8f} Bitcoins".format(proporcao_100))


# python3.10 Moedas/bitcoin_BRL.py

