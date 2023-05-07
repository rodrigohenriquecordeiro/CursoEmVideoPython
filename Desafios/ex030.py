print('*' * 25, 'DESAFIO 030', '*' * 25)

print('\nCrie um programa que leia um número inteiro e mostre se ele é par ou ímpar.')

n = int(input('\nDigite um número inteiro: '))
if n % 2 == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O número {} é ÍMPAR!'.format(n))
