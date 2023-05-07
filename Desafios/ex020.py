print('*' * 25, 'DESAFIO 020', '*' * 25)

print('\nO mesmo professor do desafio anterior que sortear a ordem\n'
      'de apresentação de trabalhos dos alunos. Faça um programa que\n'
      'leia o nome dos quatros alunos e mostre a ordem sorteada.\n')

from random import shuffle

n1 = str(input('Digite o 1º nome: '))
n2 = str(input('Digite o 2º nome: '))
n3 = str(input('Digite o 3º nome: '))
n4 = str(input('Digite o 4º nome: '))
lista = [n1, n2, n3, n4]

shuffle(lista)
print('\nA ordem de apresentação será: \n')
print(lista)

print('*' * 29, 'FIM', '*' * 29)
