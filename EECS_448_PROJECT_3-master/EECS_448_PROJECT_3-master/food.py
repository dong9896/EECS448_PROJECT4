"""
food module containing the food class and
the food movement class which gets the information needed for
Game to initialize
"""

import pygame
import random
import math

color = (255, 0, 0)
radius = 24
speed = 1
cd = 100
GREEN = (0, 255, 0)
size = 3


class Food:

    def __init__(self, master, x, y):
        """
        Constructs food for shark. Keep creating food in window
        :param: master
        :param: x location for the random food
        :param: y location for the random food
        :return: returns none.
        :pre: After player starting move their shark
        """
        self._master = master
        img_path = 'image/prawn.png'
        self.image = pygame.image.load(img_path)
        temp = random.randint(1, 5)
        if temp == 1:
            img_path = 'image/crustacean.png'
        elif temp == 2:
            img_path = 'image/fish.png'
        self.image = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.lives = 1

    def update(self):
        """
        Give food a random moving direction
        :return: returns none.
        :pre: after construct generate a location for food
        """
        temp = random.randint(0, 3)
        if temp == 0:
            self.y += speed
            self.x += speed
        if temp == 1:
            self.y += speed
            self.x -= speed
        if temp == 2:
            self.y -= speed
            self.x -= speed
        if temp == 3:
            self.y -= speed
            self.x += speed

    def draw(self):
        """
        Draw the shape of food(for project 3, green triangle stands for food)
        :return: returns none.
        :pre: after construct generate a location for food
        :post: draw shape on that location
        """
        #x = self.x
        #y = self.y
        #point1 = [(x - math.sqrt(3) * size), (y - size)]
        #point2 = [(x + math.sqrt(3) * size), (y - size)]
        #point3 = [x, (y + 2 * size)]
        #pygame.draw.polygon(self._master, GREEN, [point1, point2, point3], size)
        self._master.blit(self.image, (self.x, self.y))

    def get_center(self):
        """
        Help those check function to know whether shark touch food
        :return: returns the center coordinate of that food.
        :pre: There is food in the list
        :post: Help those check function to know whether shark touch food
        """
        return self.x, self.y

    def get_radius(self):
        """
        Help those check function to know whether shark touch food
        :return: returns the center coordinate of that food.
        :pre: There is food in the list
        :post: Help those check function to know whether shark touch food
        """
        return size


class Food_move:
    def __init__(self, master):
        """
        Constructs the property of food
        :param: master
        :return: returns none.
        :pre: list of food is needed
        """
        self._master = master
        self.food_list = []
        self.time = 0
        self.num = 0
        self.lives = 1

    def number(self):
        """
        Generate coordinate for obstacle and the time gap
        :return: returns none.
        :post: Generate coordinate for obstacle and the time gap
        """
        self.time += 1
        if self.time % cd == 0:
            x_scale = random.randint(0, self._master.get_width() - radius * 2)
            y_scale = random.randint(0, self._master.get_width() - radius * 2)
            z = Food(self._master, x_scale, y_scale)
            self.food_list.append(z)
            self.num += 1

    def update(self):
        """
        update the list of food
        :return: returns none.
        :pre: There is settled food in the window
        :post: update the list of food
        """
        temp = []
        for food in self.food_list:
            food.update()
            if food.lives>0:
                temp.append(food)
            self.food_list = temp

    def draw(self):
        """
        Draw food on window
        """
        for food in self.food_list:
            food.draw()

    def delete(self):
        self.food_list = []