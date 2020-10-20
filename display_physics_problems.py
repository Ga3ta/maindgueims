import pygame
from box import *
import random
import physics_set
import display_answers

class DisplayPhysics:

    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    def init_var(self):
        self.values=physics_set.get_prob()
        self.bg_surface_game = pygame.image.load('assets/background.jpg')
        self.bg_surface_game = pygame.transform.scale(self.bg_surface_game, (self.size, self.size))

        self.exercise = str(self.values[1])
        self.exercise2 = str(self.values[2])
        if self.values[0]==0:
            self.vehicle_asset = pygame.image.load('assets/tren.jpg')
            self.vehicle_asset = pygame.transform.scale(self.vehicle_asset,(600//(self.size//160), 472//(self.size//160)))
        elif self.values[0]==1:
            self.vehicle_asset = pygame.image.load('assets/barco.jpg')
            self.vehicle_asset = pygame.transform.scale(self.vehicle_asset,(600 // (self.size // 160), 472 // (self.size // 160)))
        elif self.values[0] == 2:
            self.vehicle_asset = pygame.image.load('assets/auto.jpg')
            self.vehicle_asset = pygame.transform.scale(self.vehicle_asset,(600 // (self.size // 160), 472 // (self.size // 160)))

        self.secondary_font = pygame.font.Font('assets/Diagramm-Regular.ttf', self.size//25)

        self.exercise_text = self.secondary_font.render(str(self.exercise), True, (0, 0, 0), (255, 255, 255))
        self.exercise_textRect = self.exercise_text.get_rect()
        self.exercise_textRect.center = (self.size //2, self.size // 2+self.size // 10)

        self.exercise2_text = self.secondary_font.render(str(self.exercise2), True, (0, 0, 0), (255, 255, 255))
        self.exercise2_textRect = self.exercise2_text.get_rect()
        self.exercise2_textRect.center = (self.size //2, self.size // 2+self.size // 7)

        self.values.pop(0)
        self.values[0]=int(random.randint(int(self.values[2]-30),int(self.values[2]+30)))
        self.values[1] =int(random.randint(int(self.values[2] - 30),int(self.values[2] + 30)))
        self.answer_text=display_answers.AnswersDisplay(self.size,self.screen,self.values)
        self.answer_text.init_var()

    def show(self):
        self.answer_text.show()
        self.screen.blit(self.vehicle_asset, ((self.size // 2) -(600//(self.size//160)//2), self.size // 2-((600//(self.size//160)//2)+self.size//12)))
        self.screen.blit(self.exercise_text, self.exercise_textRect)
        self.screen.blit(self.exercise2_text, self.exercise2_textRect)

