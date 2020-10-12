import pygame
from element import *
from answers_element import *

class Display:

    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    def init_var(self):
        self.score = 100
        self.lives = 3;
        self.lifes = pygame.image.load('assets/life.png')
        self.lifes = pygame.transform.scale(self.lifes, (self.size//15, self.size//15))

        self.secondary_font = pygame.font.Font('assets/Diagramm-Regular.ttf', self.size//20)

        self.score_text = self.secondary_font.render('Score: '+str(self.score), True, (0, 0, 0), (255, 255, 255))
        self.score_textRect = self.score_text.get_rect()
        self.score_textRect.center = (self.size // 5, self.size // 18)

        self.lifes_text = self.secondary_font.render('Lifes', True, (0, 0, 0), (255, 255, 255))
        self.lifes_textRect = self.score_text.get_rect()
        self.lifes_textRect.center = ((self.size // 10) * (8)+self.size//9, self.size // 18)

        self.element = Element(self.size, self.screen)
        self.element_answers1 = AnswersElement(self.size, 0, self.screen)
        self.element_answers2 = AnswersElement(self.size, 1, self.screen)
        self.element_answers3 = AnswersElement(self.size, -1, self.screen)
        self.element.init_var()
        self.element_answers1.init_var()
        self.element_answers2.init_var()
        self.element_answers3.init_var()

    def show(self):
        self.element.show()
        self.element_answers1.show()
        self.element_answers2.show()
        self.element_answers3.show()

        if self.lives > 2:
           self.screen.blit(self.lifes, ((self.size // 10) * (9), self.size // 10))
        if self.lives > 1:
           self.screen.blit(self.lifes, ((self.size // 10) * (8), self.size // 10))
        if self.lives > 0:
           self.screen.blit(self.lifes, ((self.size // 10) * (7), self.size // 10))

        self.screen.blit(self.score_text, self.score_textRect)
        self.screen.blit(self.lifes_text, self.lifes_textRect)
