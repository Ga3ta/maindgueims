import pygame
from box import *
from screen_text import *
from quadratic import *

class DisplayMath:

    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    def init_var(self):
        self.values=new_quadratic()

        self.secondary_font = pygame.font.Font('assets/Diagramm-Regular.ttf', self.size//10)

        self.exercise_text = self.secondary_font.render(str(self.values[0])+'x^2 '+str(self.values[1])+'x '+str(self.values[0]),
                                                        True, (0, 0, 0), (255, 255, 255))
        self.exercise_textRect = self.exercise_text.get_rect()
        self.exercise_textRect.center = (self.size //2, self.size // 2)

    def show(self):
        self.screen.blit(self.exercise_text, self.exercise_textRect)
        print(self.values)

