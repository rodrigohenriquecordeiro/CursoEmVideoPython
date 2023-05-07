print('*' * 25, 'DESAFIO 023', '*' * 25)

print('\nFaça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.\n')

num = int(input('Número: '))

print('\nMilhar: {}'.format(num[0]))

print('Centena: {}'.format(num[1]))

print('Dezena: {}'.format(num[2]))

print('Unidade: {}\n'.format(num[3]))

print('*' * 60)

# Meu ficou incompleto por causa de números com menos de 4 algarismo. Uma opção é utilizar módulo em matemática.