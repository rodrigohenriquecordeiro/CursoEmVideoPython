print('*' * 25, 'DESAFIO 049', '*' * 25)

# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o for.

t = int(input('\nDigite um número inteiro para o cálculo da tabuada: '))
print('Tabuada do {}:'.format(t))
for c in range(1, 11):
    print('{} x {} = {}.'.format(t, c, t*c))
print('Fim.')
