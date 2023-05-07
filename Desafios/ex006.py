n = int(input('Digite um número inteiro: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('\nO número {} tem as seguintes variaveis: \nDobro: {:_>10}. \nTriplo: {:_>9}. \nRaíz: {:_>11.2f}.'.format(n, d, t, r))
