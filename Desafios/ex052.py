print('*' * 25, 'DESAFIO 052', '*' * 25)

# Faça um programa que leia um número inteiro e diga se ele é primo ou não.

num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número \033[32m{} \033[mfoi divisível \033[32m{} \033[mvezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele \033[34mÉ PRIMO!')
else:
    print('\033[mE por isso ele \033[34mNÃO É PRIMO!')
