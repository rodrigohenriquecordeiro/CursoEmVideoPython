print('*' * 25, 'DESAFIO 050', '*' * 25)

# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar desconsidere-o.

s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        cont += 1
        s += n
print('Você informou {} números pares e a soma foi {}'.format(cont, s))
