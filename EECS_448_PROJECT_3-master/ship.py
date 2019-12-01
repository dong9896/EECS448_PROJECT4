import pygame
from fire import bulltes
import random
class Ship:
    firecd =70
    imgpath = 'image/ship.png'
    imgpath2 = 'image/ship2.png'
    def __init__(self, master):
        """
                Constructs ship. Keep creating food in window
                :param: master
                :return: returns none.
                :pre: After player starting game
                """
        self._master=master
        self.image= pygame.image.load(self.imgpath)
        self.x= 200
        self.y= 50
        self.speed = 5
        self.bool =True
        self.t = 0
        self.bullte =[]
    def move(self):
        """
                update the coordinate after starting move ship
                :return: returns none.
                :pre: After player starting move their shark
                :post: update coordinate ship
                """
        if self.x == 0-65 and self.bool == False:
            self.update()
            self.x += self.speed
        elif self.x == self._master.get_width() - 65 and self.bool == True:
            self.update()
            self.x -= self.speed
        elif self.bool == True:
            self.x += self.speed
        elif self.bool == False:
            self.x -= self.speed
    def draw(self):
        """
                Renders the img of shark(For project 3, black circle stands for shark)
                """
        self._master.blit(self.image, (self.x, self.y))

    def update(self):
        """
                Help those check function to know whether ship touch bullets
                :return: returns the center coordinate of that ship.
                :pre: There is ship exist in window
                :post: Help those check function to know whether ship touch bullets
                """
        if self.bool == True:
            self.image = pygame.image.load(self.imgpath2)
            self.bool = False
        elif self.bool == False:
            self.image = pygame.image.load(self.imgpath)
            self.bool = True


    def fire(self):
        """
                Generate coordinate for bullets and the time gap
                :return: returns none.
                :post: Generate coordinate for bullets and the time gap
                """
        cd = random.randint(1, 10)
        self.t += cd
        if self.t >= self.firecd:
            self.t =0
            bx= self.x
            by = self.y+55
            Bullte= bulltes(self._master,bx,by)
            self.bullte.append(Bullte)

    def update_b(self):
        """
              update the list of bullets
              :return: returns none.
              :pre: There is settled bullets in the window
              :post: update the list of bullets
              """
        temp=[]
        for b  in self.bullte:
            b.update()
            if b.on:
                temp.append(b)
        self.bullte = temp

    def draw_b(self):
        """
                Draw food on window
                """
        for b in self.bullte:
            b.draw()

    def clean(self):
        """
                       Clean food on window
                       """
        self.x =200
        self.y =50
        self.bullte =[]

