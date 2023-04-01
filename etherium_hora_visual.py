
# -*- coding: utf-8 -*-
import requests
import json
import time
from playsound import playsound

# Definir os valores de referência

valor_referencia1 = 10950
valor_referencia2 = 6000

# Definir as porcentagens de diferença para cima e para baixo

porcentagem_up = 0.03
porcentagem_down = 0.1

# Definir o caminho do arquivo de som

sound_file = 'alarm.wav'

# Definir o preço da última consulta

last_price = None

while True:
    # Configurar as informações da API do Mercado Bitcoin
    coin = 'ETH'
    method = 'ticker'

    # Definir a URL da API
    url = f'https://www.mercadobitcoin.net/api/{coin}/{method}/'

    # Fazer uma requisição GET para a API
    response = requests.get(url)

    # Extrair os dados da resposta
    data = response.json()

    # Extrair o preço atual do Etherium
    price = float(data['ticker']['last'])

    # Obter a data e hora atual
    current_time = time.strftime('%H:%M   %d/%m/%Y')

    # Imprimir o preço atual do Etherium
    print(f'Preço Etherium: {price:.2f}   {current_time}')

    # Verificar se o preço ultrapassou o valor de referência 1
    if price >= valor_referencia1:
        # Tocar o arquivo de som
        playsound(sound_file)

        # Emitir um alerta
        print('AVISO: Preço do Etherium ultrapassou o valor de referência 1!')

        break

    # Verificar se o preço ultrapassou o valor de referência 2
    if price <= valor_referencia2:
        # Tocar o arquivo de som
        playsound(sound_file)

        # Emitir um alerta
        print('AVISO: Preço do Etherium ficou abaixo do valor de referência 2!')

        break

    # Verificar se o preço mudou mais que a porcentagem definida para cima ou para baixo
    if last_price is not None:
        diff = price / last_price - 1
        if abs(diff) >= porcentagem_up:
            # Tocar o arquivo de som
            playsound(sound_file)

            # Emitir um alerta
            print(f'GAP ENCONTRADO: Preço do Etherium subiu ou desceu mais que {porcentagem_up:.0%} '
                  f'desde a última consulta!')

            break
        elif abs(diff) >= porcentagem_down:
            # Tocar o arquivo de som
            playsound(sound_file)

            # Emitir um alerta
            print(f'GAP ENCONTRADO: Preço do Etherium caiu mais que {porcentagem_down:.0%} '
                  f'desde a última consulta!')

            break

    # Atualizar o preço da última consulta
    last_price = price

    # Esperar por um minuto antes de fazer a próxima consulta
    time.sleep(60)


#   python3.10 Moedas/etherium_hora_visual.py

