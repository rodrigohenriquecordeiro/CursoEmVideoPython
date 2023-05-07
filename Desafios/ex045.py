print('*' * 25, 'DESAFIO 045', '*' * 25)

# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)

nome = input('\nQual o seu nome? ').strip().capitalize()
print('''\nOpções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Digite sua escolha: '))
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÓ!!!')

print('-=' * 11)
print('Computador jogou {}.'.format(itens[computador]))
print('{} jogou {}.'.format(nome, itens[jogador]))
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('{} VENCEU'.format(nome))
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('{} VENCEU'.format(nome))
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('{} VENCEU'.format(nome))
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
else:
    print('JOGADA INVÁLIDA!')
