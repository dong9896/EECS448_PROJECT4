import pygame
import sys
import os
from player import Player
from obstacle import ObstacleM
from buttom import buttom
from food import Food_move

worldx = 960
worldy = 720
fps = 60
level = 1
pygame.init()
clock = pygame.time.Clock()
# images
back = 'image/backbord.jpg'
shark = 'image/icon.png'
intro_backg = 'image/shark.jpg'
intro_backg2 = 'image/introb.jpeg'
# screen set up
screen = pygame.display.set_mode((worldx, worldy))
# background set up


# title
pygame.display.set_caption("Shark")
icon = pygame.image.load('fishincon.png')
pygame.display.set_icon(icon)


# loading
def pre_intro():
    intro = pygame.image.load(intro_backg).convert()
    
    backg=pygame.Surface((worldx,worldy))
    font=pygame.font.SysFont('Arial',20,True,True)
    
    text=font.render('Shake Shark Present ©',True,(255,255,255))
   
    
    i=1
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
       
        intro.set_alpha(i)
        
        screen.blit(backg,backg.get_rect())
        screen.blit(intro, (100,100))
        screen.blit(text,(390,550))
        pygame.time.delay(16)
        
        i+=1
        if(i==225):
            run=False
        pygame.display.update()
  
    
   

# game intro

def game_intro():
    intro = True
    buttom1 = buttom(430, 375, 100, 50, (255, 255, 255), 'Start')
    buttom2 = buttom(430, 455, 100, 50, (255, 255, 255), 'Quit')
    buttom0 = buttom(360, 255, 250, 50, (255, 255, 255), 'Hungary Shark')
    intro_scp = pygame.image.load(intro_backg2).convert()
    x = 0
    while intro:

        for event in pygame.event.get():
            position = pygame.mouse.get_pos()
            # click=pygame.mouse.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                if buttom1.ontop(position):
                    buttom1.color = (255, 255, 0)
                else:
                    buttom1.color = (255, 255, 255)

                if buttom2.ontop(position):
                    buttom2.color = (255, 255, 0)
                else:
                    buttom2.color = (255, 255, 255)
            if event.type == pygame.MOUSEBUTTONDOWN and buttom1.ontop(position):
                intro = False
            if event.type == pygame.MOUSEBUTTONDOWN and buttom2.ontop(position):
                pygame.quit()
                sys.exit()

        rel_x = x % intro_scp.get_rect().height
        screen.blit(intro_scp, (0, rel_x - intro_scp.get_rect().height))
        if rel_x < worldy:
            screen.blit(intro_scp, (0, rel_x))
        x -= 1

        clock.tick(fps)
        buttom0.draw(screen)
        buttom1.draw(screen)
        buttom2.draw(screen)
        pygame.display.update()

# set needed information for game_loop


count = 0
fonts = {
    16: pygame.font.SysFont("Times New Roman", 16, True),
    32: pygame.font.SysFont("Times New Roman", 32, True)
}
background = pygame.image.load(back).convert()
background = pygame.transform.scale(background, (worldx, worldy), screen)
player = Player(background, 200, 200, shark)


def get_level():
    """
    Get into next level(For project 3, next level requires more score to pass.)
    :return: returns updated level number.
    :pre: player successfully get needed scores
    """
    global level
    if player.score == level * 5:
        level += 1
        reset_game()
    return level


def reset_game():
    """
    Reset score,get into next level(For project 3, only score will be reset in reset function.)
    :return: returns none
    :pre: player successfully get into next level
    """
    player.score = 0


def draw():
    """
    Draw the needed text on the window
    :return: returns none
    :pre: player hit start button on the main menu screen
    :post: Display necessary information
    """
    score_display = fonts[16].render("Scores: " + str(max([player.score, 0])), True, (0, 0, 0))
    screen.blit(score_display, (10, 25))
    level_display = fonts[16].render("Level: " + str(get_level()), True, (0, 0, 0))
    screen.blit(level_display, (10, 10))
    next_level = fonts[16].render(
        "Get into Next Level Needs to Score " + str(5 * get_level() - max([player.score, 0])) + " More Points",
        True, (0, 0, 0))
    screen.blit(next_level, (10, 40))
    pygame.display.flip()


# game loop


def game_loop():
    global player, background
    om = ObstacleM(background)
    fm = Food_move(background)
    mx = 0
    my = 0
    speed = 3

    main = True
    while main:

        background = pygame.image.load(back).convert()
        background = pygame.transform.scale(background, (worldx, worldy), screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                main = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    main = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('a'):
                    mx = -speed
                if event.key == ord('w'):
                    my = -speed
                if event.key == ord('d'):
                    mx = speed
                if event.key == ord('s'):
                    my = speed
            if event.type == pygame.KEYUP:
                if event.key == ord('a'):
                    if mx == -speed:
                        my = 0
                if event.key == ord('w'):
                    if my == -speed:
                        mx = 0
                if event.key == ord('d'):
                    if mx == speed:
                        my = 0
                if event.key == ord('s'):
                    if my == speed:
                        mx = 0
        player.check_status(om.list)
        if player.lives <= 0:
            print("You lose your shark!")
            break
        player.check_food(fm.food_list)

        # Starting update obstacle
        om.number()
        om.update()
        om.draw()

        # Starting update food
        fm.number()
        fm.update()
        fm.draw()

        # react as player moving shark
        player.move(mx, my)
        player.draw()
        draw()
        dt = 1.0 / float(fps)
        clock.tick(fps)
        pygame.display.update()


pre_intro()
game_intro()
game_loop()
pygame.quit()
