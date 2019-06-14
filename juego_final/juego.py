import pygame
import random


BLANCO=[255,255,255]
NEGRO=[0,0,0]
VERDE=[0,255,0]
ANCHO=640
ALTO=480

class jugador(pygame.sprite.Sprite):
    def __init__(self,mat_i,lim,pos_ini):
        pygame.sprite.Sprite.__init__(self)
        self.m=mat_i
        self.col=0
        self.lim=lim
        self.accion=1
        self.image=self.m[self.accion][self.col]
        self.rect=self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]
        self.velx = 0
        self.vely = 0
    def update(self):

        self.rect.x += self.velx
        self.rect.y += self.vely

        self.image=self.m[self.accion][self.col]
        if self.col<self.lim[self.accion]:
            self.col+=1
        else:
            self.col=0
            self.col=0
            if self.accion!=1:
                self.accion=1

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
    pj=pygame.image.load("pj.png")
    cortar = cortar(pj,)
    img2=pygame.transform.scale(img2,[2*4960,2*815])
    posy=-584
    posx=0
    pantalla.blit(img2,[posx,posy])

    while not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_DOWN:
                    posx=0
                    posy=-584
                if event.key== pygame.K_UP:
                    posx=0
                    posy=-584
                if event.key== pygame.K_LEFT:
                    posy=-584
                    posx-=20
                if event.key== pygame.K_RIGHT:
                    pos=-584
                    posx+=20
            if event.type==pygame.KEYUP:
                pos=-584
                posx+=20
        pantalla.blit(img2,[posx,posy])

        pygame.display.flip()
