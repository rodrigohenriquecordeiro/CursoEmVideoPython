print('*' * 25, 'DESAFIO 071', '*' * 25)

# Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte
# ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues (1, 10, 20 e 50).

print('=' * 30)
print('{:^30}'.format('BANCO RHC'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} céduas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break
print('=' * 30)
print('Fim da Operação')
