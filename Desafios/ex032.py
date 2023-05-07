print('*' * 25, 'DESAFIO 032', '*' * 25)

print('\nFaça um programa que leia um ano qualquer e mostre se ele é bissexto.')

ano = int(input('\nDigite um ano: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('{} é bissexto.'.format(ano))
        else:
            print('{} não é bissexto.'.format(ano))
    else:
        print('{} é bissexto.'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))
