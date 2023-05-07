print('*' * 25, 'DESAFIO 035', '*' * 25)

print('\nDesenvolva um programa que leia  o comprimento de três retas e\n'
      'diga ao usuário se elas podem ou não formar um triângulo.\n')

r1 = float(input('Digite a medida do lado A: '))
r2 = float(input('Digite a medida do lado B: '))
r3 = float(input('Digite a medida do lado C: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
