import pygame
import question_set
import random

class ScreenText:
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    def init_var(self):
        self.data_questions=question_set.throw_questions()
        element_font = pygame.font.Font('assets/Diagramm-Regular.ttf', ((self.size//100)*45)//2)
        self.element_symbol_text = element_font.render(str(self.data_questions[0]), True, (0, 0, 0), (255, 255, 255))
        self.element_symbol_textRect = self.element_symbol_text.get_rect()
        self.element_symbol_textRect.center = (self.size // 2, self.size // 2 - (self.size // 10))

        element_font = pygame.font.Font('assets/Diagramm-Regular.ttf', ((self.size//100)*45)//6)
        self.element_number_text = element_font.render(str(self.data_questions[1]), True, (0, 0, 0), (255, 255, 255))
        self.element_number_textRect = self.element_number_text.get_rect()
        self.element_number_textRect.center = ((self.size // 2 - ((self.size//100)*45) // 2)
                                               +self.size//13, ((self.size // 2 - ((self.size//100)*45) // 2)
                                                                - (self.size / 10))+self.size//13)
        element_font = pygame.font.Font('assets/Diagramm-Regular.ttf', ((self.size//100)*45)//6)
        self.element_name_text = element_font.render('?', True, (0, 0, 0), (255, 255, 255))
        self.element_name_textRect = self.element_name_text.get_rect()
        self.element_name_textRect.center = (self.size//2, self.size // 2 + (((self.size//100)*45) // 10))

    def show(self):

        self.screen.blit(self.element_symbol_text, self.element_symbol_textRect)
        self.screen.blit(self.element_number_text, self.element_number_textRect)
        self.screen.blit(self.element_name_text, self.element_name_textRect)