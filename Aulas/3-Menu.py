print('\033[1:36m=' * 20)
print('\033[mRestaurante R.H.C.')
print('\033[1:36m=' * 20)

print('\033[1:36m1. \033[mDomingo')
print('\033[1:36m2. \033[mSegunda-feira')
print('\033[1:36m3. \033[mTerça-feira')
print('\033[1:36m4. \033[mQuarta-feira')
print('\033[1:36m5. \033[mQuinta-feira')
print('\033[1:36m6. \033[mSexta-feira')
print('\033[1:36m7. \033[mSábado')

menu = int(input('\033[34mTecle o número do dia da semana para ter acesso ao cardápio:\033[m '))

if menu == 1:
    print('\033[1;33mDOMINGO:\033[m '
          '\033[1:36mFrango Assado, Macarão ao Molho Pesto e Legumes no Vapor.')
elif menu == 2:
    print('\033[1;33mSEGUNDA-FEIRA:\033[m '
          '\033[1:36mPicadinho de Carne, Salada de Batata e Arroz Carreteiro.')
elif menu == 3:
    print('\033[1;33mTERÇA-FEIRA:\033[m '
          '\033[1:36mMacarrão Alho e Óleo, Frango Frito e Purê Cenoura.')
elif menu == 4:
    print('\033[1;33mQUARTA-FEIRA:\033[m '
          '\033[1:36mPeixa no Vapor, Lentinha e Salada de Brocólis.')
elif menu == 5:
    print('\033[1;33mQUINTA-FEIRA:\033[m '
          '\033[1:36mPicanha Suína, Arroz Pardo e Salada de Macarrão.')
elif menu == 6:
    print('\033[1;33mSEXTA-FEIRA:\033[m '
          '\033[1:36mVirado a Paulista, Bolinho de Arroz e Cuscus.')
elif menu == 7:
    print('\033[1;33mSÁBADO:\033[m '
          '\033[1:36mFeijoada Completa.')
else:
    print('Tente novamente escolher o cardápio.')
