import pygame
from box import *

#Clase auxiliar de display, la cual muestra elementos que siempre estan presentes en los juegos (vidas, score, ....)
class DisplayScreen:
    # La función con la que se instancia el objeto
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen
        self.score = 100
        self.lives = 3

    # Esta función inicializa los textos, las cajas de respuesta y el sprite de corazon, se llama 1 vez
    def init_var(self):

        self.lifes = pygame.image.load('assets/life.png')
        self.lifes = pygame.transform.scale(self.lifes, (self.size//15, self.size//15))

        self.secondary_font = pygame.font.Font('assets/Diagramm-Regular.ttf', self.size//20)

        self.score_text = self.secondary_font.render('Score: '+str(self.score), True, (0, 0, 0), (255, 255, 255))
        self.score_textRect = self.score_text.get_rect()
        self.score_textRect.center = (self.size // 5, self.size // 18)

        self.lifes_text = self.secondary_font.render('Lifes', True, (0, 0, 0), (255, 255, 255))
        self.lifes_textRect = self.score_text.get_rect()
        self.lifes_textRect.center = ((self.size // 10) * (8)+self.size//9, self.size // 18)

        self.box_answer1 = Box(self.size, self.screen,1,0)
        self.box_answer2 = Box(self.size, self.screen,1,1)
        self.box_answer3 = Box(self.size, self.screen,1,-1)
        self.box_answer1.init_var()
        self.box_answer2.init_var()
        self.box_answer3.init_var()
    # Una función que esta en un ciclo mostrando los elementos
    def show(self):

        if self.lives > 2:
           self.screen.blit(self.lifes, ((self.size // 10) * (9), self.size // 10))
        if self.lives > 1:
           self.screen.blit(self.lifes, ((self.size // 10) * (8), self.size // 10))
        if self.lives > 0:
           self.screen.blit(self.lifes, ((self.size // 10) * (7), self.size // 10))

        self.screen.blit(self.score_text, self.score_textRect)
        self.screen.blit(self.lifes_text, self.lifes_textRect)
        self.box_answer1.show()
        self.box_answer2.show()
        self.box_answer3.show()
