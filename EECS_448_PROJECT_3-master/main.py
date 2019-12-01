import pygame
import sys
import os
import time
from player import Player
from pygame.locals import  FULLSCREEN
from obstacle import ObstacleM
from buttom import buttom
from food import Food_move
from ship import Ship

white = (255, 255, 255)
blue = (0, 0, 128)
display_width = 1000
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
worldx = 960
worldy = 720
fps = 60
level = 1
limit = 0
pygame.init()
clock = pygame.time.Clock()
# images
back = 'image/backbord.jpg'
shark = 'image/icon.png'
shark1 = 'image/flip.png'
intro_backg = 'image/shark.jpg'
intro_backg2 = 'image/introb.jpeg'
# screen set up
screen = pygame.display.set_mode((worldx, worldy), FULLSCREEN)
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
    buttom3 = buttom(360, 535, 260, 50, (255, 255, 255), 'LeaderBoard')
    buttom0 = buttom(360, 255, 250, 50, (255, 255, 255), 'Hungry Shark')
    buttom4 = buttom(430, 635, 100, 50, (255, 255, 255), 'Start2')
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

                if buttom3.ontop(position):
                    buttom3.color = (255, 255, 0)
                else:
                    buttom3.color = (255, 255, 255)
                if buttom4.ontop(position):
                    buttom4.color = (255, 255, 0)
                else:
                    buttom4.color = (255, 255, 255)
            if event.type == pygame.MOUSEBUTTONDOWN and buttom1.ontop(position):
                intro = False
                game_loop()
            if event.type == pygame.MOUSEBUTTONDOWN and buttom2.ontop(position):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and buttom3.ontop(position):
                highScore()
            if event.type == pygame.MOUSEBUTTONDOWN and buttom4.ontop(position):
                intro = False
                game_loop2()
        rel_x = x % intro_scp.get_rect().height
        screen.blit(intro_scp, (0, rel_x - intro_scp.get_rect().height))
        if rel_x < worldy:
            screen.blit(intro_scp, (0, rel_x))
        x -= 1

        clock.tick(fps)
        buttom0.draw(screen)
        buttom1.draw(screen)
        buttom2.draw(screen)
        buttom3.draw(screen)
        buttom4.draw(screen)
        pygame.display.update()

# set needed information for game_loop


count = 0
fonts = {
    16: pygame.font.SysFont("Times New Roman", 16, True),
    32: pygame.font.SysFont("Times New Roman", 32, True)
}
background = pygame.image.load(back).convert()
background = pygame.transform.scale(background, (worldx, worldy), screen)
player = Player(background, 200, 600, shark)
om = ObstacleM(background)
fm = Food_move(background)
sm = Ship(background)


def text_object(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 70)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = (display_width // 2, display_height // 2)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)


def highScore():
    with open('ScoreRanking.txt', 'r') as f:
        f_content = f.read()
        f_content = str(f_content)

    screen.fill(white)
    message_display('Highest Score: '+ f_content + 'pts')



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
    global limit
    player.score = 0
    om.delete()
    fm.delete()
    limit =0



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
    global player, background, om, fm
    mx = 0
    my = 0
    speed = 5
    global shark,limit


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
                    player.shark(shark1)
                    mx = -speed
                if event.key == ord('w'):
                    my = -speed

                if event.key == ord('d'):
                    player.shark(shark)
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
            with open('ScoreRanking.txt', 'r') as rf:
                HighestScore = rf.read()
                HighestScore = int(HighestScore)
            rf.close()
            with open('ScoreRanking.txt', 'w') as wf:
                if HighestScore > player.CumulativeScore:
                    wf.write(str(HighestScore))
                else:
                    wf.write(str(player.CumulativeScore))
                    print("Congratulations, You Beat the Highest Score !")
            wf.close()
            break
        player.check_food(fm.food_list)

        # Starting update obstacle
        if limit < (10 + level)*100:
            om.number()
            limit += 1
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


def game_loop2():
    global background, player
    mx = 0
    my = 0
    speed = 10
    main= True
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
                    player.shark(shark1)
                    mx = -speed
                if event.key == ord('w'):
                    my = -speed

                if event.key == ord('d'):
                    player.shark(shark)
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
        player.check_status(sm.bullte)
        if player.lives <= 0:
            break
        sm.move()
        sm.draw()
        sm.fire()
        sm.update_b()
        sm.draw_b()
        if player.y <=100 and my <0:
            player.move(mx, 0)
        else:
            player.move(mx, my)
        player.draw()
        pygame.display.flip()
        dt = 1.0 / float(fps)
        clock.tick(fps)
        pygame.display.update()
pre_intro()
game_intro()

pygame.quit()
