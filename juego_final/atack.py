import pygame
import random


BLANCO=[255,255,255]
NEGRO=[0,0,0]
VERDE=[0,255,0]
ANCHO=640
ALTO=480


def cortar(img,anch,alto,fila,columna):
    lista=[]
    for i in range(0,fila):
        lista.append([])
        for e in range(0,columna):

            cuadro=img.subsurface(e*anch,i*alto,anch,alto)
            lista[i].append(cuadro)
    return lista

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    fin = False
    img2=pygame.image.load("mapa.png")
    pj2=pygame.image.load("movimiento.png")
    img2=pygame.transform.scale(img2,[6143*2,900*2])
    att=pygame.image.load("attac.png")
    atta=cortar(att,50,50,9,7)
    atta2=cortar(att,90,50,9,3)
    esta=cortar(pj2,30,50,8,17)
    a=0
    b=0
    while b<4:
        while a<3:
            atta[b][a+4]=atta2[b+4][a]
            a+=1
        a=0
        b+=1
    esta.apentd([])
    
    a=0
    b=0
    while not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_DOWN:
                    if b!=6:
                        b+=1
                    else:
                        b=0
                if event.key== pygame.K_UP:
                    if a!=8:
                        a+=1
                    else:
                        a=0

        pantalla.fill(NEGRO)
        pantalla.blit(atta[a][b],[0,0])
        pantalla.blit(esta[a][b],[50,50])
        pygame.display.flip()
