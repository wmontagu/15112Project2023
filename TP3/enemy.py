import math
import copy
from cmu_graphics import *

import random
from PIL import Image
difficulty = 1
level = 1

class Character:
   def __init__(self, x, y, height, health, maxHealth, Screenwidth = 800, Screenheight = 800):
        self.health = health
        self.maxHealth = maxHealth
        self.defense = 0
        self.weaken = 1
        self.strength = 1
        self.isWeakened = False
        imageFilename = 'character1.png'
        imPIL = Image.open(imageFilename)
        self.image = CMUImage(imPIL)
        self.aspectRatio = imPIL.width/imPIL.height
        self.height = height
        self.width = rounded(self.height * self.aspectRatio)
        self.x = x
        self.y = y
        self.screenWidth = Screenwidth
        self.screenHeight = Screenheight
   def getWeaken(self):
       return self.weaken
   def getStrength(self):
       return self.strength
   def drawCharacter(self):
        drawImage(self.image, self.x, self.y, width = self.width, height = self.height, align='center')
        if self.health > 0:
            drawRect(self.x - self.width / 1.4, self.y + self.height / 1.5, self.width * 1.5 * (self.health / self.maxHealth), self.height / 8, fill = "green")
        drawRect(self.x - self.width / 1.4, self.y + self.height / 1.5, self.width * 1.5, self.height / 8, fill = None, border = "black")
        drawLabel(f'{self.health}/{self.maxHealth}', self.x , self.y + self.height, align = 'center', size = 30)
        if (self.weaken * self.strength) != 1:
            drawLabel(f'Your attacks do {rounded(self.weaken * self.strength * 100)}% damage', self.x, self.y - self.height, align = "center", size = 30)
        if self.defense != 0:
            drawLabel(self.defense, self.x , self.y + self.height * 1.5, align = 'center', size = 30, fill = 'blue', bold = True)
   def heal(self, health):    
        self.health += health
        if self.health > self.maxHealth:
            self.health = self.maxHealth
   def defend(self, defense):
       self.defense += defense
   def getHealth(self):
       return self.health
   def isDead(self):
       return self.health >= 0
   def resetDefend(self):
       self.defense = 0
   def takeDamage(self, damage):
       while self.defense > 0 and damage > 0:
           self.defense = self.defense - 1
           damage = damage - 1
       if damage > 0:
           self.health -= damage

   def updateHealth(self, health):
       self.health = health
   def getMaxHealth(self):
       return self.maxHealth
   def addMaxHealth(self, health):
       self.maxHealth += health
   def isWeakened(self):
       return self.isWeakened
   def getWeaken(self):
       return self.weaken
   def setWeaken(self, weaken):
       self.weaken = weaken
       if self.weaken < 1:
           self.isWeakend = True
       else:
           self.isWeakend = False
   def setStrength(self, strength):
       self.strength = strength
class Enemy:
    #health will base in 0
    def __init__(self, x, y, height, health, Screenwidth = 800, Screenheight = 800):
        self.health = health
        self.name = ''
        self.description = ''
        self.isBoss = False
        self.x = x
        self.y = y
        self.height = height
        self.image = None
        self.width = None
        self.scalar = 0
        self.screenWidth = Screenwidth
        self.screenHeight = Screenheight
        self.attack = 0
        self.angle = 0
        self.baseHealth = 0
    def __repr__(self):
        return f'Enemy: {self.name}({self.x}, {self.y})'
    def updateBaseHealth(self, health):
        self.health = health
    def updateAngle(self, angle):
        self.angle = angle
    def updateName(self, name):
        self.name = name
    def updateDesc(self, desc):
        self.description = desc
    def updateHealth(self, health):
        self.health = health
    def getStatus(self):
        return self.isBoss
    def updateStatus(self):
        self.isBoss = True
    def isDead(self):
        return self.health <= 0
    def getHealth(self):
        return self.health
    def takeDamage(self, damage):
        self.health -= damage
    def getScalar(self):
        return self.scalar
    def setScalar(self, scalar):
        self.scalar = scalar
    def setAttack(self, attack):
        self.attack = attack
    def getAttack(self):
        return self.attack
    def updateImage(self, image):
        self.image = image
    def drawEnemy(self):
        drawImage(self.image, self.x, self.y, width = self.width, height = self.height, align='center', rotateAngle=self.angle)
        if self.health > 0:
            drawRect(self.x - self.width / 1.4, self.y + self.height / 1.5, self.width * 1.5 * (self.health / self.baseHealth), self.height / 8, fill = "green")
        drawRect(self.x - self.width / 1.4, self.y + self.height / 1.5, self.width * 1.5, self.height / 8, fill = None, border = "black")
        drawLabel(f'{self.health} / {self.baseHealth}', self.x - self.width , self.y + self.height / 1.5 + self.height / 16, align = 'center', size = 15, fill = "green", bold = True)
        if self.attack != 0:
            drawLabel(self.attack, self.x, self.y - self.height / 1.5, align = 'center', size = 30, fill = 'red')
        else:
            drawRect(self.x, self.y - self.height / 1.5, 30, 30, fill = "black", border = 'blue', align = "center", rotateAngle = 45)
            drawLine(self.x, self.y - 30 - self.height / 1.5, self.x, self.y + 15 - self.height / 1.5, fill = "silver")
            drawLine(self.x, self.y + 15 - self.height / 1.5, self.x, self.y + 30 - self.height / 1.5, fill = "grey")
    def aspectRatio(self, width, height):
        return width/height
    def updateWidth(self, width):
        self.width = width
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width
    def getIsBoss(self):
        return self.isBoss
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    #im not sure if this correct.
        #how do I link the health of the enemy with above
