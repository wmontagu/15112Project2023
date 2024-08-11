from enemy import *
import random
from startbutton import *
from deck import *
class CombatRoom:
    #make a room class, make the other classes in that
    def __init__(self, Room):
        self.Room = Room
        self.enemies = []
        self.possibleEnemies = [Cockroach(1000, 500, 100, 0), Byte(1000, 500, 100, 0), Pi(1000, 500, 200, 0)]
        self.indexListforRemoving = []
        self.scalar = 0
    def getEnemies(self):
        return self.enemies
    def addEnemy(self, enemy):
        if isinstance(enemy, Enemy):
            self.enemies += [enemy]
    def drawEnemies(self):
        for enemy in self.enemies:
            enemy.drawEnemy()
    def drawEnergy(self, currEnergy, maxEnergy):
        drawLabel(f'{currEnergy} / {maxEnergy}', 200, 450, size = 30, fill = 'lightgreen')
        #draw all enemies in list
    def removeDeadEnemies(self):   
        for index in range(len(self.enemies)):
            if self.enemies[index].isDead():
                self.indexListforRemoving.insert(0, index)
                print(self.indexListforRemoving)
        for index in self.indexListforRemoving:
            self.enemies.pop(index)
        self.indexListforRemoving = []
    def setScalar(self, scalar):
        print(scalar)
        self.scalar = scalar
    def fight(self):
        for number in range(-1, int(self.scalar // 4)):
            if self.Room == "Final Boss":
                enemy = self.possibleEnemies[2]
                enemy.setWidth()
                enemy.setAngle()
                CombatRoom.addEnemy(self, enemy)
                break
            else:
                r = random.randrange(0, 2)
                l = copy.copy(self.possibleEnemies)
                enemy = l[r]
                if isinstance(enemy, Cockroach):
                    enemy = (Cockroach(1000, 500, 100, 0))
                elif isinstance(enemy, Byte):
                    enemy = (Byte(1000, 500, 100, 0))
                x = enemy.getX() + (number * 100)
                y = enemy.getY() + (number * 100)
                print(x, y)
                enemy.setX(x)
                enemy.setY(y)
            enemy.setWidth()
            enemy.setAngle()
            CombatRoom.addEnemy(self, enemy)
    def combatOver(self):
        return self.enemies == []
            #add enemies to list according to level of place and difficulty modifer
    def getRoom(self):
        return self.Room
    
class ShopRoom:
    def __init__(self):
        #room to buy cards or upgrades.
        self.items = []
    def exchange(self, cost, gold):
        if not cost <= gold:
            gold = gold - cost
    def getItems(self):
        return self.items
class Item:
    def __init__(self, effect, changedObject, cost):
        self.effect = effect
        self.amount = 1
        self.changedObject = changedObject
        self.cost = cost
        self.x = 0
        self.y = 0
    def setCost(self, cost):
        self.cost = cost
    def getLabel(self):
        if isinstance(self.changedObject, Character):
            if self.effect == "Damage":
                return f'Added {rounded(self.amount * 100)}% to your {self.effect}'
            else:
                return f'Added {self.amount} to your {self.effect}'
        elif isinstance(self.changedObject, GameDeck):
            if self.effect == "Upgrade":
                return f'{self.effect}ed {self.amount} cards in your deck'
            elif self.effect == "Add":
                return f'{self.effect}ed {self.amount} random cards to your deck'
            elif self.effect == "Remove":
                return f'{self.effect}d {self.amount} card from your deck'
    def calculateAmount(self, scalar):
        if isinstance(self.changedObject, Character):
            if self.effect == "Energy":
                self.amount = 1
            elif self.effect == "Health":
                self.amount = int(scalar * 7 * self.amount)
            elif self.effect == "Damage":
                self.amount = (1 / scalar) + 1
        elif isinstance(self.changedObject, GameDeck):
            if self.effect == "Add":
                self.amount = math.ceil(scalar / 20)
            elif self.effect == "Upgrade":
                self.amount = math.ceil((scalar * self.amount) / 20)
            elif self.effect == "Remove":
                self.amount = 1
        self.cost = rounded(scalar * random.randrange(10,20))
    def getAmount(self):
        return self.amount
    def drawItem(self):
        button = Button(self.x, self.y)
        if isinstance(self.changedObject, Character):
            if self.effect == "Damage":
                button.drawButton(f'Add {rounded(self.amount * 100)}% to your {self.effect}', f'{self.cost}G')
            else:
                button.drawButton(f'Add {self.amount} to your {self.effect}', f'{self.cost}G')
        elif isinstance(self.changedObject, GameDeck):
            button = Button(self.x, self.y)
            if self.effect == "Upgrade":
                button.drawButton(f'{self.effect} {self.amount} cards in your deck', f'{self.cost}G')
            elif self.effect == "Add":
                button.drawButton(f'{self.effect} {self.amount} random cards to your deck', f'{self.cost}G')
            elif self.effect == "Remove":
                button.drawButton(f'{self.effect} {self.amount} card from your deck', f'{self.cost}G')
    def setXY(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getEffect(self):
        return self.effect
    def changedObject(self):
        return self.changedObject
    def getCost(self):
        return self.cost
class TreasureRoom:
    def __init__(self):
        self.Item = None
    def setItem(self, Item):
        self.Item = Item
    def getItem(self):
        return self.Item
        #works similarly to shop but gives you something random and tells you want it gives you.
        
        pass
class RecoverySiteRoom:
    def __init__(self):
        self.restoreAmount = 0
    def restore(self, character):
        health = character.getHealth() + rounded(character.getMaxHealth() / 3)
        if health >= character.getMaxHealth():
            character.updateHealth(character.getMaxHealth())
        else:
            character.heal(health)
    
class Scenario:
    def __init__(self):
        pass