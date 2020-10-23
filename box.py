'''
Importamos el módulo Pygame para tener una interfaz gráfica para nuestros juegos
'''
import pygame

'''
Creamos un objeto Box, que van a ser los recuadros donde irá nuestro texto
'''
class Box:
    '''
    Inicializamos sus valores, su tamaño, la pantalla donde van a estar, 
    si es pequeño o no y si estarán a la derecha, centro o izquierda
    '''
    def __init__(self, size, screen,lil=0,pos=0):
        self.size = size
        self.screen = screen
        self.lil = lil
        self.pos = pos
    '''
    Aquí inicializamos el recuadro y le asignamos una posición y tamaño en base a sus atributos
    '''
    def init_var(self):
        if self.lil>0:
            self.lil_square_size = int(self.size // 4)
            self.lil_square_pos_x = int(self.size//2-self.lil_square_size//2+(self.lil_square_size+self.size//20)*self.pos)
            self.lil_square_pos_y = int((self.size//6)*5-self.lil_square_size//2)
        else:
            self.square_size = int((self.size//100)*45)
            self.square_pos_x = int(self.size // 2 - self.square_size // 2)
            self.square_pos_y = int((self.size // 2 - self.square_size // 2) - (self.size / 10))

        self.color = (255, 255, 255)
    '''
    Aquí hacemos que el cuadro aparezca en la pantalla
    '''
    def show(self):
        if self.lil>0:
            pygame.draw.rect(self.screen, self.color,
                             [self.lil_square_pos_x, self.lil_square_pos_y, self.lil_square_size, self.lil_square_size])
        else:
            pygame.draw.rect(self.screen, self.color,[self.square_pos_x, self.square_pos_y, self.square_size, self.square_size])

