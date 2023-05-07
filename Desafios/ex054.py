print('*' * 25, 'DESAFIO 054', '*' * 25)

# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = 0
menor = 0

for c in range(1, 4):
    nascimento = int(input('Em que ano você nasceu? '))
    idade = atual - nascimento
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('Dessa listagem temos {} pessoas com menos de 21 anos.\n'
      'e {} pessoas com mais de 21 anos.'.format(menor, maior))
