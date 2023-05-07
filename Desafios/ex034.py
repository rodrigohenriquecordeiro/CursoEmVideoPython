print('*' * 25, 'DESAFIO 034', '*' * 25)

print('\nEscreva um programa que pergunte o salário de um funcionário e calcule o\n'
      'valor do seu aumento. Para salários superiores a R$ 1250,00, calcule\n'
      'aumento de 10%. Para inferiores ou iguais, o aumento será de 15%.\n')

salario = float(input('Qual o seu salario? R$ '))
if salario > 1250.00:
    aumento = salario + (salario * 10 / 100)
    print('\nVocê tem direito a 10% de aumento!')
    print('Seu novo salário será R$ {:.2f}.'.format(aumento))
else:
    aumento = salario + (salario * 15 / 100)
    print('Você tem direito a 15% de aumento!')
    print('Seu novo salário sera R$ {:.2f}.'.format(aumento))
