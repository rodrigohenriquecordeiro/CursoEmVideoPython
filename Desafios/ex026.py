print('*' * 25, 'DESAFIO 026', '*' * 25)

print('\nFaça um programa que leia uma frase pelo teclado e mostre: ')

frase = str(input('\nDigite uma frase: ')).strip().upper()
print(frase)

print('\n- Quantas vezes aparece a letra A:', frase.count('A'))

print('- Em que posição ela aparece pela primeira vez: ', frase.find('A')+1)

print('- Em que posição ela aparece pela última vez: ', frase.rfind('A')+1)

print('*' * 60)
