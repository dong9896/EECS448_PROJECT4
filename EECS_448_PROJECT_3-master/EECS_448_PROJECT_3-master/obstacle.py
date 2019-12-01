"""
obstacle module containing the obstacle class and
the obstacle movement class which gets the information needed for
Game to initialize
"""

import pygame
import random

color = (255, 0, 0)
radius = 32
speed = 1
cd = 100


class Obstacle:

    def __init__(self, master, x, y):
        """
        Constructs obstacle. Keep creating obstacles in window
        :param: master
        :param: x location for the random obstacles
        :param: y location for the random obstacles
        :return: returns none.
        :pre: After player starting move their shark
        """
        img_path = 'image/trash.png'
        self._master = master
        temp = random.randint(1, 5)
        if temp == 1:
            img_path = 'image/trash.png'
        elif temp == 2:
            img_path = 'image/plastic.png'
        elif temp == 3:
            img_path = 'image/plastic-bottle.png'
        elif temp == 4:
            img_path = 'image/waste.png'
        elif temp == 5:
            img_path = 'image/plastic-bottle2.png'
        self.image = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.lives = 1

    def update(self):
        """
        Give obstacle a random moving direction
        :return: returns none.
        :pre: after construct generate a location for obstacle
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
        Draw the shape of obstacle(for project 3, red circle stands for obstacle)
        :return: returns none.
        :pre: after construct generate a location for obstacle
        :post: draw shape on that location
        """
        self._master.blit(self.image, (self.x, self.y))

    def get_center(self):
        """
        Help those check function to know whether shark touch a obstacle
        :return: returns the center coordinate of that obstacle.
        :pre: There is obstacle in the list
        :post: Help those check function to know whether shark touch a obstacle
        """
        return self.x + radius / 2, self.y + radius / 2

    def get_radius(self):
        """
        Help those check function to know whether shark touch a obstacle
        :return: returns the radius of obstacle
        :pre: There is obstacle in the list
        :post: Help those check function to know whether shark touch a obstacle
        """
        return radius / 2


class ObstacleM:

    def __init__(self, master):
        """
        Constructs the property of obstacles
        :param: master
        :return: returns none.
        :pre: list of obstacles is needed
        """
        self._master = master
        self.list = []
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
            z = Obstacle(self._master, x_scale, y_scale)
            self.list.append(z)
            self.num += 1

    def update(self):
        """
        update the list of obstacle
        :return: returns none.
        :pre: There is settled obstacle in the window
        :post: update the list of obstacle
        """
        temp = []
        for obstacle in self.list:
            obstacle.update()
            temp.append(obstacle)
            self.list = temp

    def draw(self):
        """
        Draw obstacle on window
        """
        for obstacle in self.list:
            obstacle.draw()

    def delete(self):
        self.list = []

