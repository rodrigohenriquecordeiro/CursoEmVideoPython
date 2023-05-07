print('*' * 25, 'DESAFIO 037', '*' * 25)

# Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de converção.

print('''\nDigite um número inteiro e escolha para qual base será convertido:
1 - para Binário.
2 - para Octal.
3 - para Hexadecimal.''')

n = int(input('Número: '))
b = int(input('Base: '))
if b == 1:
      print('Binário {}.'.format(bin(n)[2:]))
elif b == 2:
      print('Octal {}.'.format(oct(n)[2:]))
elif b == 3:
      print('Hexadecial {}.'.format(hex(n)[2:]))
else:
      print('Opção inválida. Tente novamente.')
