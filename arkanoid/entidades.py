#definiremos los objetos que necesitamos
import pygame as pg
from pygame.sprite import Sprite

class Raqueta(Sprite):
    disfraces = "electric00.png" #no lleva self porque es una varibale de clase
    def __init__(self, **kwargs):  #rectangulo
        self.image = pg.image.load(f"resources/images/{self.disfraces}")  #tenemos que añadirle el self para que sepa que esta en la clase
        self.rect = self.image.get_rect(**kwargs) 

    def update(self):
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.rect.x -= 5

        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.rect.x +=5
