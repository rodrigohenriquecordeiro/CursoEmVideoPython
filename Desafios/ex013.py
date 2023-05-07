nome = input('Qual o nome do funcionário? ')
salario = float(input('Qual o valor do salário atual? '))
resultado = salario * 1.15
print('O salário de {}, com 15% de aumento, irá de R$ {:.2f} para R$ {:.2f} no final do mês.'.format(nome, salario, resultado))
