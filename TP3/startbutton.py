import math
import copy

from cmu_graphics import *
import random
from PIL import Image

class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 200
        self.height = 100
    def drawButton(self, label, label2):
        drawRect(self.x, self.y, self.width, self.height, fill = 'yellow')
        drawLabel(label, self.x + self.width / 2, self.y + self.height / 2)
        drawLabel(label2, self.x + self.width / 2, self.y + self.height / 2 + self.height / 3)
    def __repr__(self):
        return self.x, self.y
class StartButton(Button):
    def __init__(self, x, y, difficulty):
        self.x = x
        self.y = y
        self.height = 100
        self.width = 200
        self.difficulty = difficulty
    def getDifficulty(self):
        return self.difficulty
    def draw(self):
        drawRect(self.x, self.y, self.width, self.height, fill = 'yellow')
        drawLabel(self.difficulty, self.x + self.width / 2, self.y + self.height / 2)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    