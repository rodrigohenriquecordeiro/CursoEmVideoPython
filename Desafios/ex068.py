print('*' * 25, 'DESAFIO 068', '*' * 25)

# Faça um programa que jogue Par ou Ímpar com o computador. O jogo só será interrompido
# quando o Jogador perder, mostrando o total de vitórias consecultivas que ele conquistou.

from random import randint

print('--' * 11)
print('P.A.R   ou   Í.M.P.A.R')
print('--' * 11)

while True:
    # nome = str(input('Qual o nome do jogador? '))
    jogador = 'Rodrigo'
    computador = 'Computador'
    print(f'{jogador} você quer jogar com PAR ou ÍMPAR?')
    cont = escolhaJogador = 0
    par = impar = ''
    while cont < 1:
        escolhaJogador = int(input('Digite 0 para PAR ou 1 para ÍMPAR: '))
        if escolhaJogador == 0:     # Jogador escolheu PAR
            par = jogador
            impar = computador
            print(f'{jogador} você escolheu PAR e o Computador jogará com ÍMPAR.')
            cont += 1
        elif escolhaJogador == 1:   # Jogador escolheu ÍMPAR
            impar = jogador
            par = computador
            print(f'{jogador} você escolheu ÍMPAR e o Computador jogará com PAR.')
            cont += 1
        else:
            print('Opção inválida, tente novamente.')
            cont += 0
    print('--' * 20)
    print('Próxima etapa do jogo')
    jogada = int(input(f'{jogador} agora escolha entre 0 e 10: '))
    computador = randint(0, 10)
    print('--' * 20)
    print(f'''{jogador} sua escolha: {jogada} 
Computador sua escolha: {computador}''')
    soma = jogada + computador
    print('--' * 20)
    vitoria = 0
    if soma % 2 == 0:
        print(f'{par} você venceu!')
        if par == 'Rodrigo':
            vitoria += 1
        else:
            break
    else:
        print(f'{impar} você venceu!')
        if impar == 'Rodrigo':
            vitoria += 1
        else:
            break
    print('--' * 20)
print(f'{jogador} você venceu {vitoria} partidas.')
print('Fim')
