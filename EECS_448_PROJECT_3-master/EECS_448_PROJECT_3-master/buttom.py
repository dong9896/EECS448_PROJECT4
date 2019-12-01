"""
buttom module containing the buttom class
"""
import pygame
class buttom():
    def __init__(self,x,y,width,hight,color,text=None):
        """
        Constructs buttom for menu. 
        :param: master
        :param: x location for the buttom
        :param: y location for the buttom
        :param: width width for the buttom
        :param: hight height for the buttom
        :param: color color for the buttom
        :param: text text for the buttom
        """
        self.x=x
        self.y=y
        self.width=width
        self.hight=hight
        self.color=color
        self.text=text
    
    def draw(self,screen):
        """
        draw a buttom in to the main screen
        :param: master
        :param: screen window for the buttom display
        :return: returns none
        """
        pygame.draw.rect(screen,self.color, (self.x,self.y,self.width,self.hight),0)
        #text font, text size
        font = pygame.font.SysFont('times', 40)
        text = font.render(self.text, 1, (0,0,0))
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.hight/2 - text.get_height()/2)))
    
    def ontop(self,position):
        """
        checking if a position is on top of a buttom
        :param: master
        :param: position a set of x and y value
        :return: returns true if a position is on top of buttom, false otherwise 
        """
        if position[0]<self.x+self.width and position[0]>self.x:
            if position[1]>self.y and position[1]<self.y+self.hight:
                return True
        return False