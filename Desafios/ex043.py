print('*' * 25, 'DESAFIO 043', '*' * 25)

# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso.
# - Entre 18.5 e 25: Peso Ideal.
# - 25 até 30: Sobrepeso.
# - 30 até 40: Obesidade.
# - Acima de 40: Obesidade mórbida.

peso = float(input('\nQual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)

print('\nPeso: {:.1f} kg\n'
      'Altura: {:.2f} m\n'
      'IMC: {:.2f}'.format(peso, altura, imc))
if imc <= 18.5:
    print('Categoria: Abaixo do Peso.')
elif imc <= 25:
    print('Categoria: Peso Ideal.')
elif imc <= 30:
    print('Categoria: Sobrepeso.')
elif imc <= 40:
    print('Categoria: Obesidade.')
else:
    print('Categoria: Obesidade Mórbida.')
