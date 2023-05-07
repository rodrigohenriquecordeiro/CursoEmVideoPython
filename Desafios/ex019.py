print('*' * 25, 'DESAFIO 019', '*' * 25)

print('\nUm professor quer sortear um dos seus quatro alunos para apagar\n'
      'o quadro. Faça um programa que ajude ele, lendo o nome deles e\n'
      'escrevendo o nome escolhido.\n')

from random import choice

n1 = str(input('Digite o 1º nome: '))
n2 = str(input('Digite o 2º nome: '))
n3 = str(input('Digite o 3º nome: '))
n4 = str(input('Digite o 4º nome: '))
lista = [n1, n2, n3, n4]

nome = choice(lista)
print('\nO aluno escolhido é {}.\n'.format(nome))

print('*' * 29, 'FIM', '*' * 29)
