import pygame as pg
from arkanoid import ALTO, ANCHO
#from . import ALTO, ANCHO --> desde mi propio modulo(otra opción)
#Iniciamos el juego
from arkanoid.escenas import Portada, Partida, Records

pg.init()

class Game():
    def __init__(self):
        pantalla = pg.display.set_mode((ANCHO, ALTO))  #creamos la pantalla
        self.escenas = [Portada(pantalla), Partida(pantalla), Records(pantalla)]

    def launch(self):  #montamos el bucle principal(infinito)
        i = 0

        while True:
            self.escenas[i].bucle_principal()  #llama a la escena para que se represente
            i += 1
            if i == len(self.escenas):
                i = 0

            # fórmula matemática equivalente al if de arriba
            # i = (i + 1) % len(self.escenas)                
      
    

