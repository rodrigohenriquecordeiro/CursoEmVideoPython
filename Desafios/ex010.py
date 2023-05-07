carteira = float(input('Quantos reais você tem na carteira? R$ '))
dolar = float(input('Qual a cotação do dólar hoje? USD '))
resp = carteira / dolar
print('Meus R$ {:.2f} valem hoje USD {:.2f}.'.format(carteira, resp))
