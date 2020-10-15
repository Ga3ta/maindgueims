import pygame
from box import *
from answers_box import *
from screen_text import *
from quadratic import *

class DisplayOrthography:

    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    def init_var(self):
        self.words='aquivaloqueestahaciendogaeta'
        self.secondary_font = pygame.font.Font('assets/Diagramm-Regular.ttf', self.size//10)
        self.exercise_text = self.secondary_font.render(str(self.words),True, (0, 0, 0), (255, 255, 255))
        self.exercise_textRect = self.exercise_text.get_rect()
        self.exercise_textRect.center = (self.size //2, self.size // 2)

    def show(self):
        self.screen.blit(self.exercise_text, self.exercise_textRect)
