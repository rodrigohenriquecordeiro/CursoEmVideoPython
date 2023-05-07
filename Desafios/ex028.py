print('*' * 25, 'DESAFIO 028', '*' * 25)

print('\nEscreva um programa que faça o computador pensar em um número inteiro\n'
      'entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número\n'
      'escolhido pelo computador. O programa deverá escrever da tela se o\n'
      'usuário venceu ou perdeu.\n')

from random import randint
from time import sleep
n = randint(0, 5)

u = int(input('Usuário, tente acertar o número que o computador "pensou".\nDigite sua opção aqui: '))

print('Processando...')
sleep(3)

if u == n:
    print('PARABENS! Você acertou.')
else:
    print('ERROU! O computador pensou no número {}.'.format(n))
