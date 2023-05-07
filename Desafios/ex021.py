print('*' * 25, 'DESAFIO 021', '*' * 25)

print('\nFaça um programa em Python que abra e reproduza o aúdio'
      'de um arquivo MP3.\n')

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

# Não consegui fazer funcionar
