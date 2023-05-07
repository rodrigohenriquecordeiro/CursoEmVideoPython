print('*' * 25, 'DESAFIO 029', '*' * 25)

print('\nEscreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h\n'
      'mostre uma mensagem avisando que foi multado. A multa irá custar R$ 7,00 para cada\n'
      'km acima do limite.\n')

v = float(input('Qual velocidade você estava dirigindo? '))

if v > 80.0:
    m = (v - 80.0) * 7
    print('Sua velocidade: {:.0f} km/h.'.format(v))
    print('Acima do limite de 80 km/h permitido.\n'
          'Multa de R$ {:.2f}'.format(m))
else:
    print('Velocidade dentro do limite permitido.\n'
          'Obrigado por respeitar as leis de trânsito.')
