from random import randint, random, uniform
from window import width, height, food_color,size
import pygame


class Food:
    def __init__(self, screen, x, y):
        self.screen = screen
        if not x:
            self.x = randint(0, round(width/size))*size
        else:
            self.x = x

        if not y:
            self.y = randint(0, round(height/size))*size
        else:
            self.y = y

    def DrawFood(self):

        pygame.draw.rect(self.screen, food_color,
                         (self.x, self.y, size, size))
