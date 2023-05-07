print('*' * 25, 'DESAFIO 033', '*' * 25)

print('Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')

a = float(input('Digite o primeiro número para análise: '))
b = float(input('Digite o segundo número para análise: '))
c = float(input('Digite o terceiro número para análise: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado é {:.0f}.'.format(menor))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado é {:.0f}.'.format(maior))
