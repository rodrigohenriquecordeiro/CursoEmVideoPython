print('*' * 25, 'DESAFIO 055', '*' * 25)

# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input("Informe o {}º peso (kg): ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior: {} kg. Menor: {} kg'.format(maior, menor))
