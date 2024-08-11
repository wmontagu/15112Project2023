from enemy import *
from room import *
class Card:
    #type is either Attack, Defense or Skill
    #Effect is None or certain effect: None, poison, ice fire?
    #DMG can be zero...
    #Screw the description, make the description of the cards attributes.
    #cost is the mana cost of the card
    def __init__(self, name, upgraded, Type, effect, damage, cost):
        #if the type is defensive, then the damage equals to how much defensive it gives
        self.type = Type
        self.effect = effect
        self.damage = damage
        self.cost = cost
        self.name = name
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.upgraded = False
    def __repr__(self):
        return f'Card({self.name}, {self.upgraded}, {self.type}, {self.effect}, {self.damage}, {self.cost})'
    def __eq__(self, other):
        return isinstance(other, Card) and (self.name == other.name) and (self.upgraded == other.upgraded) and (self.effect == other.effect) and (self.cost == other.cost)
    def getDamage(self):
        return self.damage
    def getName(self):
        return self.name
    def upgrade(self):
        self.upgraded = True
        self.damage += 1
    def isUpgraded(self):
        return self.upgraded
    def getType(self):
        return self.type
    def getEffect(self):
        return self.effect
    def getCost(self):
        return self.cost
    def doDamage(self, damage, Enemy, weaken):
        if self.upgraded:
            health = math.floor(Enemy.getHealth() - (weaken * (damage + (damage * 0.2))))
        else:
            health = math.floor(Enemy.getHealth() - (weaken * (damage)))
        Enemy.updateHealth(health)
    def __eq__(self, other):
        pass
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def updateX(self, x):
        self.x = x
    def updateY(self, y):
        self.y = y
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def updateWidth(self, width):
        self.width = width
    def updateHeight(self, height):
        self.height = height