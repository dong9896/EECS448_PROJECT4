"""
player module containing the player class which gets the information needed for
Game to initialize
"""

import pygame
import math
import sys
from obstacle import Obstacle
from obstacle import ObstacleM
from food import Food_move
from food import Food

sharksize = 50
color = (0, 0, 0)


class Player:

    def __init__(self, master, x, y, img_path):
        """
        Constructs player's shark.
        :param: master
        :param: x location for the shark
        :param: y location for the shark
        :return: returns none.
        :pre: After player starting move their shark, the coordinate will be updated
        """
        self._master = master
        self.image = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.lives = 1
        self.score = 0
        self.CumulativeScore = 0;

    def move(self, x, y):
        """
        update the coordinate after player starting move shark
        :param: x location for the shark
        :param: y location for the shark
        :return: returns none.
        :pre: After player starting move their shark
        :post: update coordinate
        """
        if 0 - 65 < self.x + x <= self._master.get_width() - 65:
            self.x += x
        if 0 - 55< self.y + sharksize / 2 + y <= self._master.get_height() - 55:
            self.y += y

    def draw(self):
        """
        Renders the img of shark(For project 3, black circle stands for shark)
        """
        print(self.x,self.y)
        self._master.blit(self.image, (self.x, self.y))

    def get_center(self):
        """
        Help those check function to know whether shark touch a obstacle or food
        :return: returns the center coordinate of that shark.
        :pre: There is shark exist in window
        :post: Help those check function to know whether shark touch a obstacle or food
        """
        return self.x + 65, self.y + 55

    def get_distance(self, xy):
        """
        Find the distance from the center to the shark's edge
        :return: returns the distance
        :pre: There is shark exist in window
        :post: Help those check function to know whether shark touch a obstacle or food
        """
        x, y = xy
        x_distance = self.x + sharksize / 2 + 65
        y_distance = self.y + sharksize / 2 + 55
        return math.sqrt(math.pow(x_distance - x, 2) + (math.pow(y_distance - y, 2)))

    def check_status(self, list):
        """
        Check the status of shark whether crash with obstacle
        :return: returns shark's lives when there is crash(For project 3, sharks will only have one live)
        :pre: There is array of obstacle
        :post: Give the game's status
        """
        for i in list:
            if i.lives > 0:
                temp = self.get_distance(i.get_center())
                if temp <= sharksize / 2 + i.get_radius():
                    self.lives = 0
                    i.lives = 0

    def check_food(self, food_list):
        """
        Check the status of shark whether eat the food
        :return: returns shark's lives when there is crash(For project 3, sharks will only have one live)
        :pre: There is array of food
        :post: Give the game's status
        """
        for j in food_list:
            if j.lives > 0:
                temp = self.get_distance(j.get_center())
                if temp <= sharksize / 2 + j.get_radius():
                    self.lives = 1
                    self.score += 1
                    self.CumulativeScore += 1
                    j.lives = 0

    def shark(self, img_path):
        self.image = pygame.image.load(img_path)