class Cockroach(Enemy):
    def __init__(self, x, y, height, health):
        #need changing sprits
        super().__init__(x, y, height, health)
        super().updateDesc("This cockroach lives and breathes of Mudge basement, it is most commonly found on the lower levels, although can be seen scurring in bathrooms up to floor 2")
        super().updateName("Cockroach")
        self.x = x
        self.y = y
        self.baseHealth = 11
        self.health = health
        imageFilename = 'cockroach.jpg'
        imPIL = Image.open(imageFilename)
        self.image = CMUImage(imPIL)
        self.aspectRatio = super().aspectRatio(imPIL.width, imPIL.height)
        self.height = height
        self.width = rounded(self.height * self.aspectRatio)
        self.attack = super().getAttack() * super().getScalar() / 4
        self.angle = 180
    def setHealth(self):
        health = int(self.baseHealth * super().getScalar())
        super().updateHealth(health)
    def setBaseHealth(self):
        health = int(self.baseHealth * super().getScalar())
        self.baseHealth = health
        
        super().updateBaseHealth(health)
    def setImage(self):
        image = self.image
        super().updateImage(image)
    def setWidth(self):
        width = self.width
        super().updateWidth(width)
    def setAngle(self):
        angle = self.angle
        super().updateAngle(angle)
class Pi(Enemy):
    #pi should be able to apply confusion, cuz idk.
    def __init__(self, x, y, height, health):
        #need changing sprits
        super().__init__(x, y, height, health)
        super().updateDesc("This legendary enemy of infinance is a final boss. Naturally, a symbol that has caused years of stress and pain from trigonometry to calculus will be here on this day ready to destory our hero.")
        super().updateName("Pi")
        self.baseHealth = 75
        self.health = health
        imageFilename = 'pi.png'
        imPIL = Image.open(imageFilename)
        self.image = CMUImage(imPIL)
        self.aspectRatio = super().aspectRatio(imPIL.width, imPIL.height)
        self.height = height
        self.width = rounded(self.height * self.aspectRatio)
        self.angle = 0
    def setBaseHealth(self):
        health = int(self.baseHealth * super().getScalar())
        self.baseHealth = health
        
        super().updateBaseHealth(health)
    def setHealth(self):
        health = int(self.baseHealth + 6 * super().getScalar())
        super().updateHealth(health)
        super().updateStatus()
    def setImage(self):
        image = self.image
        super().updateImage(image)
    def setWidth(self):
        width = self.width
        super().updateWidth(width)
    def setAngle(self):
        angle = self.angle
        super().updateAngle(angle)
        

class Byte(Enemy):
    #pi should be able to apply confusion, cuz idk.
    def __init__(self, x, y, height, health):
        #need changing sprits
        super().__init__(x, y, height, health)
        super().updateDesc("This enemy causes all the pain and bugs of this project, it attacks hard.")
        super().updateName("Byte")
        self.baseHealth = 5
        self.health = health
        imageFilename = 'byte.png'
        imPIL = Image.open(imageFilename)
        self.image = CMUImage(imPIL)
        self.aspectRatio = super().aspectRatio(imPIL.width, imPIL.height)
        self.height = height
        self.width = rounded(self.height * self.aspectRatio)
        self.angle = 0
    def setHealth(self):
        health = int(self.baseHealth + 6 * super().getScalar())
        super().updateHealth(health)
        super().updateStatus()
    def setImage(self):
        image = self.image
        super().updateImage(image)
    def setWidth(self):
        width = self.width
        super().updateWidth(width)
    def setAngle(self):
        angle = self.angle
        super().updateAngle(angle)
    def setBaseHealth(self):
        health = int(self.baseHealth * super().getScalar())
        self.baseHealth = health
        
        super().updateBaseHealth(health)


    #unique moves
    
    #moveSet

