import pygame, sys
from display import *
from menu import *

if __name__=='__main__':
    background_size = int(500)
    showing=0
    pygame.mixer.init()
    pygame.mixer.music.load('assets/DK.OGG')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    pygame.init()
    clock = pygame.time.Clock()

    screen=pygame.display.set_mode((background_size,background_size))

    menu=Menu(background_size,screen)
    menu.init_var()
    display=Display(background_size,screen)
    display.init_var()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


        if showing==0:
            menu.show()
            showing=menu.menu_mech()
        elif showing==1:
            display.show(3)
        elif showing == 2:
            display.show(1)
        elif showing == 3:
            display.show(4)
        elif showing == 4:
            display.show(2)
        print(showing)
        pygame.display.update()
        clock.tick(120)