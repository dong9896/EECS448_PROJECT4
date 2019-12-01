import pygame
import sys
import os
import time
from player import Player
from pygame.locals import FULLSCREEN
from obstacle import ObstacleM
from buttom import buttom
from food import Food_move
from ship import Ship

white = (255, 255, 255)
blue = (0, 0, 128)
display_width = 1000
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))
worldx = 960
worldy = 720
fps = 60
level = 1
limit = 0

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
# images
back = 'image/backbord.jpg'
shark = 'image/icon.png'
shark1 = 'image/flip.png'
intro_backg = 'image/shark.jpg'
intro_backg2 = 'image/introb.jpeg'
# sounds/music
main_sound = 'sounds/10 Arpanauts.mp3'
game_mode2 = 'sounds/01 A Night Of Dizzy Spells.mp3'
game_mode1 = 'sounds/03 Chibi Ninja.mp3'
selection_m = pygame.mixer.Sound("sounds/Pop.wav")
selection_m2 = pygame.mixer.Sound("sounds/da.wav")
ding = pygame.mixer.Sound("sounds/ding.wav")
end = pygame.mixer.Sound("sounds/end.wav")
win = pygame.mixer.Sound("sounds/win.wav")
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

    backg = pygame.Surface((worldx, worldy))
    font = pygame.font.SysFont('Arial', 20, True, True)

    text = font.render('Shake Shark Present ©', True, (255, 255, 255))

    i = 1
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        intro.set_alpha(i)

        screen.blit(backg, backg.get_rect())
        screen.blit(intro, (100, 100))
        screen.blit(text, (390, 550))
        pygame.time.delay(16)

        i += 2
        if(i > 225):
            run = False
        pygame.display.update()


# game intro

def game_intro():
    intro = True
    buttom1 = buttom(410, 355, 150, 50, (255, 255, 255), 'Mode1')
    buttom2 = buttom(430, 615, 100, 50, (255, 255, 255), 'Quit')
    buttom3 = buttom(370, 510, 220, 50, (255, 255, 255), 'Score Board')
    buttom0 = buttom(360, 200, 250, 50, (255, 255, 255), 'Hungry Shark')
    buttom4 = buttom(410, 435, 150, 50, (255, 255, 255), 'Mode2')
    intro_scp = pygame.image.load(intro_backg2).convert()
    x = 0
    pygame.mixer.music.load(main_sound)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    selection_m.set_volume(0.8)
    pygame.time.delay(20)
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
                pygame.mixer.Sound.play(selection_m)
                pygame.mixer.music.stop()
                game_loop()
                pygame.mixer.music.play(-1)
            if event.type == pygame.MOUSEBUTTONDOWN and buttom2.ontop(position):
                pygame.mixer.Sound.play(selection_m)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and buttom3.ontop(position):
                pygame.mixer.Sound.play(selection_m)
                highScore()
            if event.type == pygame.MOUSEBUTTONDOWN and buttom4.ontop(position):
                pygame.mixer.Sound.play(selection_m)
                pygame.mixer.music.stop()
                game_loop2()
                pygame.mixer.music.play(-1)
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
boss = False
check = False


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
    message_display('Highest Score: ' + f_content + 'pts')


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
    limit = 0


def draw():
    """
    Draw the needed text on the window
    :return: returns none
    :pre: player hit start button on the main menu screen
    :post: Display necessary information
    """
    score_display = fonts[16].render(
        "Scores: " + str(max([player.score, 0])), True, (0, 0, 0))
    screen.blit(score_display, (10, 25))
    level_display = fonts[16].render(
        "Level: " + str(get_level()), True, (0, 0, 0))
    screen.blit(level_display, (10, 10))
    next_level = fonts[16].render(
        "Get into Next Level Needs to Score " +
        str(5 * get_level() - max([player.score, 0])) + " More Points",
        True, (0, 0, 0))
    screen.blit(next_level, (10, 40))
    pygame.display.flip()


# game loop


def game_loop():
    global player, background, om, fm
    mx = 0
    my = 0
    speed = 3
    global shark, limit, level
    condition = False
    pygame.mixer.music.load(game_mode1)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    speed = 8

    global shark,limit,level,boss
    condition=False

    main = True
    pygame.time.delay(20)
    while main:

        background = pygame.image.load(back).convert()
        background = pygame.transform.scale(
            background, (worldx, worldy), screen)

        background = pygame.transform.scale(background, (worldx, worldy), screen)
        if level%5 == 0:
            boss = True
            level +=1
            game_loop2()
        if check ==True:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                main = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.mixer.music.pause()
                    pygame.mixer.Sound.play(ding)
                    if SecM():
                        condition = True
                        main = False
                        break
                    else:
                        pygame.mixer.music.unpause()
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
            player = Player(background, 200, 600, shark)
            reset_game()
            level = 1
            limit = 0
            pygame.mixer.music.stop()
            gameOver()
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
    if condition:
        player = Player(background, 200, 600, shark)
        reset_game()
        level = 1
        limit = 0


