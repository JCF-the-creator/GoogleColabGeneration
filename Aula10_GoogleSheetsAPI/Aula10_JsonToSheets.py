import requests
import json
from datetime import datetime 

url = "https://script.google.com/macros/s/AKfycbzUvH8NVsaUvzfYFFBTmz_4xmdTj9wGNu-jK_kCkES_4QublVq-9EL-vs7oM3IQ01zrHg/exec"

def enviar_dados(placa, carro, funcionario):
    # vou colocar aqui a data e hora
    data_e_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    parametros = {
        'data_hora': data_e_hora,
        'placa': placa,
        'carro': carro,
        'funcionario': funcionario
    }

    print(' enviando dados para a tabela')

    resposta = requests.post(url, json=parametros)

    if resposta.status_code == 200:
        print('Dados prontos para o envio')
    else:
        print(f'erro ao enviar os dados {resposta.status_code}')

while True:
    print(f'\n')
    placa = input(' informe a placa do carro: ')
    carro = input(' informe o modelo do carro: ')
    funcionario = input(' informe o funcionario que registrou: ')

    enviar_dados(placa, carro, funcionario)

    op = input('deseja sair? S/N ')
    if op == 's':
        break