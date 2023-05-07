print('*' * 25, 'DESAFIO 036', '*' * 25)

print('\nEscreva um programa para aprovar o empréstimo bancário de uma casa. O programa\n'
      'vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.\n'
      'Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou \n'
      'então o empréstimo será negado.\n')

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
ano = int(input('Em quantos anos você quer financiar a casa? '))
parcela = (casa / (ano * 12))

if parcela <= (0.30 * salario):
      print('Financimento aprovado!')
      print('{:.0f} parcelas de R$ {:.2f}.'.format(ano, parcela))

else:
      print('Financiamento não aprovado.')
      print('Suas parcelas de R$ {:.2f} execederiam o limite de 30% do seu selário.'.format(parcela))
