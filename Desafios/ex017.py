print('*' * 25, 'DESAFIO 017', '*' * 25)

print('\nFaça um programa que leia o comprimento do Cateto Oposto e o Cateto Adjacente\n'
      'de um Triângulo Retângulo. Calcule e mostre o comprimento da Hipotenusa.\n')

from math import hypot
co = float(input('Digite em cm o Cateto Oposto: '))
ca = float(input('Digite em cm o Cateto Adjacente: '))
h = hypot(co, ca)
print('\nA Hipotenusa é {:.2f} cm.\n'.format(h))

print('*' * 29, 'FIM', '*' * 29)
