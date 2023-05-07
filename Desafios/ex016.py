print('\nDESAFIO 016: Crie um programa que leia um nº real e mostre na tela a sua porção inteira.\n')

from math import trunc
n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(n, trunc(n)))
