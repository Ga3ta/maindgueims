import pygame
from random import randint
from box import *
from screen_text_chemistry import *
import math_set

class DisplayMath:

    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    def init_var(self):
        self.values = []
        self.bg_surface_game = pygame.image.load('assets/background4.jpg')
        self.bg_surface_game = pygame.transform.scale(self.bg_surface_game, (self.size, self.size))
        self.intake=math_set.new_quadratic()
        self.secondary_font = pygame.font.Font('assets/Diagramm-Regular.ttf', self.size//10)

        self.exercise_text = self.secondary_font.render(str(self.intake[0])+'x^2 + '+str(self.intake[1])+' x + '+str(self.intake[2]),
                                                        True, (0, 0, 0), (255, 255, 255))
        self.exercise_textRect = self.exercise_text.get_rect()
        self.exercise_textRect.center = (self.size //2, self.size // 2)

        if(self.intake[4]==1):
            self.values.append(str(self.intake[3][0]) + ", " + str(self.intake[3][1]))
            self.values.append("{0:.2f}".format(randint(-10, 10)+ randint(0,100)/100))
            self.values.append("No hay soluciones")
        elif(self.intake[4]==0):
            self.values.append(str(self.intake[3][0]))
            self.values.append("{0:.2f}, {1:.2f}".format(randint(-10, 10)+ randint(0,100)/100, randint(-10, 10)+ randint(0,100)/100))
            self.values.append("No hay soluciones")
        else:
            self.values.append(str(self.intake[3][0]))
            self.values.append("{0:.2f}, {1:.2f}".format(randint(-10, 10)+ randint(0,100)/100, randint(-10, 10)+ randint(0,100)/100))
            self.values.append(str(randint(-10, 10)+ round(randint(0,100)/100, 2)))
 
        self.answer_text=display_answers.AnswersDisplay(self.size,self.screen,self.values)
        self.answer_text.init_var()


    def show(self):
        self.answer_text.show()
        self.screen.blit(self.exercise_text, self.exercise_textRect)

