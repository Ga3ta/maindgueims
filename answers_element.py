import pygame

class AnswersElement:

    def __init__(self, size, pos, screen):
        self.size = size
        self.screen = screen
        self.pos = pos

        self.file = open("assets/Tp.txt", "r")
        self.elements = []

        for line in self.file:
            e = line.split(",")
            self.elements.append({"name": e[0], "symbol": e[1], "number": int(e[2])})

        self.element = self.elements[38]["symbol"]
        self.number = self.elements[38]["number"]
        self.name = self.elements[38]["name"]

    def init_var(self):
        self.answer1 = self.element
        self.answer2 = self.element
        self.answer3 = self.element

        self.color = (255, 255, 255)

        self.element_answers_font = pygame.font.Font('assets/Diagramm-Regular.ttf', 30)

        self.lil_square_size = int(self.size // 4)

        self.lil_square_pos_x = int(self.size // 2 - self.lil_square_size*2 // 2 // 2)
        self.lil_square_pos_y = int((self.size // 2 - self.lil_square_size*2 // 2) + ((self.size // 14) * 6))

        self.element_answer_text = self.element_answers_font.render(str(self.answer1), True, (0, 0, 0), (255, 255, 255))
        self.element_answer_textRect = self.element_answer_text.get_rect()
        self.element_answer_textRect.center = (self.size // 2 - 100, self.size // 2 + (self.size // 3))


    def show(self):
        self.screen.blit(self.element_answer_text, self.element_answer_textRect)
        pygame.draw.rect(self.screen, self.color,
                         [self.lil_square_pos_x - self.size // 3, self.lil_square_pos_y, self.lil_square_size, self.lil_square_size])