def SecM():
    main = True
    screen.fill([255, 255, 255])
    buttom1 = buttom(400, 375, 160, 50, (255, 255, 255), 'Continue')
    buttom2 = buttom(430, 455, 100, 50, (255, 255, 255), 'Quit')
    buttom3 = buttom(350, 535, 260, 50, (255, 255, 255), 'Return to Menu')
    buttom0 = buttom(360, 255, 250, 50, (255, 255, 255), 'Paused')
    pygame.time.delay(20)
    while main:
        for event in pygame.event.get():
            position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                main = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
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

            if event.type == pygame.MOUSEBUTTONDOWN and buttom1.ontop(position):
                pygame.mixer.Sound.play(selection_m2)
                main = False

            if event.type == pygame.MOUSEBUTTONDOWN and buttom2.ontop(position):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and buttom3.ontop(position):
                pygame.mixer.Sound.play(selection_m2)
                pygame.mixer.music.load(main_sound)
                main = False
                return True
        buttom0.draw(screen)
        buttom1.draw(screen)
        buttom2.draw(screen)
        buttom3.draw(screen)
        pygame.display.flip()

    return False


def gameOver():
    main = True
    screen.fill([255, 255, 255])
    #buttom1 = buttom(430, 375, 160, 50, (255, 255, 255), 'Continue')
    buttom2 = buttom(430, 455, 100, 50, (255, 255, 255), 'Quit')
    buttom3 = buttom(350, 535, 260, 50, (255, 255, 255), 'Return to Menu')
    buttom0 = buttom(360, 255, 250, 50, (255, 255, 255), 'Game Over !')
    pygame.mixer.Sound.play(end)
    pygame.time.delay(20)
    while main:
        for event in pygame.event.get():
            position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                main = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEMOTION:

                if buttom2.ontop(position):
                    buttom2.color = (255, 255, 0)
                else:
                    buttom2.color = (255, 255, 255)
                if buttom3.ontop(position):
                    buttom3.color = (255, 255, 0)
                else:
                    buttom3.color = (255, 255, 255)
            if event.type == pygame.MOUSEBUTTONDOWN and buttom2.ontop(position):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and buttom3.ontop(position):
                pygame.mixer.Sound.play(selection_m2)
                pygame.mixer.music.load(main_sound)
                main = False

        buttom0.draw(screen)
        buttom2.draw(screen)
        buttom3.draw(screen)
        pygame.display.flip()


def game_loop2():
    global background, player,boss,check
    mx = 0
    my = 0
    pygame.mixer.music.load(game_mode2)
    pygame.mixer.music.play(-1)
    pygame.time.delay(20)
    speed = 8
    main= True
    times= 0
    timex =60
    while main:
        background = pygame.image.load(back).convert()
        background = pygame.transform.scale(
            background, (worldx, worldy), screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                main = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.mixer.music.pause()
                    pygame.mixer.Sound.play(ding)
                    if SecM():
                        # pygame.mixer.music.stop()
                        condition = True
                        main = False
                        break
                    else:
                        pygame.mixer.music.unpause()

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
           if boss == True:
               player = Player(background, 200, 600, shark)
               sm.clean()
               pygame.mixer.music.stop()
               gameOver()
               check = True
               break
           elif boss == False:
               player = Player(background, 200, 600, shark)
               sm.clean()
               pygame.mixer.music.stop()
               gameOver()
               break
        elif timex == 0:
           if boss == True:
               boss = False
               check = False
               sm.clean()
               pygame.mixer.music.stop()
               break
           elif boss == False:
               player = Player(background, 200, 600, shark)
               sm.clean()
               pygame.mixer.music.stop()
               success()
               break
        sm.move()
        sm.draw()
        sm.fire()
        sm.update_b()
        sm.draw_b()
        if player.y <= 100 and my < 0:
            player.move(mx, 0)
        else:
            player.move(mx, my)
        player.draw()
        pygame.display.flip()
        dt = 1.0 / float(fps)
        clock.tick(fps)
        pygame.display.update()
# pre_intro()

        clock.tick(60)
        times +=1
        if times == 30:
            timex -= 1
            times = 0
        time_display = fonts[32].render(str(timex), True, (0, 0, 0))
        screen.blit(time_display, (450, 25))

        pygame.display.update()


def success():
    main = True
    screen.fill([255, 255, 255])
    # buttom1 = buttom(430, 375, 160, 50, (255, 255, 255), 'Continue')
    buttom2 = buttom(430, 455, 100, 50, (255, 255, 255), 'Quit')
    buttom3 = buttom(350, 535, 260, 50, (255, 255, 255), 'Return to Menu')
    buttom0 = buttom(360, 255, 250, 50, (255, 255, 255), 'Victory!')
    pygame.mixer.Sound.play(win)
    pygame.time.delay(20)
    while main:
        for event in pygame.event.get():
            position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                main = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEMOTION:

                if buttom2.ontop(position):
                    buttom2.color = (255, 255, 0)
                else:
                    buttom2.color = (255, 255, 255)
                if buttom3.ontop(position):
                    buttom3.color = (255, 255, 0)
                else:
                    buttom3.color = (255, 255, 255)
            if event.type == pygame.MOUSEBUTTONDOWN and buttom2.ontop(position):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and buttom3.ontop(position):
                pygame.mixer.Sound.play(selection_m2)
                pygame.time.delay(20)
                pygame.mixer.music.load(main_sound)
                main = False

        buttom0.draw(screen)

        buttom2.draw(screen)
        buttom3.draw(screen)
        pygame.display.flip()

#main function call

pre_intro()

game_intro()

pygame.quit()
