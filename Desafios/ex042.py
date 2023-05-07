print('*' * 25, 'DESAFIO 042', '*' * 25)

# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais.
# - Esósceles: dois lados iguais.
# - Escaleno: todos os lados diferentes.

r1 = float(input('Digite a medida do lado A: '))
r2 = float(input('Digite a medida do lado B: '))
r3 = float(input('Digite a medida do lado C: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nOs segmentos acima PODEM FORMAR um triângulo')
    if r1 == r2 == r3:
          print('É um Triângulo Equilátero.')
    elif r1 != r2 != r3 != r1:
          print('É um Triângulo Escaleno.')
    else:
          print('É um Triângulo Esósceles.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
