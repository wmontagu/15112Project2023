import math
import copy

from cmu_graphics import *
import random
from PIL import Image

class StageMap:
    #pass level in stageMap.
    def __init__(self, x, y, room, level, r = 30, borderWidth = 3):
        self.x = x
        self.y = y
        self.r = r
        self.room = room
        self.level = level
        self.borderWidth = borderWidth
        self.map = []
    def __repr__(self):
        return f'StageMap: ({self.x}, {self.y}, {self.room}, {self.level})'
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getLevel(self):
        return self.level
    def getRoom(self):
        return self.room
    def getRadius(self):
        return self.r
    def updateRoom(self, other):
        self.room = other
    def addStageMap(self):
        self.map.append(self)
    def getMap(self):
        return self.map
    def updateX(self, x):
        self.x = x
    def updateY(self, y):
        self.y = y
    def drawRoom(self):
        drawCircle(self.x, self.y, self.r, fill = None, borderWidth = self.borderWidth, border = "black")
        if self.room == "Enemy":
                drawCircle(self.x, self.y, self.r // 2, fill = "blue", borderWidth = self.borderWidth / 3, border = "red")
                drawLine(self.x - self.r, self.y, self.x + self.r, self.y)
                drawLine(self.x, self.y - self.r, self.x, self.y + self.r)
        elif self.room == "Final Boss":
                drawCircle(self.x, self.y, self.r, fill = "yellow", borderWidth = (self.borderWidth * 1.1) // 1, border = "black")
                drawLabel('#1', self.x, self.y, size = (self.r * 1.1) // 2, align = "center")
                #draw trophy
        elif self.room == "Unknown":
            drawLabel('?', self.x, self.y, size = self.r, align = "center")
            #draw question mark
        elif self.room == "Treasure":
            #do pythogorean theorem to fix this visual
            drawRect(self.x, self.y, self.r, self.r, fill = "white", border = 'blue', align = "center", rotateAngle = 45)
            drawLine(self.x, self.y - self.r, self.x, self.y + self.r, fill = "blue")
            drawLine(self.x - self.r, self.y, self.x + self.r, self.y, fill = "blue")
            
        elif self.room == "Recovery Site":
            drawLabel('z', self.x - self.r / 4, self.y + self.r / 4, size = self.r, align = "center")
            drawLabel('z', self.x, self.y, size = self.r, align = "center")
            drawLabel('z', self.x + self.r / 4, self.y - self.r / 4, size = self.r, align = "center")
            #draw zzzs
        elif self.room == "Shop":
            drawCircle(self.x, self.y + self.r // 3, self.r // 2, fill = "brown", borderWidth = self.borderWidth / 3, border = "black")
            drawOval(self.x, self.y - self.r // 5, self.r / 1.1, self.r // 3, fill = "brown", borderWidth = self.borderWidth / 3, border = "black")