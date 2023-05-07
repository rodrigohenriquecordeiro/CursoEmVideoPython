print('Sistema de Avaliação do Motorista Parceiro da Uber')

e1 = int(input('Quantas avaliações 1 estrela você recebeu? '))
e2 = int(input('Quantas avaliações 2 estrelas você recebeu? '))
e3 = int(input('Quantas avaliações 3 estrelas você recebeu? '))
e4 = int(input('Quantas avaliações 4 estrelas você recebeu? '))
e5 = int(input('Quantas avaliações 5 estrelas você recebeu? '))
n = ((e1 * 1) + (e2 * 2) + (e3 * 3) + (e4 * 4) + (e5 * 5))/(500)

print('Sua nota é {:.2f}'.format(n))
