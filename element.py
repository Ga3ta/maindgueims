import pygame

class Element:
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

        self.file = open("assets/Tp.txt", "r")
        self.elements = []

        for line in self.file:
            e = line.split(",")
            self.elements.append({"name": e[0], "symbol": e[1], "number": int(e[2])})

        self.element = self.elements[38]["symbol"]
        self.number = self.elements[38]["number"]
        self.name = self.elements[38]["name"]

    def init_var(self):

        self.font_size=1
        self.square_size = int(self.size//2)
        self.square_pos_x = int(self.size // 2 - self.square_size // 2)
        self.square_pos_y = int((self.size // 2 - self.square_size // 2) - (self.size / 10))

        self.color = (255, 255, 255)

        element_font = pygame.font.Font('assets/Diagramm-Regular.ttf', self.font_size)

        self.font_size = self.size//4
        self.element_symbol_text = element_font.render(str(self.element), True, (0, 0, 0), (255, 255, 255))
        self.element_symbol_textRect = self.element_symbol_text.get_rect()
        self.element_symbol_textRect.center = (self.size // 2, self.size // 2 - (self.size // 14))

        self.font_size = self.size//8
        self.element_number_text = element_font.render(str(self.number), True, (0, 0, 0), (255, 255, 255))
        self.element_number_textRect = self.element_number_text.get_rect()
        self.element_number_textRect.center = (self.size // 2 - (self.size // 6), self.size // 2 - (self.size // 4))

        self.font_size = self.size//10
        self.element_name_text = element_font.render(str(self.name), True, (0, 0, 0), (255, 255, 255))
        self.element_name_textRect = self.element_name_text.get_rect()
        self.element_name_textRect.center = (self.size// 2, self.size // 2 + (self.size // 14))

    def show(self):
        pygame.draw.rect(self.screen, self.color,[self.square_pos_x, self.square_pos_y, self.square_size, self.square_size])
        self.screen.blit(self.element_symbol_text, self.element_symbol_textRect)
        self.screen.blit(self.element_number_text, self.element_number_textRect)
        self.screen.blit(self.element_name_text, self.element_name_textRect)
