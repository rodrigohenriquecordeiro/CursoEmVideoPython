print('*' * 25, 'DESAFIO 059', '*' * 25)

# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1 = int(input('\nDigite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
escolha = 0
while escolha != 5:
    print('''\nO que você gostaria de fazer com os dois números?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    escolha = int(input('Digite sua escolha: '))
    if escolha == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
    elif escolha == 2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} e {} é igual a {}.'.format(n1, n2, multiplicar))
    elif escolha == 3:
        if n1 > n2:
            print('O maior número é: {}'.format(n1))
        else:
            print('O maior número é: {}'.format(n2))
    elif escolha == 4:
        print('Escolha novos números:')
        n1 = float(input('Digite sua primeira escolha: '))
        n2 = float(input('Digite sua segunda escolha: '))
        print('Suas escolhas são o número {} e {}.'.format(n1, n2))
    elif escolha == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida, tente novamente.')
    print('*' * 30)
print('Fim do programa! Volte sempre.')
