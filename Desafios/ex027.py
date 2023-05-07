print('*' * 25, 'DESAFIO 027', '*' * 25)

print('\nFaça um progrma que leia o nome completo de uma pessoa, mostrando em '
      'seguida o primeiro e último nome de forma separada.')

n = str(input('\nDigite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
