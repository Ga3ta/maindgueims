import pygame, sys, random
from element import *
from answers_element import *

if __name__=='__main__':
    background_size = int(600)

    pygame.mixer.init()
    pygame.mixer.music.load('assets/DK.OGG')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    pygame.init()
    clock = pygame.time.Clock()

    screen=pygame.display.set_mode((background_size,background_size))
    bg_surface=pygame.image.load('assets/background.jpg')
    bg_surface=pygame.transform.scale(bg_surface,(background_size,background_size))

    element = Element(background_size, screen)
    element_answers1 = AnswersElement(background_size,1,screen)
    element_answers2 = AnswersElement(background_size, 2, screen)
    element_answers3 = AnswersElement(background_size, 3, screen)

    lives=3;

    lifes=pygame.image.load('assets/life.png')
    lifes=pygame.transform.scale(lifes,(40,32))

    secondary_font = pygame.font.Font('assets/Diagramm-Regular.ttf', 28)

    score_text = secondary_font.render('Score', True, (0,0,0), (255,255,255))
    score_textRect = score_text.get_rect()
    score_textRect.center = (background_size//8,background_size//18)

    lifes_text = secondary_font.render('Life', True, (0,0,0), (255,255,255))
    lifes_textRect = score_text.get_rect()
    lifes_textRect.center = ((background_size//30)*26,background_size//18)

    element.init_var()
    element_answers1.init_var()
    element_answers2.init_var()
    element_answers3.init_var()

    while lives>0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if pygame.mouse.get_pos()[0] > 0 and pygame.mouse.get_pos()[0] < 200 and pygame.mouse.get_pressed()[0]:
                print("Ayes")
                lives-=1

        screen.blit(bg_surface,(0,0))


        if lives>2:
            screen.blit(lifes, ((background_size//10)*(9),background_size//10))
        if lives>1:
            screen.blit(lifes, ((background_size//10)*(8),background_size//10))
        if lives>0:
            screen.blit(lifes, ((background_size//10)*(7),background_size//10))

        element.show()
        element_answers1.show()
        element_answers2.show()
        element_answers3.show()

        screen.blit(score_text,score_textRect)
        screen.blit(lifes_text, lifes_textRect)

        pygame.display.update()
        clock.tick(120)