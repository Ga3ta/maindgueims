import pygame
import random
import question_set

class AnswersDisplay:
    def __init__(self,size,screen):
        self.size=size
        self.screen=screen
    def init_var(self):
        self.data_answers=question_set.throw_answers()

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
    def show(self):
        self.screen.blit(self.element_answer_text1, self.element_answer_textRect1)
        self.screen.blit(self.element_answer_text2, self.element_answer_textRect2)
        self.screen.blit(self.element_answer_text3, self.element_answer_textRect3)