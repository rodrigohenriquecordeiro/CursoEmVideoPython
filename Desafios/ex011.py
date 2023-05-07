altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))
area = largura * altura
tinta = area / 2
print('A parede possui {:.2f} m² e precisará de {} litros de tintas para ser pintada.'.format(area, tinta))
