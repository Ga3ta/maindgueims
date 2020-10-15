import pygame
from box import *
from answers_box import *
from screen_text import *

class DisplayPhysics:

    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    def init_var(self):
        self.exercise = 'Si un tren va a 100 km/h en una vía de 100 km,'
        self.exercise2 = '¿cuánto tiempo tardará en recorrer toda la vía?'
        self.train_asset = pygame.image.load('assets/tren.jpg')
        self.train_asset = pygame.transform.scale(self.train_asset, (600//3, 472//3))
        self.box_answer1 = Box(self.size, self.screen,1,0)
        self.box_answer2 = Box(self.size, self.screen,1,1)
        self.box_answer3 = Box(self.size, self.screen,1,-1)
        self.box_answer1.init_var()
        self.box_answer2.init_var()
        self.box_answer3.init_var()

        self.secondary_font = pygame.font.Font('assets/Diagramm-Regular.ttf', self.size//25)

        self.exercise_text = self.secondary_font.render(str(self.exercise), True, (0, 0, 0), (255, 255, 255))
        self.exercise_textRect = self.exercise_text.get_rect()
        self.exercise_textRect.center = (self.size //2, self.size // 2+self.size // 10)

        self.exercise2_text = self.secondary_font.render(str(self.exercise2), True, (0, 0, 0), (255, 255, 255))
        self.exercise2_textRect = self.exercise2_text.get_rect()
        self.exercise2_textRect.center = (self.size //2, self.size // 2+self.size // 7)

    def show(self):
        self.box_answer1.show()
        self.box_answer2.show()
        self.box_answer3.show()

        self.screen.blit(self.train_asset, ((self.size // 2) -(600//3//2), self.size // 2-(472//3//2)-self.size//8))
        self.screen.blit(self.exercise_text, self.exercise_textRect)
        self.screen.blit(self.exercise2_text, self.exercise2_textRect)

