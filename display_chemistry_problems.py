from box import *
from screen_text_chemistry import *

class DisplayChemistry:

    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    def init_var(self):
        self.bg_surface_game = pygame.image.load('assets/background3.jpg')
        self.bg_surface_game = pygame.transform.scale(self.bg_surface_game, (self.size, self.size))
        self.question_box = Box(self.size, self.screen)
        self.screen_text = ScreenText(self.size,self.screen)
        self.screen_text.init_var()
        self.question_box.init_var()

    def show(self):
        self.question_box.show()
        self.screen_text.show()

