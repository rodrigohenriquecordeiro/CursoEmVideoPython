print('*' * 25, 'DESAFIO 022', '*' * 25)

print('\nCrie um programa que leia o nome completo de uma pessoa e mostre: \n')

nome = input('Qual o seu nome completo? ').strip()

print('\n- Nome com todos as letras maiúsculas:', nome.upper())

print('\n- Nome com todas as letras minúsculas.', nome.lower())

print('\n- Quantas letras tem ao todo (sem considerar os espaços).', len(nome.replace(' ', '')))

dividido = nome.split()
print('\n- Quantas letras tem o primeiro nome. {}\n'.format(len(dividido[0])))

print('*' * 60)
