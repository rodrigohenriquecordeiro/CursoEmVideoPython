print('*' * 25, 'DESAFIO 056', '*' * 25)

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre:
# A média da idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

s = 0
maior = 0
menor = 0
velho = ''
contador = 0
for c in range(1, 5):
    nome = input('Qual o seu nome? ').capitalize().strip()
    idade = int(input('Qual a sua idade? '))
    sexo = input('Qual seu sexo? (M/F): ').upper().strip()
    s += idade
    if c == 1 and sexo == 'M':
        maior = idade
        menor = idade
    else:
        if idade > maior and sexo == 'M':
            maior = idade
            velho = nome
        else:
            print('Nenhum homem cadastrado.')
        if sexo == 'F' and idade <= 20:
            contador += 1
        else:
            print('Nenhuma mulher cadastrada.')
media = s / 4
print('A média da idade do grupo: {:.1f}'.format(media))
print('O homem mais velho: {}.'.format(velho))
print('Temos {} mulher(s) com menos de 20 anos.'.format(contador))
