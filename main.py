import pygame, sys
from display import *


if __name__=='__main__':
    background_size = int(500)

    pygame.mixer.init()
    pygame.mixer.music.load('assets/DK.OGG')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    pygame.init()
    clock = pygame.time.Clock()

    screen=pygame.display.set_mode((background_size,background_size))
    bg_surface=pygame.image.load('assets/background.jpg')
    bg_surface=pygame.transform.scale(bg_surface,(background_size,background_size))

    display=Display(background_size,screen)
    display.init_var()

    while display.lives>0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if pygame.mouse.get_pos()[0] > 0 and pygame.mouse.get_pos()[0] < 200 and pygame.mouse.get_pressed()[0]:
                print("Ayes")
                display.lives-=1

        screen.blit(bg_surface,(0,0))
        display.show()
        pygame.display.update()
        clock.tick(120)