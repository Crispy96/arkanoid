import pygame as pg
from arkanoid import ALTO, ANCHO
#from . import ALTO, ANCHO --> desde mi propio modulo(otra opción)
#Iniciamos el juego
pg.init()

class Game():
    def __init__(self):
        #creamos la pantalla
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))  
    
    #montamos el bucle principal
    def launch(self): 
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            self.pantalla.fill(123,123,255)

            #pasar todo a la memoria gráfica
            pg.display.flip()

        
        pg.quit()
       
    

