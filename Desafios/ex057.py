print('*' * 25, 'DESAFIO 057', '*' * 25)

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja
# errado, peça a digitação novamente até ter um valor correto.

sexo = ''
contador = 0
while contador < 1:
    sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            sexo = 'Masculino'
            print('Sexo digitado: {}.'.format(sexo))
            contador += 1
        if sexo == 'F':
            sexo = 'Feminino'
            print('Sexo digitado: {}.'.format(sexo))
            contador += 1
    else:
        print('Opção digitada incorretamente.')
        print('Digite M para masculino e F para feminino.')
        contador += 0
print('Fim')
