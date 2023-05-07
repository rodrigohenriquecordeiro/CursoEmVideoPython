print('\nResolvendo uma Equação de Segundo Grau com Bhasckara\n')

from math import sqrt
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = (b ** 2) - 4 * a * c

x1 = float(-b + sqrt(delta)) / (2 * (a))
x2 = float(-b - sqrt(delta)) / (2 * (a))

print('\nDelta = {:.0f}'.format(delta))
print('x1 = {:.0f}'.format(x1))
print('x2 = {:.0f}\n'.format(x2))

xv = (-b) / (-2 * a)
print('Vértice de x = {:.0f}\n'.format(xv))

yv = (-delta) / (4 * a)
print('Vértice de y = {:.0f}'.format(yv))
