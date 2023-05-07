print('*' * 25, 'DESAFIO 044', '*' * 25)

# Elabore um programa que calcule o valor a ser pago por um produto, considerandoo seu preço
# normal e condição de pagamento:
# - Á vista dinheiro/cheque: 10% de desconto.
# - Á vista no cartão: 5% de desconto.
# - Em até 2x no cartão: preço normal.
# - 3x ou mais no cartão: 20% de juros.

produto = float(input('\nQual o preço do produto? R$ '))
pagamento = float(input('''\nMétodos de pagamento
[1] Á vista no dinheiro/cheque: 10% de desconto.
[2] Á vista no cartão de débito: 5% de desconto.
[3] Em até 2x no cartão de crédito: preço normal.
[4] 3x ou mais no cartão de crédito: 20% de juros.
Digite sua Opção: '''))

print('\nPreço do Produto: R$ {:.2f}'.format(produto))
if pagamento == 1:
      valor = produto * 0.90
      print('Preço com 10% de Desconto: R$ {:.2f}'.format(valor))
elif pagamento == 2:
      valor = produto * 0.95
      print('Preço com 5% de Desconto: R$ {:.2f}'.format(valor))
elif pagamento == 3:
      valor = produto / 2
      print('Parcelado em 2x sem Desconto: R$ {:.2f}'.format(valor))
elif pagamento == 4:
      parcela = int(input('\nParcelamos em até 6x com acrescimento de 20% de juros.\n'
                          'Digite a quantidade de parcelas para acesso a simulação do preço: '))
      valor = (produto * 1.20) / parcela
      print('Preco Total com 20% de Juros: R$ {:.2f}\n'
            'Quantidades de Parcelas: {:.0f}\n'
            'Valor por Parcela: R$ {:.2f}\n'.format(produto * 1.20, parcela, valor))
else:
    print('Opção inválida de pagamento. Tente novamente.')
