print('*' * 25, 'DESAFIO 031', '*' * 25)

print('\nDesenvolva um programa  que pergunte a distância de uma viagem em km.\n'
      'Calcule o preço da passagem cobrando R$ 0,50 por km para viagens de\n'
      'até 200 km e R$ 0,45 para viagens mais longas.')

d = float(input('\nQuantos km possuem a sua viagem? '))
if d <= 200.0:
    p = d * 0.50
    print('Você percorreu {:.2f} km.'.format(d))
    print('O preço da sua viagem será: R$ {:.2f}.'.format(p))
else:
    p = d * 0.45
    print('Você percorreu {:.2f} km.'.format(d))
    print('O preço da sua viagem será: R$ {:.2f}.'.format(p))
