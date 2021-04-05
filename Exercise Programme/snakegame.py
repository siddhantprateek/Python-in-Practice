# couple modules required for snake game

import tkinter as tk
from tkinter import messagebox
import random
import pygame
import math


class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class snake():
    def __init__(self, color, pos):
        pass

    def move(self, pos):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self):
        pass


def drawGrid(w, rows, surface):
    sizeBtwn = w//rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        # drawing a line
        pygame.draw.line(surface, (255, ))


def redrawWindow(surface):
    global rows, width
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnacks(rows, item):
    pass


def message_box(subject, content):
    pass


def main():
    global rows, width
    width = 500
    height = 500
    row = 20       # no. of rows you want to have in your display
    # we need a surface or display to run
    win = pygame.display.set_mode((width, height))
    # need a  snake object
    # provide the position to start the snake
    # basically (255, 0, 0): red is the color and 10, 10 is at the center position
    s = snake((255, 0, 0), (10, 10))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)  # speed
        # delay us by 0.5 millisecond so that our programme does not run too fast
        clock.tick(10)  # FPS
        # this will ensure our game runs by 10 frames persecond
        redrawWindow(win)
