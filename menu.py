import pygame

class Menu:
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    def init_var(self):
        self.secondary_font = pygame.font.Font('assets/Diagramm-Regular.ttf', self.size//20)

        self.title_text = self.secondary_font.render('TRIVIA', True, (0, 0, 0), (255, 255, 255))
        self.title_textRect = self.title_text.get_rect()
        self.title_textRect.center = (self.size // 2, self.size // 10)

        self.game1_text = self.secondary_font.render('Quimica', True, (0, 0, 0), (255, 255, 255))
        self.game1_textRect = self.game1_text.get_rect()
        self.game1_textRect.center = (self.size // 4, self.size //2)

        self.game2_text = self.secondary_font.render('Matematicas', True, (0, 0, 0), (255, 255, 255))
        self.game2_textRect = self.game2_text.get_rect()
        self.game2_textRect.center = ((self.size // 4)*3, self.size //2)

        self.game3_text = self.secondary_font.render('Fisica', True, (0, 0, 0), (255, 255, 255))
        self.game3_textRect = self.game3_text.get_rect()
        self.game3_textRect.center = (self.size // 4, (self.size // 4)*3)

        self.game4_text = self.secondary_font.render('Biologia', True, (0, 0, 0), (255, 255, 255))
        self.game4_textRect = self.game4_text.get_rect()
        self.game4_textRect.center = ((self.size // 4)*3, (self.size // 4)*3)



    def show(self):
        self.screen.blit(self.title_text, self.title_textRect)
        self.screen.blit(self.game1_text, self.game1_textRect)
        self.screen.blit(self.game2_text, self.game2_textRect)
        self.screen.blit(self.game3_text, self.game3_textRect)
        self.screen.blit(self.game4_text, self.game4_textRect)
