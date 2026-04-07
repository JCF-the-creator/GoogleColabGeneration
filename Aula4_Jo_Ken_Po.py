import random #importa a biblioteca para sortear um numero

import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def verificarValor(valor):
  try:
    valor = int(valor)
    return valor
  except ValueError:
    limpar_tela()
    print(f"Erro: o menu deve receber um número, sem texto ou caracteres")
    return None
  
def Jogo():
    valor = None
    while valor == None:
        print(f"\nSelecione o modo de jogo")
        valor = verificarValor(input(f"\n[1]PVP = Jogador1 vs Jogador2 \n[2]PVE = Jogador1 vs Computador \n[3]Regras \n[4]Sair\n"))
        if valor in [1, 2, 3, 4]:
            menuPrincipal = int(valor)
        else:
            limpar_tela()
            print(f"Digite um valor acessivel no Menu")
            print(f"\n")
            valor = None

    if (menuPrincipal == 1):
        PvP()

    if (menuPrincipal == 2):
        PvE()

    if (menuPrincipal == 3):
        limpar_tela()
        print(f"="*58)
        print(f"\nRegras:")
        print(f"\n")
        print(f"\nPara vencer é necessário que:")
        print(f"\n")
        print(f"\nCaso jogue Pedra a vitória será se o oponente jogou Tesoura")
        print(f"\nCaso jogue Tesoura a vitória será se o oponente jogou Papel")
        print(f"\nCaso jogue Papel a vitória será se o oponente jogou Pedra")
        print(f"\n")
        print(f"\nJogadas Iguais recebem Empate")
        print(f"\n")
        print(f"="*58)
        print(f"\n")
        Jogo()

    if (menuPrincipal == 4):
        aberto = False
        return aberto

def menuJogada(jogada):
    valor = None
    while valor == None:
        print(f"\nSelecione sua jogada")
        valor = verificarValor(input(f"\n[1]Pedra \n[2]Papel \n[3]Tesoura\n"))
        if valor in [1, 2, 3]:
            jogada = int(valor)
            return jogada
        else:
            limpar_tela()
            print(f"Digite um valor acessivel no Menu")
            print(f"\n")
            valor = None

def menuSair(menuJN):
    valor = None
    while valor == None:
        print(f"\nDeseja Jogar novamente")
        valor = verificarValor(input(f"\n[1]Sim \n[2]Não,voltar ao Menu inicial \n[3]Sair\n"))
        if valor in [1, 2, 3]:
            menuJN = int(valor)
            return menuJN
        else:
            limpar_tela()
            print(f"Digite um valor acessivel no Menu")
            print(f"\n")
            valor = None


def PvP():

    jogada = None
    limpar_tela()
    jogador1 = input(f"\nDigite o nome do Jogador 1: \n")
    jogadaP1 = None

    limpar_tela()
    jogador2 = input(f"\nDigite o nome do Jogador 2: \n")
    jogadaP2 = None

    menuJN = 1
    PontoP1 = 0
    PontoP2 = 0
    while menuJN == 1:

        limpar_tela()
        print(f"\n{jogador1}:")
        jogadaP1 = menuJogada(jogada)
        if(jogadaP1==1):
            print(f"\nVocê jogou Pedra")
        elif(jogadaP1==2):
            print(f"\nVocê jogou Papel")
        elif(jogadaP1==3):
            print(f"\nVocê jogou Tesoura")
        input(f"\nDigite qualquer tecla para continuar")

        limpar_tela()
        print(f"\n{jogador2}:")
        jogadaP2 = menuJogada(jogada)
        if(jogadaP2==1):
            print(f"\nVocê jogou Pedra")
        elif(jogadaP2==2):
            print(f"\nVocê jogou Papel")
        elif(jogadaP2==3):
            print(f"\nVocê jogou Tesoura")
        input(f"\nDigite qualquer tecla para continuar")

        limpar_tela()
        if((jogadaP1==1 and jogadaP2==3) or (jogadaP1==2 and jogadaP2==1) or (jogadaP1==3 and jogadaP2==2)):
            PontoP1 = PontoP1 + 1
            if(jogadaP1==1):
                print(f"\nPedra ganha de Tesoura, vencedor da rodada {jogador1}!")
            elif(jogadaP1==2):
                print(f"\nPapel ganha de Pedra, vencedor da rodada {jogador1}!")
            elif(jogadaP1==3):
                print(f"\nPapel ganha de Pedra, vencedor da rodada {jogador1}!")
            
        elif((jogadaP1==3 and jogadaP2==1) or (jogadaP1==1 and jogadaP2==2) or (jogadaP1==2 and jogadaP2==3)):
            PontoP2 = PontoP2 + 1
            if(jogadaP2==1):
                print(f"\nPedra ganha de Tesoura, vencedor da rodada {jogador2}!")
            elif(jogadaP2==2):
                print(f"\nPapel ganha de Pedra, vencedor da rodada {jogador2}!")
            elif(jogadaP2==3):
                print(f"\nPapel ganha de Pedra, vencedor da rodada {jogador2}!")
        else:
            if(jogadaP2==1):
                print(f"\nAmbos Jogaram Pedra, Empate!")
            elif(jogadaP2==2):
                print(f"\nAmbos Jogaram Papel, Empate!")
            elif(jogadaP2==3):
                print(f"\nAmbos Jogaram Tesoura, Empate!")

        jogadaP1 = None
        jogadaP2 = None

        print(f"\n")
        print(f"\nPontuação: {jogador1} = {PontoP1}")
        print(f"\n           {jogador2} = {PontoP2}")

        menuJN = menuSair(menuJN)
    
    if(menuJN == 2):
        Jogo()

