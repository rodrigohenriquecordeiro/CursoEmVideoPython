print('*' * 25, 'DESAFIO 069', '*' * 25)

# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastradas, o
# computador deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# [a] quantas pessoas tem mais de 18 anos.
# [b] quantos homens foram cadastradas.
# [c] quantas mulheres tem menos de 20 anos.

tot18 = totH = totM = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade <= 20:
        totM += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens: {totH}')
print(f'Total de mulheres com menos de 20 anos: {totM}')
