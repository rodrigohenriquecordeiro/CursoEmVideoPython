preco = float(input('Qual o preço de um produto? R$ '))
desconto = float(input('Qual o valor do desconto? '))
resultado = preco - (preco * desconto / 100)
print('Meu produto custa R$ {:.2f} e está com {:.2f} % de desconto.'.format(preco, desconto))
print('O preço final será de: R$ {:.2f}.'.format(resultado))
print('O valor do desconto é R$ {}'.format(desconto))
