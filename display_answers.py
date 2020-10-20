import pygame
import random


class AnswersDisplay:
    def __init__(self,size,screen,data_answers):
        self.size=size
        self.screen=screen
        self.data_answers=data_answers
        self.correct_index = -1
        self.correct_ans=self.data_answers[0]
        random.shuffle(self.data_answers)
        for i in range(len(self.data_answers)):
            if self.data_answers[i]==self.correct_ans:
                self.correct_index=i
                break
    def init_var(self):
        self.element_answers_font = pygame.font.Font('assets/Diagramm-Regular.ttf',(self.size // 4) // 6)

        self.element_answer_text1 = self.element_answers_font.render(str(self.data_answers[0]), True, (0, 0, 0), (255, 255, 255))
        self.element_answer_textRect1 = self.element_answer_text1.get_rect()
        self.element_answer_textRect1.center = ((self.size//2-(self.size // 4)//2+((self.size // 4)+self.size//20)*0)
                                               + (self.size // 4) // 2, ((self.size//6)*5-(self.size // 4)//2)
                                               + (self.size // 4) // 2)
        self.element_answer_text2 = self.element_answers_font.render(str(self.data_answers[1]), True, (0, 0, 0), (255, 255, 255))
        self.element_answer_textRect2 = self.element_answer_text2.get_rect()
        self.element_answer_textRect2.center = ((self.size//2-(self.size // 4)//2+((self.size // 4)+self.size//20)*1)
                                               + (self.size // 4) // 2, ((self.size//6)*5-(self.size // 4)//2)
                                               + (self.size // 4) // 2)
        self.element_answer_text3 = self.element_answers_font.render(str(self.data_answers[2]), True, (0, 0, 0), (255, 255, 255))
        self.element_answer_textRect3 = self.element_answer_text3.get_rect()
        self.element_answer_textRect3.center = ((self.size//2-(self.size // 4)//2+((self.size // 4)+self.size//20)*-1)
                                               + (self.size // 4) // 2, ((self.size//6)*5-(self.size // 4)//2)
                                               + (self.size // 4) // 2)
    def show(self):
        self.screen.blit(self.element_answer_text1, self.element_answer_textRect1)
        self.screen.blit(self.element_answer_text2, self.element_answer_textRect2)
        self.screen.blit(self.element_answer_text3, self.element_answer_textRect3)
    