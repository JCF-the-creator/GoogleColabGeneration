jogador1 = int(input('informe um numero: '))
jogador2 = int(input('informe um numero: '))

numero = jogador1 + jogador2

if(numero%2 == 0):
    print(f"\nPar ganhou")
else:
    print(f"\nImpar ganhou")