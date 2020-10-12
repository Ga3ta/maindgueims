import pygame

class AnswerBox:

    def __init__(self, size, pos, screen):
        self.size = size
        self.screen = screen
        self.pos = pos

    def init_var(self):

        self.color = (255, 255, 255)
        self.lil_square_size = int(self.size // 4)
        self.lil_square_pos_x = int(self.size//2-self.lil_square_size//2+(self.lil_square_size+self.size//20)*self.pos)
        self.lil_square_pos_y = int((self.size//6)*5-self.lil_square_size//2)

    def show(self):

        pygame.draw.rect(self.screen, self.color,[self.lil_square_pos_x, self.lil_square_pos_y, self.lil_square_size, self.lil_square_size])







