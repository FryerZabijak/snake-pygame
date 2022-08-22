import copy
from operator import truediv
from window import width, height, size
import pygame


class Snake:
    def __init__(self, speedX, speedY, color, trace, screen):
        self.speedX = speedX
        self.speedY = speedY
        self.color = color
        self.trace = trace
        self.screen = screen

    # Vykreslení hada
    def DrawSnake(self):
        for pos in self.trace:
            snake_block_x = pos["x"]
            snake_block_y = pos["y"]
            pygame.draw.rect(self.screen,
                             self.color,
                             (snake_block_x, snake_block_y,
                              size, size)
                             )

    # Pohyb hada
    def Move(self):
        new_positions = []
        newX = self.trace[0]["x"]+self.speedX
        if newX<0:
            newX=width
        elif newX>=width:
            newX=0
        newY = self.trace[0]["y"]+self.speedY
        if newY<0:
            newY=height
        elif newY>=height:
            newY=0
        new_positions.append({"x": newX, "y": newY})

        for pos in self.trace:
            new_positions.append(pos)

        new_positions.pop()
        self.trace = new_positions
        return new_positions

    # Zkontroluje zda-li had zemřel
    def CheckDeath(self):
        # Boundaries
        snake_copy = list.copy(self.trace)
        snake_head = snake_copy[0]

        # Himself
        snake_head = snake_copy.pop(0)
        for pos in snake_copy:
            if snake_head["x"] == pos["x"] and snake_head["y"] == pos["y"]:
                return True
