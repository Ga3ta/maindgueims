import pygame
from box import *
from screen_text_chemistry import *
import orthography_set

#Una clase que muestra los problemas de ortografia
class DisplayOrthography:
    # La función con la que se instancia el objeto
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen
    # Una función que llama el diccionario de palabras de orthography_set y inicializa los textos
    #función que se llama solo 1 vez
    def init_var(self):
        self.intake=orthography_set.get_word()
        self.values=[]
        self.bg_surface_game = pygame.image.load('assets/background2.jpg')
        self.bg_surface_game = pygame.transform.scale(self.bg_surface_game, (self.size, self.size))

        self.words=self.intake[1]
        self.secondary_font = pygame.font.Font('assets/Diagramm-Regular.ttf', self.size//20)
        self.exercise_text = self.secondary_font.render(str(self.words),True, (0, 0, 0), (255, 255, 255))
        self.exercise_textRect = self.exercise_text.get_rect()
        self.exercise_textRect.center = (self.size //2, self.size // 2)

        self.intake[2].remove(self.intake[0])
        self.values.append(self.intake[0])
        self.values.append(self.intake[2][0])
        self.values.append(self.intake[2][1])
        self.answer_text=display_answers.AnswersDisplay(self.size,self.screen,self.values)
        self.answer_text.init_var()
    # Una función que esta en un ciclo mostrando los elementos
    def show(self):
        self.answer_text.show()
        self.screen.blit(self.exercise_text, self.exercise_textRect)

