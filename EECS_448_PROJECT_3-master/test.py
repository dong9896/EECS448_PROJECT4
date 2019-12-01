from player import Player
from food import Food
from obstacle import Obstacle
from fire import bulltes
import pygame
from buttom import buttom

worldx = 960
worldy = 720
screen = pygame.display.set_mode((worldx, worldy))
shark = 'image/icon.png'
background = pygame.image.load(shark).convert()
background = pygame.transform.scale(background, (worldx, worldy), screen)
player = Player(background, 0, 0, shark)
food = Food(background, 1, 1)
obstacle = Obstacle(background, 2, 2)
fire = bulltes(background, 0, 0)
button = buttom(1, 1, 1, 1, (255, 255, 255), 'Mode1')


def test1() -> bool:
    """
    Test whether get_center in player.py works
    :return:
    """
    x = player.get_center()
    if x == (65, 35):
        print("Test 1: Testing player.py get_center() function: Passed")
        return True
    else:
        print("Test 1: Testing player.py get_center() function: Not Passed")
        return False


def test2() -> bool:
    """
    Test whether get_distance in player.py works
    :return:
    """
    x = player.get_distance((0, 0))
    if 94 < x < 95:
        print("Test 2: Testing player.py get_distance() function: Passed")
        return True
    else:
        print("Test 2: Testing player.py get_distance() function: Not Passed")
        return False


def test3() -> bool:
    """
    Test whether move in player.py works
    :return:
    """
    x = player.move(1, 1)
    if x == (1, 1):
        print("Test 3: Testing player.py move() function: Passed")
        return True
    else:
        print("Test 3: Testing player.py move() function: Not Passed")
        return False


def test4() -> bool:
    """
    Test whether get_center in food.py works
    :return:
    """
    x = food.get_center()
    if x == (1, 1):
        print("Test 4: Testing food.get_center() function: Passed")
        return True
    else:
        print("Test 4: Testing food.get_center() function: Not Passed")
        return False


def test5() -> bool:
    """
    Test whether get_radius in food.py works
    :return:
    """
    x = food.get_radius()
    if x == 32:
        print("Test 5: Testing food.get_radius() function: Passed")
        return True
    else:
        print("Test 5: Testing food.get_radius() function: Not Passed")
        return False


def test6() -> bool:
    """
    Test whether get_center in obstacle.py works
    :return:
    """
    x = obstacle.get_center()
    if x == (18, 18):
        print("Test 6: Testing obstacle.get_center() function: Passed")
        return True
    else:
        print("Test 6: Testing obstacle.get_center() function: Not Passed")
        return False


def test7() -> bool:
    """
    Test whether get_radius in obstacle.py works
    :return:
    """
    x = obstacle.get_radius()
    if x == 16:
        print("Test 7: Testing obstacle.get_radius() function: Passed")
        return True
    else:
        print("Test 7: Testing obstacle.get_radius() function: Not Passed")
        return False


def test8() -> bool:
    """
    Test whether get_center in fire.py works
    :return:
    """
    x = fire.get_center()
    if x == (16, 16):
        print("Test 8: Testing fire.get_center() function: Passed")
        return True
    else:
        print("Test 8: Testing fire.get_center() function: Not Passed")
        return False


def test9() -> bool:
    """
    Test whether get_radius in fire.py works
    :return:
    """
    x = obstacle.get_radius()
    if x == 16:
        print("Test 9: Testing fire.get_radius() function: Passed")
        return True
    else:
        print("Test 9: Testing fire.get_radius() function: Not Passed")
        return False


def test10() -> bool:
    """
    Test whether ontop in buttom.py works using given location
    :return:
    """
    if button.ontop((1.5, 1.5)):

        print("Test 10: Testing buttom py ontop() function: Passed")
        return True
    else:

        print("Test 10: Testing buttom py ontop() function: Not Passed")
        return False


def test11() -> bool:
    """
    Double Test whether ontop in buttom.py works using given location
    :return:
    """
    if not button.ontop((3, 3)):

        print("Test 11: Double Testing buttom py ontop() function: Passed")
        return True
    else:

        print("Test 10: Double Testing buttom py ontop() function: Not Passed")
        return False




print("-----------------------------Beginning of Testing-----------------------------------")
print("------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------")
test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()
test11()
print("------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------")
print("--------------------------------End of Testing--------------------------------------")