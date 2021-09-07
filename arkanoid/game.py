import pygame as pg
from arkanoid import ALTO, ANCHO
#from . import ALTO, ANCHO --> desde mi propio modulo(otra opción)
#Iniciamos el juego
from arkanoid.escenas import Portada

pg.init()

class Game():
    def __init__(self):
        #creamos la pantalla
        pantalla = pg.display.set_mode((ANCHO, ALTO))  
        #lista de escenas
        self.escenas = [Portada(pantalla)]  
    
    #montamos el bucle principal
    def launch(self): 
        self.escenas[0].bucle_principal()

        pg.quit()
        
       
    

