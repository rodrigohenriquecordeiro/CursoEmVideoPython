print('*' * 25, 'DESAFIO 066', '*' * 25)

# Crie um programa que leia vários números inteiros pelo teclado. O programa só irá
# parar quando o usuário digitar o valor 999. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).

c = soma = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'\nForam digitados {c} números e a soma entre eles é igual a {soma}.')
print('Fim')
