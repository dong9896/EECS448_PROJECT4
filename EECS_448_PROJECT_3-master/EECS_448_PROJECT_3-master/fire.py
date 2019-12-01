import pygame
radius = 4
class bulltes():

    imgpath3 = 'image/bomb.png'
    def __init__(self,master,x,y):
        self._master= master
        self.x =x
        self.y =y
        self.speed = 10
        self.on = True
        self.image2= pygame.image.load(self.imgpath3)
        self.lives =1
    def  update(self):
        self.y += self.speed
        if self.y >= 800:
            self.on =False

    def draw(self):
        self._master.blit(self.image2, (self.x, self.y))

    def get_center(self):

        return self.x + radius / 2, self.y + radius / 2
    def get_radius(self):

        return radius / 2