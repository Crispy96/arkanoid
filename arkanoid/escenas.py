import pygame as pg
from . import FPS, ANCHO, ALTO
from .entidades import Raqueta

class Escena():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()
    
    def bucle_principal(self):
        pass
    
class Portada(Escena):    #nos muestra un texto o una imagen y espera que pulsemos espacio para lanzar la partida
    def __init__(self, pantalla): #super busca la clase padre que es Escena y le aplica el método
        super().__init__(pantalla)
        self.logo = pg.image.load("resources/images/arkanoid_name.png") #añadimos la imagen al lienzo
        fuente = pg.font.Font("resources/fonts/CabinSketch-Bold.ttf", 45)
        self.textito = fuente.render("Pulsa <SPC> para comenzar", True, (0,0,0)) #crea el texto de pulsar espacio para inciar
        self.anchoTexto = self.textito.get_width()


    def bucle_principal(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

                if evento.type == pg.KEYDOWN:  #darle funcionalidad al espacio
                    if evento.key == pg.K_SPACE:
                        game_over = True

            self.pantalla.fill((80, 80, 255))
            self.pantalla.blit(self.logo, (140, 140))   #blit es para poner un lienzo encima de otro
            self.pantalla.blit(self.textito, ((ANCHO - self.anchoTexto) // 2, 640))  #anchoTexto = self.callToAction.get_width() lo vamos a añadir debajo
            pg.display.flip()
        

#nos muestra la raqueta, la bola, los ladrillos y espera que tu uses derecha/izqu y vaya acumulando puntos
class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.fondo =pg.image.load("resources/images/background.jpg")
        self.player = Raqueta(midbottom=(ANCHO // 2, ALTO - 15) )


    def bucle_principal(self):
        game_over = False
        while not game_over:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

            self.player.update()

            self.pantalla.blit(self.fondo, (0, 0))
            self.pantalla.blit(self.player.image, self.player.rect)
            pg.display.flip()

#nos saldra una pantalla con varios record y en el caso de que tu hayas sacado más nos pedira nuestras iniciales
class Records(Escena):
    def bucle_principal(self):
        print("soy records")

