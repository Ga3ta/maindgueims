import pygame
import question_set
import random

class ScreenText:
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    def init_var(self):
        self.data_questions=question_set.throw_questions()
        self.data_answers=question_set.throw_answers()
        self.data_answers[2]=self.data_questions[2]

        self.element_answers_font = pygame.font.Font('assets/Diagramm-Regular.ttf',(self.size // 4) // 6)
        self.element_answer_text1 = self.element_answers_font.render(str(self.data_answers[random.randint(0,2)]), True, (0, 0, 0), (255, 255, 255))
        self.element_answer_textRect1 = self.element_answer_text1.get_rect()
        self.element_answer_textRect1.center = ((self.size//2-(self.size // 4)//2+((self.size // 4)+self.size//20)*0)
                                               + (self.size // 4) // 2, ((self.size//6)*5-(self.size // 4)//2)
                                               + (self.size // 4) // 2)
        self.element_answer_text2 = self.element_answers_font.render(str(self.data_answers[random.randint(0,2)]), True, (0, 0, 0), (255, 255, 255))
        self.element_answer_textRect2 = self.element_answer_text2.get_rect()
        self.element_answer_textRect2.center = ((self.size//2-(self.size // 4)//2+((self.size // 4)+self.size//20)*1)
                                               + (self.size // 4) // 2, ((self.size//6)*5-(self.size // 4)//2)
                                               + (self.size // 4) // 2)
        self.element_answer_text3 = self.element_answers_font.render(str(self.data_answers[random.randint(0,2)]), True, (0, 0, 0), (255, 255, 255))
        self.element_answer_textRect3 = self.element_answer_text3.get_rect()
        self.element_answer_textRect3.center = ((self.size//2-(self.size // 4)//2+((self.size // 4)+self.size//20)*-1)
                                               + (self.size // 4) // 2, ((self.size//6)*5-(self.size // 4)//2)
                                               + (self.size // 4) // 2)

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
        self.screen.blit(self.element_answer_text1, self.element_answer_textRect1)
        self.screen.blit(self.element_answer_text2, self.element_answer_textRect2)
        self.screen.blit(self.element_answer_text3, self.element_answer_textRect3)
        self.screen.blit(self.element_symbol_text, self.element_symbol_textRect)
        self.screen.blit(self.element_number_text, self.element_number_textRect)
        self.screen.blit(self.element_name_text, self.element_name_textRect)