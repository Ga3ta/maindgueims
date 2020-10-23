'''
Importamos el módulo pygame para la interfaz gráfica del juego
'''
import pygame

'''
Generamos una variable gp de tipo booleano para la siguiente función
'''
gp=False

'''
Esta función nos regresa si el mouse fue liberado para checar el menú y evitar bugs
al checar la actividad del mouse cuando se usa get_pressed()
'''
def get_released():
    global gp
    if(gp==False):
        if(pygame.mouse.get_pressed()[0]==True):
            gp=True
        return False
    else:
        if(pygame.mouse.get_pressed()[0]==False):
            gp = False
            return True
        else:
            return False

'''
Empezamos a crear nuestro objeto Menu
'''
class Menu:
    '''
    Iniciamos las variables de tamaño y pantalla en la que se encuentra el menú
    '''
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen
    '''
    Esta función inicializa la pantalla para cargar el texto e imágenes que lleva el menú
    '''
    def init_var(self):
        self.bg_surface_menu = pygame.image.load('assets/menu.jpg')
        self.bg_surface_menu = pygame.transform.scale(self.bg_surface_menu, (self.size, self.size))

        self.secondary_font = pygame.font.Font('assets/Diagramm-Regular.ttf', self.size//15)

        self.title_text = self.secondary_font.render('TRIVIA', True, (0, 0, 0), (255, 255, 255))
        self.title_textRect = self.title_text.get_rect()
        self.title_textRect.center = (self.size // 2, self.size // 10)

        self.game1_text = self.secondary_font.render('QUIMICA', True, (0, 0, 0), (255, 255, 255))
        self.game1_textRect = self.game1_text.get_rect()
        self.game1_textRect.center = (self.size // 2, self.size //2+self.size //6)

        self.game2_text = self.secondary_font.render('MATEMATICAS', True, (0, 0, 0), (255, 255, 255))
        self.game2_textRect = self.game2_text.get_rect()
        self.game2_textRect.center = ((self.size // 2), self.size //2+self.size //3)

        self.game3_text = self.secondary_font.render('FISICA', True, (0, 0, 0), (255, 255, 255))
        self.game3_textRect = self.game3_text.get_rect()
        self.game3_textRect.center = (self.size // 2, (self.size // 3))

        self.game4_text = self.secondary_font.render('ESPAÑOL', True, (0, 0, 0), (255, 255, 255))
        self.game4_textRect = self.game4_text.get_rect()
        self.game4_textRect.center = ((self.size // 2, (self.size // 2)))

    '''
    Esta función hace que el texto y las imágenes aparezcan en pantalla
    '''
    def show(self):
        self.screen.blit(self.bg_surface_menu, (0, 0))
        self.screen.blit(self.title_text, self.title_textRect)
        self.screen.blit(self.game1_text, self.game1_textRect)
        self.screen.blit(self.game2_text, self.game2_textRect)
        self.screen.blit(self.game3_text, self.game3_textRect)
        self.screen.blit(self.game4_text, self.game4_textRect)

    '''
    Con esta función, checamos si el mouse se encuentra en alguno de los textos de selección de juego
    y si el mouse fue liberado para así empezar a correr el minijuego seleccionado
    '''
    def menu_mech(self):
        if pygame.mouse.get_pos()[0] > self.size // 2 - self.size // 9 \
                and pygame.mouse.get_pos()[0] < self.size // 2 + self.size // 9 \
                and pygame.mouse.get_pos()[1] > self.size // 2 - self.size // 6 - self.size // 28 \
                and pygame.mouse.get_pos()[1] < self.size // 2 - self.size // 6 + self.size // 28 \
                and get_released():
            return 1
        if pygame.mouse.get_pos()[0] > self.size // 2 - self.size // 7 \
                and pygame.mouse.get_pos()[0] < self.size // 2 + self.size // 7 \
                and pygame.mouse.get_pos()[1] > self.size // 2 - self.size // 28 \
                and pygame.mouse.get_pos()[1] < self.size // 2 + self.size // 28 \
                and get_released():
            return 2
        if pygame.mouse.get_pos()[0] > self.size // 2 - self.size // 7 \
                and pygame.mouse.get_pos()[0] < self.size // 2 + self.size // 7 \
                and pygame.mouse.get_pos()[1] > self.size // 2 + self.size // 6 - self.size // 28 \
                and pygame.mouse.get_pos()[1] < self.size // 2 + self.size // 6 + self.size // 28 \
                and get_released():
            return 3
        if pygame.mouse.get_pos()[0] > self.size // 2 - self.size // 4 \
                and pygame.mouse.get_pos()[0] < self.size // 2 + self.size // 4 \
                and pygame.mouse.get_pos()[1] > self.size // 2 + self.size // 3 - self.size // 28 \
                and pygame.mouse.get_pos()[1] < self.size // 2 + self.size // 3 + self.size // 28 \
                and get_released():
            return 4
        else:
            return 0

