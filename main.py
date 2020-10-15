import pygame, sys
from display import *
from menu import *
from display_physics_problems import *
from display_math_problems import *
from display_orthography_problems import *


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
    bg_surface_menu=pygame.image.load('assets/menu.jpg')
    bg_surface_menu=pygame.transform.scale(bg_surface_menu,(background_size,background_size))
    bg_surface_game1=pygame.image.load('assets/background.jpg')
    bg_surface_game1=pygame.transform.scale(bg_surface_game1,(background_size,background_size))
    bg_surface_game2=pygame.image.load('assets/background2.jpg')
    bg_surface_game2=pygame.transform.scale(bg_surface_game2,(background_size,background_size))
    bg_surface_game3=pygame.image.load('assets/background3.jpg')
    bg_surface_game3=pygame.transform.scale(bg_surface_game3,(background_size,background_size))
    bg_surface_game4=pygame.image.load('assets/background4.jpg')
    bg_surface_game4=pygame.transform.scale(bg_surface_game4,(background_size,background_size))

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
            screen.blit(bg_surface_menu, (0, 0))
            menu.show()
            if pygame.mouse.get_pos()[0] > background_size//2-background_size//9\
                    and pygame.mouse.get_pos()[0] < background_size//2+background_size//9\
                    and pygame.mouse.get_pos()[1] > background_size//2-background_size//6-background_size//28\
                    and pygame.mouse.get_pos()[1] < background_size//2-background_size//6+background_size//28\
                    and pygame.mouse.get_pressed()[0]:
                showing = 1
            if pygame.mouse.get_pos()[0] > background_size//2-background_size//7\
                    and pygame.mouse.get_pos()[0] < background_size//2+background_size//7\
                    and pygame.mouse.get_pos()[1] > background_size//2-background_size//28\
                    and pygame.mouse.get_pos()[1] < background_size//2+background_size//28\
                    and pygame.mouse.get_pressed()[0]:
                showing = 2
            if pygame.mouse.get_pos()[0] > background_size // 2 - background_size // 7 \
                    and pygame.mouse.get_pos()[0] < background_size // 2 + background_size // 7 \
                    and pygame.mouse.get_pos()[1] > background_size // 2 + background_size // 6 - background_size // 28 \
                    and pygame.mouse.get_pos()[1] < background_size // 2 + background_size // 6 + background_size // 28\
                    and pygame.mouse.get_pressed()[0]:
                showing = 3
            if pygame.mouse.get_pos()[0] > background_size // 2 - background_size // 4 \
                    and pygame.mouse.get_pos()[0] < background_size // 2 + background_size // 4 \
                    and pygame.mouse.get_pos()[1] > background_size // 2 + background_size // 3 - background_size // 28 \
                    and pygame.mouse.get_pos()[1] < background_size // 2 + background_size // 3 + background_size // 28\
                    and pygame.mouse.get_pressed()[0]:
                showing = 4
        elif showing==1:
            screen.blit(bg_surface_game1, (0, 0))
            display.show(3)
        elif showing == 2:
            screen.blit(bg_surface_game2, (0, 0))
            display.show(1)
        elif showing == 3:
            screen.blit(bg_surface_game3, (0, 0))
            display.show(4)
        elif showing == 4:
            screen.blit(bg_surface_game4, (0, 0))
            display.show(2)
        print(showing)
        pygame.display.update()
        clock.tick(120)