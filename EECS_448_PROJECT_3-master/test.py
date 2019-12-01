from player import Player
from food import Food
from  obstacle import Obstacle
from fire import bulltes
import pygame

worldx = 960
worldy = 720
screen = pygame.display.set_mode((worldx, worldy))
shark = 'image/icon.png'
background = pygame.image.load(shark).convert()
background = pygame.transform.scale(background, (worldx, worldy), screen)
player = Player(background, 0, 0, shark)
food = Food(background, 1, 1)
obstacle = Obstacle(background,2,2)
fire =bulltes(background,0,0)


def test1() -> bool:
    x = player.get_center()
    if x == (65, 35):
        print("Test 1: Testing player.py get_center() function: Passed")
        return True
    else:
        print("Test 1: Testing player.py get_center() function: Not Passed")
        return False


def test2() -> bool:
    x = player.get_distance((0, 0))
    if 94 < x < 95:
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

def test4() -> bool:
    x = food.get_center()
    if x == (1, 1):
        print("Test 4: Testing food.get_center() function: Passed")
        return True
    else:
        print("Test 4: Testing food.get_center() function: Not Passed")
        return False

def test5() -> bool:
    x=food.get_radius()
    if x == 32:
        print("Test 5: Testing food.get_radius() function: Passed")
        return True
    else:
        print("Test 5: Testing food.get_radius() function: Not Passed")
        return False

def test6() -> bool:
    x = obstacle.get_center()
    if x == (18, 18):
        print("Test 6: Testing obstacle.get_center() function: Passed")
        return True
    else:
        print("Test 6: Testing obstacle.get_center() function: Not Passed")
        return False

def test7() -> bool:
    x=obstacle.get_radius()
    if x == 16:
        print("Test 7: Testing obstacle.get_radius() function: Passed")
        return True
    else:
        print("Test 7: Testing obstacle.get_radius() function: Not Passed")
        return False

def test8() -> bool:
    x = fire.get_center()
    if x == (16, 16):
        print("Test 8: Testing fire.get_center() function: Passed")
        return True
    else:
        print("Test 8: Testing fire.get_center() function: Not Passed")
        return False

def test9() -> bool:
    x=obstacle.get_radius()
    if x == 16:
        print("Test 9: Testing fire.get_radius() function: Passed")
        return True
    else:
        print("Test 9: Testing fire.get_radius() function: Not Passed")
        return False

test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()