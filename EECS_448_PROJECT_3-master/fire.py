import pygame
radius = 32
class bulltes():

    imgpath3 = 'image/bomb.png'
    def __init__(self,master,x,y):
        """
       Constructs bulltes for ship. Keep creating bulltes in window
       :param: master
       :param: x location for the master
       :param: y location for the master
       :return: returns none.
       :pre: After player starting game
       """
        self._master= master
        self.x =x
        self.y =y
        self.speed = 10
        self.on = True
        self.image2= pygame.image.load(self.imgpath3)
        self.lives =1
    def  update(self):
        """
        Give bullets a moving direction
        :return: returns none.
        :pre: after construct generate a location for bullets
        """
        self.y += self.speed
        if self.y >= 800:
            self.on =False

    def draw(self):
        """
              Draw the shape of bullets
              :return: returns none.
              :pre: after construct generate a location for bullets
              :post: draw shape on that location
              """
        self._master.blit(self.image2, (self.x, self.y))

    def get_center(self):
        """
             Help those check function to know whether shark touch bullets
             :return: returns the center coordinate of that bullets.
             :pre: There is bullets in the list
             :post: Help those check function to know whether shark touch bullets
             """

        return self.x + radius / 2, self.y + radius / 2
    def get_radius(self):
        """
              Help those check function to know whether shark touch bullets
              :return: returns the center coordinate of that bullets.
              :pre: There is bullets in the list
              :post: Help those check function to know whether shark touch bullets
              """
        return radius / 2