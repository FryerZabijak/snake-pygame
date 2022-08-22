from random import randint, random, uniform
from window import width, height, food_color,size
from player import Snake
import pygame

class Food:
    def __init__(self, screen, x, y, player):
        self.screen = screen
        if not x:
            randomX = randint(0, round(width/size))*size-size
            if randomX <= 0: randomX=0
            self.x = randomX
        else:
            self.x = x

        if not y:
            randomY = randint(0, round(height/size))*size-size
            if randomY <= 0: randomY = 0
            self.y = randomY
        else:
            self.y = y

        self.player = player

        print(f"x: {self.x}, y: {self.y}")

    def DrawFood(self):
        pygame.draw.rect(self.screen, food_color,
                         (self.x, self.y, size, size))

    def CheckEat(self):
        snake_head = self.player.trace[0]
        if snake_head["x"]+self.player.speedX == self.x and snake_head["y"]+self.player.speedY == self.y:
            return True