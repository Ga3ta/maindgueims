import pygame
import random
import display_answers
import chemistry_set

#Clase auxiliar de display_chemistry_problems para mostrar los textos de los problemas de quimica
class ScreenText:
    # La función con la que se instancia el objeto
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen
    # La función que inicializa los textos y manda llamar el diccionario con los mismos,funcion que se llama solo 1 vez
    def init_var(self):
        self.data_questions=chemistry_set.element_variables()

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

        self.data_questions.pop(0)
        self.data_questions.pop(0)
        self.answer_text=display_answers.AnswersDisplay(self.size,self.screen,self.data_questions)
        self.answer_text.init_var()

    # Una función que esta en un ciclo mostrando los elementos
    def show(self):
        self.answer_text.show()
        self.screen.blit(self.element_symbol_text, self.element_symbol_textRect)
        self.screen.blit(self.element_number_text, self.element_number_textRect)
        self.screen.blit(self.element_name_text, self.element_name_textRect)