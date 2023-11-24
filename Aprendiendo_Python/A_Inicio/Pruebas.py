import pygame, sys

from pygame.locals import *

 

pygame.init()
#crea ventana                       #ancho,largo
DISPLAYSURF = pygame.display.set_mode((800, 700))

pygame.display.set_caption('Juego el Ahorcado')

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()