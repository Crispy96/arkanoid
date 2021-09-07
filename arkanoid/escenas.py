import pygame as pg
from . import FPS

class Escena():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass

#nos muestra un texto o una imagen y espera que pulsemos espacio para lanzar la partida
class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        #añadimos la imagen al lienzo
        self.logo = pg.image.load("resources/images/arkanoid_name.png")
    def bucle_principal(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            self.pantalla.fill((80, 80, 255))
            #blit es para poner un lienzo encima de otro
            self.pantalla.blit(self.logo, (140,100))

            pg.display.flip()

#nos muestra la raqueta, la bola, los ladrillos y espera que tu uses derecha/izqu y vaya acumulando puntos
class Partida(Escena):
    pass

#nos saldra una pantalla con varios record y en el caso de que tu hayas sacado más nos pedira nuestras iniciales
class Record(Escena):
    pass
   