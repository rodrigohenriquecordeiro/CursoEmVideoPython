print('*' * 25, 'DESAFIO 070', '*' * 25)

# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final:
# [a] qual é o total de gastos na compra.
# [b] quantos produtos custam mais de de R$ 1000.
# [c] qual é o nome do produto mais barato?

total = totmil = menor = cont = barato = 0
while True:
    produto = str(input('Qual o produto? ')).strip().capitalize()
    preco = float(input('Qual o preço do produto: R$ '))
    cont += 1
    total += preco
    if preco >= 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' Fim do Programa '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000,00.')
print(f'O produto mais barato é {barato} custa R$ {menor:.2f}')
