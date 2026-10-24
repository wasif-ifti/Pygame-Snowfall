# drawable.py
# Name: Wasif Islam
# Description: Drawable objects for the snowfall animation

import pygame
from abc import ABC, abstractmethod


class Drawable(ABC):
    """Anything that has a location and can draw itself on the screen."""

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getLoc(self):
        return (self.__x, self.__y)

    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]

    @abstractmethod
    def draw(self, surface):
        pass


class Rectangle(Drawable):
    """A filled rectangle, used for the sky and the ground."""

    def __init__(self, x, y, width, height, color):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color

    def draw(self, surface):
        x, y = self.getLoc()
        pygame.draw.rect(surface, self.__color,
                         (x, y, self.__width, self.__height))


class Snowflake(Drawable):
    """A small six-armed snowflake that falls until it lands on the ground."""

    def __init__(self, x, y, size=5, speed=1):
        super().__init__(x, y)
        self.__size = size
        self.__speed = speed
        self.__landed = False

    def isLanded(self):
        return self.__landed

    def fall(self, groundY):
        # Move down by this flake's speed. Once it reaches the ground,
        # it stops and stays there (the snow piles up).
        if self.__landed:
            return
        x, y = self.getLoc()
        y += self.__speed
        if y >= groundY:
            y = groundY
            self.__landed = True
        self.setLoc((x, y))

    def draw(self, surface):
        x, y = self.getLoc()
        s = self.__size
        white = (255, 255, 255)
        # Three lines crossing at the center make six arms
        pygame.draw.line(surface, white, (x - s, y), (x + s, y))
        pygame.draw.line(surface, white, (x - s // 2, y - s), (x + s // 2, y + s))
        pygame.draw.line(surface, white, (x - s // 2, y + s), (x + s // 2, y - s))
