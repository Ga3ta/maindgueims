from box import *
from screen_text_chemistry import *

#Esta clase es un objeto que inicializa y muestra los elementos del juego de quimica
class DisplayChemistry:
    #La función con la que se instancia el objeto
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen
    #Una función que inicializa variables y otros objetos que necesita llamar para
    #mostrar en la pantalla de los problemas de quimica, funcion que se llama solo 1 vez
    def init_var(self):
        self.bg_surface_game = pygame.image.load('assets/background3.jpg')
        self.bg_surface_game = pygame.transform.scale(self.bg_surface_game, (self.size, self.size))
        self.question_box = Box(self.size, self.screen)
        self.screen_text = ScreenText(self.size,self.screen)
        self.screen_text.init_var()
        self.question_box.init_var()
    #Una función que esta en un ciclo mostrando los elementos
    def show(self):
        self.question_box.show()
        self.screen_text.show()

