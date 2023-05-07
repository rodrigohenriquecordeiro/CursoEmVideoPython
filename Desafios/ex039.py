print('*' * 25, 'DESAFIO 039', '*' * 25)

# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou o que passou do prazo.

from datetime import date
nascimento = int(input('\nEm que ano você nasceu? '))
atual = date.today().year
idade = atual - nascimento

if idade == 18:
      print('Você tem {} anos. Hora de se alistar!'.format(idade))
elif idade < 18:
      print('Você tem {} anos. Ainda não está na hora'.format(idade))
      saldo = 18 - idade
      print('Falta {} anos para seu alistamento.'.format(saldo))
else:
      saldo = idade - 18
      print('Você tem {} anos. Passou da hora de se alistar.'.format(idade))
      print('Passou {} anos do seu alistamento.'.format(saldo))
