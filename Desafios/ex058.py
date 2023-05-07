print('*' * 25, 'DESAFIO 058', '*' * 25)

# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador irá tentar advinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

print('\nTente advinhar o número que o computador escolheu entre 0 e 10.')
from random import randint
computador = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Digite sua escolha: '))
    palpites += 1
    if jogador == computador:
        acertou = True
        print('PARABÉNS! Você acertou.')
        print('Foram necessárias {} tentativas para acertar.'.format(palpites))
    else:
        if jogador < computador:
            print('Mais...')
        else:
            print('Menos... Tente mais uma vez.')
