import pygame
import random


BLANCO=[255,255,255]
NEGRO=[0,0,0]
VERDE=[0,255,0]
ANCHO=640
ALTO=480

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    fin = False
    img2=pygame.image.load("mapa.png")
    img2=pygame.transform.scale(img2,[6143*2,900*2])

    while not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True


            pantalla.fill(NEGRO)
            pantalla.blit(img2,[-2570,-700])
            pygame.display.flip()
