print('*' * 25, 'DESAFIO 046', '*' * 25)

# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
# artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
for c in range(10, -1, -1): # O primeiro -1 é importante para o Range terminar no 0
    print(c, '-*-' * c)
    sleep(0.5)
print(30 * '=', 'FELIZ ANO NOVO!')
print('Fim')
