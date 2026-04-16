import requests
import json
from datetime import datetime 

url = ""#inserir o link do gs do google sheets, retirado por segurança

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