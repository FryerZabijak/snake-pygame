import copy
from operator import truediv
from window import width, height, size
import pygame


class Snake:
    def __init__(self, color, snake, screen):
        self.color = color
        self.snake = snake
        self.screen = screen

    def DrawSnake(self):
        for pos in self.snake:
            snake_block_x = pos["x"]
            snake_block_y = pos["y"]
            pygame.draw.rect(self.screen,
                             self.color,
                             (snake_block_x, snake_block_y,
                              size, size)
                             )

    def Move(self, x, y):
        new_positions = []
        newX = self.snake[0]["x"]+x
        if newX<0:
            newX=width
        elif newX>=width:
            newX=0
        newY = self.snake[0]["y"]+y
        if newY<0:
            newY=height
        elif newY>=height:
            newY=0
        new_positions.append({"x": newX, "y": newY})

        for pos in self.snake:
            new_positions.append(pos)

        new_positions.pop()
        self.snake = new_positions
        return new_positions

    def CheckDeath(self):
        # Boundaries
        snake_copy = list.copy(self.snake)
        snake_head = snake_copy[0]

        # Himself
        snake_head = snake_copy.pop(0)
        for pos in snake_copy:
            if snake_head["x"] == pos["x"] and snake_head["y"] == pos["y"]:
                return True
