print('*' * 25, 'DESAFIO 067', '*' * 25)

# Faça um programa que mostra a tabuada de vários números, uma de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

from time import sleep
print('-' * 20)
print('APRENDENDO TABUADA')
print('-' * 20)

while True:
    tabuada = int(input('Digite um número: '))
    resultado = 0
    if tabuada < 0:
        break
    for c in range(1, 11):
        resultado = tabuada * c
        print(f'{tabuada} x {c} = {resultado}')
print('Encerrando aprendizado da Tabuada...')
sleep(2)
print('Obrigado!')
