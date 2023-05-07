print('*' * 25, 'DESAFIO 018', '*' * 25)

print('\nFaça um programa que leia um ângulo qualquer e mostre na tela o valor'
      'do Seno, Cosseno e Tangente desse ângulo.\n')

from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do Ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('\nO Seno do Ângulo {} é {:.2f}.'.format(angulo, seno))
print('O Cosseno do Ângulo {} é {:.2f}.'.format(angulo, cosseno))
print('A Tangente do Ângulo {} é {:.2f}.\n'.format(angulo, tangente))

print('*' * 29, 'FIM', '*' * 29)
