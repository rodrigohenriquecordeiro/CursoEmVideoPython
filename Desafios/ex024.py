print('*' * 25, 'DESAFIO 024', '*' * 25)

print('\nCrie um programa que leia o nome de uma cidade e informe se ela começa com o nome Santos.')

cidade = str(input('\nQual o nome da cidade? ')).strip()
print(cidade[:5].upper() == 'SANTO')

print('*' * 60)
