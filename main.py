import pygame, sys
from display import *
from menu import *
from time import sleep

def get_released():
    print('0la')


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
    
    positions=[(display.display_screen_elements.box_answer1.lil_square_pos_x, display.display_screen_elements.box_answer1.lil_square_pos_y),
    (display.display_screen_elements.box_answer2.lil_square_pos_x, display.display_screen_elements.box_answer2.lil_square_pos_y),
    (display.display_screen_elements.box_answer3.lil_square_pos_x, display.display_screen_elements.box_answer3.lil_square_pos_y)]

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
            display.display_physics.screen.blit(display.display_physics.bg_surface_game, (0, 0))
            display.show(3)
            index = display.display_physics.answer_text.correct_index
            if(pygame.mouse.get_pressed()[0]):
                if(pygame.mouse.get_pos()[0] > positions[index][0]
                and pygame.mouse.get_pos()[0] < positions[index][0]+background_size//4
                and pygame.mouse.get_pos()[1] > positions[index][1]
                and pygame.mouse.get_pos()[1] < positions[index][1]+background_size//4):
                    display.display_screen_elements.score+=100
                    display.display_screen_elements.show()
                    display.new_window()
                    print(display.display_screen_elements.score)
                elif(pygame.mouse.get_pos()[0] > positions[index-1][0]
                and pygame.mouse.get_pos()[0] < positions[index-1][0]+background_size//4
                and pygame.mouse.get_pos()[1] > positions[index-1][1]
                and pygame.mouse.get_pos()[1] < positions[index-1][1]+background_size//4 
                or pygame.mouse.get_pos()[0] > positions[index-2][0]
                and pygame.mouse.get_pos()[0] < positions[index-2][0]+background_size//4
                and pygame.mouse.get_pos()[1] > positions[index-2][1]
                and pygame.mouse.get_pos()[1] < positions[index-2][1]+background_size//4):
                    display.display_screen_elements.lives-=1
                    display.display_screen_elements.show()
                    display.new_window()
                if(display.display_screen_elements.lives==0):
                    display.init_var()
                    showing = 0
        elif showing == 2:
            display.display_orthography.screen.blit(display.display_orthography.bg_surface_game, (0, 0))
            display.show(1)
            index = display.display_orthography.answer_text.correct_index
            if(pygame.mouse.get_pressed()[0]):
                if(pygame.mouse.get_pos()[0] > positions[index][0]
                and pygame.mouse.get_pos()[0] < positions[index][0]+background_size//4
                and pygame.mouse.get_pos()[1] > positions[index][1]
                and pygame.mouse.get_pos()[1] < positions[index][1]+background_size//4):
                    display.display_screen_elements.score+=100
                    display.display_screen_elements.show()
                    display.new_window()
                    print(display.display_screen_elements.score)
                elif(pygame.mouse.get_pos()[0] > positions[index-1][0]
                and pygame.mouse.get_pos()[0] < positions[index-1][0]+background_size//4
                and pygame.mouse.get_pos()[1] > positions[index-1][1]
                and pygame.mouse.get_pos()[1] < positions[index-1][1]+background_size//4 
                or pygame.mouse.get_pos()[0] > positions[index-2][0]
                and pygame.mouse.get_pos()[0] < positions[index-2][0]+background_size//4
                and pygame.mouse.get_pos()[1] > positions[index-2][1]
                and pygame.mouse.get_pos()[1] < positions[index-2][1]+background_size//4):
                    display.display_screen_elements.lives-=1
                    display.display_screen_elements.show()
                    display.new_window()
                if(display.display_screen_elements.lives==0):
                    display.init_var()
                    showing = 0
        elif showing == 3:
            display.display_chemestry.screen.blit(display.display_chemestry.bg_surface_game, (0, 0))
            display.show(4)
            index = display.display_chemestry.screen_text.answer_text.correct_index
            if(pygame.mouse.get_pressed()[0]):
                if(pygame.mouse.get_pos()[0] > positions[index][0]
                and pygame.mouse.get_pos()[0] < positions[index][0]+background_size//4
                and pygame.mouse.get_pos()[1] > positions[index][1]
                and pygame.mouse.get_pos()[1] < positions[index][1]+background_size//4):
                    display.display_screen_elements.score+=100
                    display.display_screen_elements.show()
                    display.new_window()
                    print(display.display_screen_elements.score)
                elif(pygame.mouse.get_pos()[0] > positions[index-1][0]
                and pygame.mouse.get_pos()[0] < positions[index-1][0]+background_size//4
                and pygame.mouse.get_pos()[1] > positions[index-1][1]
                and pygame.mouse.get_pos()[1] < positions[index-1][1]+background_size//4 
                or pygame.mouse.get_pos()[0] > positions[index-2][0]
                and pygame.mouse.get_pos()[0] < positions[index-2][0]+background_size//4
                and pygame.mouse.get_pos()[1] > positions[index-2][1]
                and pygame.mouse.get_pos()[1] < positions[index-2][1]+background_size//4):
                    display.display_screen_elements.lives-=1
                    display.display_screen_elements.show()
                    display.new_window()
                if(display.display_screen_elements.lives==0):
                    display.init_var()
                    showing = 0
        elif showing == 4:
            display.display_math.screen.blit(display.display_math.bg_surface_game, (0, 0))
            display.show(2)
            index = display.display_math.answer_text.correct_index
            if(pygame.mouse.get_pressed()[0]):
                if(pygame.mouse.get_pos()[0] > positions[index][0]
                and pygame.mouse.get_pos()[0] < positions[index][0]+background_size//4
                and pygame.mouse.get_pos()[1] > positions[index][1]
                and pygame.mouse.get_pos()[1] < positions[index][1]+background_size//4):
                    display.display_screen_elements.score+=100
                    display.display_screen_elements.show()
                    display.new_window()
                    print(display.display_screen_elements.score)
                elif(pygame.mouse.get_pos()[0] > positions[index-1][0]
                and pygame.mouse.get_pos()[0] < positions[index-1][0]+background_size//4
                and pygame.mouse.get_pos()[1] > positions[index-1][1]
                and pygame.mouse.get_pos()[1] < positions[index-1][1]+background_size//4 
                or pygame.mouse.get_pos()[0] > positions[index-2][0]
                and pygame.mouse.get_pos()[0] < positions[index-2][0]+background_size//4
                and pygame.mouse.get_pos()[1] > positions[index-2][1]
                and pygame.mouse.get_pos()[1] < positions[index-2][1]+background_size//4):
                    display.display_screen_elements.lives-=1
                    display.display_screen_elements.show()
                    display.new_window()
                if(display.display_screen_elements.lives==0):
                    display.init_var()
                    showing = 0
        pygame.display.update()
        clock.tick(120)