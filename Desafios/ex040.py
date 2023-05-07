print('*' * 25, 'DESAFIO 040', '*' * 25)


# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida.
# - Média abaxio de 5: REPROVADO.
# - Média entre 5 e  6.9: RECUPERAÇÃO
# - Média 7 ou superior: APROVADO.

n1 = float(input('\nNota da 1º Avaliação: '))
n2 = float(input('Nota da 2º Avaliação: '))
media = (n1 + n2) / 2
if media < 5.0:
      print('\nProva 1: {:.1f}'.format(n1))
      print('Prova 2: {:.1f}'.format(n2))
      print('Média: {:.1f}'.format(media))
      print('Status: Reprovado')
elif media >= 5 and media <= 6.9:
      print('\nProva 1: {:.1f}'.format(n1))
      print('Prova 2: {:.1f}'.format(n2))
      print('Média: {:.1f}'.format(media))
      print('Status: Recuperação')
else:
      print('\nProva 1: {:.1f}'.format(n1))
      print('Prova 2: {:.1f}'.format(n2))
      print('Média: {:.1f}'.format(media))
      print('Status: Aprovado')
