print('*' * 25, 'DESAFIO 048', '*' * 25)

# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3
# e que se encontram no intervalo de de 1 a 500.

s = 0
cont = 0
for c in range(1, 501, 2): # Outro exemplo: usando a terceira parte do Range para ganhar velocidade no processamento.
    if c % 3 == 0:
        s += c
        cont += 1
print('\nA soma de {} valores solicitados é {}'.format(cont, s))
print('Fim')
