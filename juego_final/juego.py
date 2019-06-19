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
        self.accion=0
        self.gravedad=0
        self.direccion=0
        self.image=self.m[self.accion][self.col]
        self.rect=self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]
        self.velx = 0
        self.vely = 0
    def update(self):

        self.rect.x += self.velx

        self.image=self.m[self.accion][self.col]
        self.image=pygame.transform.scale(self.image,[2*30,2*60])

        if self.direccion==1:
            self.image=pygame.transform.flip(self.image,180,0)
        else:
            self.image=pygame.transform.flip(self.image,0,0)

        if self.col<self.lim[self.accion]:
            self.col+=1
        else:
            self.col=0
        if self.rect.y!=320:
            self.rect.y+=self.vely
            self.col=3
        else:
            self.vely=0
            self.gravedad=0

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
    posy=-684
    posx=0
    reloj=pygame.time.Clock()
    img2=pygame.image.load("mapa.png")
    pj2=pygame.image.load("movimiento.png")
    lim=[2,2,5,9,7,9,3,3]
    esta=cortar(pj2,30,50,8,17)
    reco=0
    lim_mapa=[1024]
    img2=pygame.transform.scale(img2,[6143*2,900*2])

    pantalla.blit(img2,[posx,posy])

    jugadores=pygame.sprite.Group()
    j=jugador(esta,lim,[0,320])
    jugadores.add(j)

    while not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_DOWN:
                    j.vely=0
                    j.velx=0
                    j.accion=1
                    j.col=0
                    posx=0
                    posy=-584
                if event.key== pygame.K_UP:
                    j.vely=+10
                    j.velx=0
                    j.accion=2
                    j.rect.y=j.rect.y-80
                    j.gravedad=10
                    posx=0
                    posy=-584
                if event.key== pygame.K_LEFT:
                    j.vely=0
                    j.velx=-10
                    j.accion=3
                    j.col=0
                    j.direccion=1
                    posy=-584
                    posx=0
                if event.key== pygame.K_RIGHT:
                    j.vely=0
                    j.velx=+10
                    j.accion=3
                    j.col=0
                    j.direccion=0
                    pos=-584
                    posx=0
                    if j.rect.x>=500:
                        posx-=10
                        j.velx=0
            if event.type==pygame.KEYUP:
                posy=-584
                j.velx=0
                j.accion=0

        jugadores.update()
        pantalla.fill(NEGRO)

        pantalla.blit(img2,[posx,-700])
        jugadores.draw(pantalla)
        pygame.display.flip()

        reloj.tick(10)