def PvE():
    jogada = None
    limpar_tela()
    jogador1 = input(f"\nDigite o nome do Jogador 1: \n")
    jogadaP1 = None

    limpar_tela()
    jogador2 = "Computador"
    jogadaP2 = None

    menuJN = 1
    PontoP1 = 0
    PontoP2 = 0
    while menuJN == 1:

        limpar_tela()
        print(f"\n{jogador1}:")
        jogadaP1 = menuJogada(jogada)
        if(jogadaP1==1):
            print(f"\nVocê jogou Pedra")
        elif(jogadaP1==2):
            print(f"\nVocê jogou Papel")
        elif(jogadaP1==3):
            print(f"\nVocê jogou Tesoura")
        input(f"\nDigite qualquer tecla para continuar")

        limpar_tela()
        print(f"\n{jogador2}:")
        jogadaP2 = random.randint(1, 3)
        if(jogadaP2==1):
            print(f"\nComputador jogou Pedra")
        elif(jogadaP2==2):
            print(f"\nComputador jogou Papel")
        elif(jogadaP2==3):
            print(f"\nComputador jogou Tesoura")
        input(f"\nDigite qualquer tecla para continuar")

        limpar_tela()
        if((jogadaP1==1 and jogadaP2==3) or (jogadaP1==2 and jogadaP2==1) or (jogadaP1==3 and jogadaP2==2)):
            PontoP1 = PontoP1 + 1
            if(jogadaP1==1):
                print(f"\nPedra ganha de Tesoura, vencedor da rodada {jogador1}!")
            elif(jogadaP1==2):
                print(f"\nPapel ganha de Pedra, vencedor da rodada {jogador1}!")
            elif(jogadaP1==3):
                print(f"\nPapel ganha de Pedra, vencedor da rodada {jogador1}!")
            
        elif((jogadaP1==3 and jogadaP2==1) or (jogadaP1==1 and jogadaP2==2) or (jogadaP1==2 and jogadaP2==3)):
            PontoP2 = PontoP2 + 1
            if(jogadaP2==1):
                print(f"\nPedra ganha de Tesoura, vencedor da rodada {jogador2}!")
            elif(jogadaP2==2):
                print(f"\nPapel ganha de Pedra, vencedor da rodada {jogador2}!")
            elif(jogadaP2==3):
                print(f"\nPapel ganha de Pedra, vencedor da rodada {jogador2}!")
        else:
            if(jogadaP2==1):
                print(f"\nAmbos Jogaram Pedra, Empate!")
            elif(jogadaP2==2):
                print(f"\nAmbos Jogaram Papel, Empate!")
            elif(jogadaP2==3):
                print(f"\nAmbos Jogaram Tesoura, Empate!")

        jogadaP1 = None
        jogadaP2 = None

        print(f"\n")
        print(f"\nPontuação: {jogador1} = {PontoP1}")
        print(f"\n           {jogador2} = {PontoP2}")

        menuJN = menuSair(menuJN)
    
    if(menuJN == 2):
        Jogo()

print(f"\nBem vindo ao Pedra, Papel e Tesoura")
Jogo()
