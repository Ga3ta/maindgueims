import pygame, sys, random

if __name__=='__main__':
    background_width=int(576)
    background_height=int(576)
    square_size=int(250)

    a = open("assets/Tp.txt", "r")
    elements=[]
    for line in a:
        e=line.split(",")
        elements.append({"name": e[0], "symbol": e[1], "number": int(e[2])})

    element=elements[38]["symbol"]
    number=elements[38]["number"]
    name=elements[38]["name"]
    answer1='H'
    answer2='Cl'
    answer3='Br'

    lives=3;

    square_pos_x=int(background_width//2-square_size//2)
    square_pos_y=int((background_height//2-square_size//2)-(background_height/10))

    lil_square_size=int(square_size//2)

    lil_square_pos_x=int(background_width//2-square_size//2//2)
    lil_square_pos_y=int((background_height//2-square_size//2)+((background_height/14)*6))

    color=(255,255,255)

    pygame.init()
    clock = pygame.time.Clock()

    screen=pygame.display.set_mode((background_width,background_height))
    bg_surface=pygame.image.load('assets/background.jpg')
    bg_surface=pygame.transform.scale(bg_surface,(background_width,background_height))

    lifes=pygame.image.load('assets/life.png')
    lifes=pygame.transform.scale(lifes,(40,32))


    element_symbol_font = pygame.font.Font('assets/Diagramm-Regular.ttf', 150)

    element_symbol_text = element_symbol_font.render(str(element), True, (0,0,0), (255,255,255))
    element_symbol_textRect = element_symbol_text.get_rect()
    element_symbol_textRect.center = (background_width//2,background_height//2-(background_height//14))

    element_number_font = pygame.font.Font('assets/Diagramm-Regular.ttf', 50)

    element_number_text = element_number_font.render(str(number), True, (0,0,0), (255,255,255))
    element_number_textRect = element_number_text.get_rect()
    element_number_textRect.center = (background_width//2-(background_height//6),background_height//2-(background_height//4))

    element_text_font = pygame.font.Font('assets/Diagramm-Regular.ttf',40)

    element_name_text = element_text_font.render(str(name), True, (0,0,0), (255,255,255))
    element_name_textRect = element_name_text.get_rect()
    element_name_textRect.center = (background_width//2,background_height//2+(background_height//14))

    element_answers_font = pygame.font.Font('assets/Diagramm-Regular.ttf', 30)

    element_answer1_text = element_answers_font.render(str(answer1), True, (0,0,0), (255,255,255))
    element_answer1_textRect = element_name_text.get_rect()
    element_answer1_textRect.center = (background_width//2-100,background_height//2+(background_height//3))

    element_answer2_text = element_answers_font.render(str(answer2), True, (0,0,0), (255,255,255))
    element_answer2_textRect = element_name_text.get_rect()
    element_answer2_textRect.center = (background_width//2+90,background_height//2+(background_height//3))

    element_answer3_text = element_answers_font.render(str(answer3), True, (0,0,0), (255,255,255))
    element_answer3_textRect = element_name_text.get_rect()
    element_answer3_textRect.center = (background_width//2+275,background_height//2+(background_height//3))

    secondary_font = pygame.font.Font('assets/Diagramm-Regular.ttf', 28)

    score_text = secondary_font.render('Score', True, (0,0,0), (255,255,255))
    score_textRect = score_text.get_rect()
    score_textRect.center = (background_width//8,background_width//18)

    lifes_text = secondary_font.render('Life', True, (0,0,0), (255,255,255))
    lifes_textRect = score_text.get_rect()
    lifes_textRect.center = ((background_width//30)*26,background_width//18)

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
            screen.blit(lifes, ((background_width//10)*(9),background_width//10))
        if lives>1:
            screen.blit(lifes, ((background_width//10)*(8),background_width//10))
        if lives>0:
            screen.blit(lifes, ((background_width//10)*(7),background_width//10))

        pygame.draw.rect(screen,color, [square_pos_x,square_pos_y,square_size, square_size])
        pygame.draw.rect(screen,color, [lil_square_pos_x-background_width//3,lil_square_pos_y,lil_square_size, lil_square_size])
        pygame.draw.rect(screen,color, [lil_square_pos_x,lil_square_pos_y,lil_square_size, lil_square_size])
        pygame.draw.rect(screen,color, [lil_square_pos_x+background_width//3,lil_square_pos_y,lil_square_size, lil_square_size])

        screen.blit(score_text,score_textRect)
        screen.blit(lifes_text, lifes_textRect)
        screen.blit(element_symbol_text, element_symbol_textRect)
        screen.blit(element_number_text, element_number_textRect)
        screen.blit(element_name_text,element_name_textRect)
        screen.blit(element_answer1_text,element_answer1_textRect)
        screen.blit(element_answer2_text, element_answer2_textRect)
        screen.blit(element_answer3_text, element_answer3_textRect)
        pygame.display.update()
        clock.tick(120)

