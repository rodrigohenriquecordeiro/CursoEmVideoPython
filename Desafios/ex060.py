print('*' * 25, 'DESAFIO 060', '*' * 25)

# Faça um programa que leia um número qualquer e mostre seu fatorial.
# Ex: 5! = 5x4x3x2x1=120

n = int(input('\nDigite um número para calcularmos o Fatorial dele: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
