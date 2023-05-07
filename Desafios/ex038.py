print('*' * 25, 'DESAFIO 038', '*' * 25)

# Escreva um programa que lei dois números inteiros e compare-os, mostrando na tela a mensagem:
# - O primeiro valor é maior.
# - O segunvo valor é menor.
# - Não existe valor maior, os dois são iguais.

n1 = int(input('\nDigite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
      print('O primeiro valor é maior.')
elif n2 > n1:
      print('O segundo valor é maior.')
else:
      print('Os valores são iguais.')
