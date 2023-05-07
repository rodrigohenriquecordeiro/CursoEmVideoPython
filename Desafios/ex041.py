print('*' * 25, 'DESAFIO 041', '*' * 25)

# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostra sua categoria, de acordo com sua idade:
# - Até 9 anos: MIRIM.
# - Até 14 anos: INFANTIL.
# - Até 19 anos: JÚNIOR.
# - Até 25 anos: SÊNIOR.
# - Acima: MASTER.

from datetime import date
idade = date.today().year - (int(input('\nEm que ano você nasceu? ')))
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: Mirim.')
elif idade <= 14:
    print('Categoria: Infantil.')
elif idade <= 19:
    print('Categoria: Júnior.')
elif idade <= 25:
    print('Categoria: Sênior.')
else:
    print('Categoria: Master.')
