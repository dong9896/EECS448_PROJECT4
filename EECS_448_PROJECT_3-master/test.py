from player import Player
import pygame

worldx = 960
worldy = 720
screen = pygame.display.set_mode((worldx, worldy))
shark = 'image/icon.png'
background = pygame.image.load(shark).convert()
background = pygame.transform.scale(background, (worldx, worldy), screen)
player = Player(background, 0, 0, shark)


def test1() -> bool:
    x = player.get_center()
    if x == (65, 55):
        print("Test 1: Testing player.py get_center() function: Passed")
        return True
    else:
        print("Test 1: Testing player.py get_center() function: Not Passed")
        return False


def test2() -> bool:
    x = player.get_distance((0, 0))
    if 106 < x < 107:
        print("Test 2: Testing player.py get_distance() function: Passed")
        return True
    else:
        print("Test 2: Testing player.py get_distance() function: Not Passed")
        return False


def test3() -> bool:
    x = player.move(1, 1)
    if x == (1, 1):
        print("Test 3: Testing player.py move() function: Passed")
        return True
    else:
        print("Test 3: Testing player.py move() function: Not Passed")
        return False


test1()
test2()
test3()
