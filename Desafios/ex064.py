print('*' * 25, 'DESAFIO 064', '*' * 25)

# Crie um programa que leia vários números inteiros pelo teclado. O programa só irá parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

c = soma = 0
n = int(input('Digite um número inteiro: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número inteiro: '))
print('Foram digitados {} números.'.format(c))
print('A soma entre eles é igual {}'.format(soma))
print('FIM')
