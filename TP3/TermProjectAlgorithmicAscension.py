import math
import copy
import time
from cmu_graphics import *
import random
from PIL import Image
from enemy import *
from stage import *
from card import *
from room import *
from deck import *
from startbutton import *
'''
Citations:
Cockraoch image: https://www.pestworld.org/pest-guide/cockroaches/american-cockroaches/
Pi image: https://musingsonmath.com/2012/03/13/what-does-pi-sound-like/
Character: https://www.pinterest.com/pin/204773114284801655/
Overlay (AI Art): https://www.imagine.art/dashboard/tool/from-text
Byte Image: https://bytedigital.io/

Deck Background (AI Art): https://www.imagine.art/dashboard/tool/from-text: 529804
HomeScreen (AI Art): https://www.imagine.art/dashboard/tool/from-text Seed: 870665

Defense Card Background (AI Art): https://www.imagine.art/dashboard/tool/from-text 644264

Offensive Card Background (AI Art): https://www.imagine.art/dashboard/tool/from-text :279400
'''

#logic for enemy
#harder map for generation
#GUI could be better


imageFilename = 'overlay.png'
imPIL = Image.open(imageFilename)
image1 = CMUImage(imPIL)
aspectRatio1 = imPIL.width/imPIL.height
height1 = 1600
width1 = height1 * aspectRatio1

imageFilename = 'homescreen.png'
imPIL = Image.open(imageFilename)
image2 = CMUImage(imPIL)
aspectRatio2 = imPIL.width/imPIL.height
height2 = 1600
width2 = height2 * aspectRatio2

imageFilename = 'combatoverlay.png'
imPIL = Image.open(imageFilename)
image3 = CMUImage(imPIL)
aspectRatio3 = imPIL.width/imPIL.height
height3 = 1600
width3 = height3 * aspectRatio3

imageFilename = 'cardbackGround.png'
imPIL = Image.open(imageFilename)
image4 = CMUImage(imPIL)
aspectRatio4 = imPIL.width/imPIL.height
height4 = 1600
width4 = height4 * aspectRatio4
with open("highscoreEasy.txt", "r") as file1:
    data1 = file1.read()
with open("highscoreMedium.txt", "r") as file2:
    data2 = file2.read()
with open("highscoreHard.txt", "r") as file3:
    data3 = file3.read()
def onAppStart(app):
    app.data = ''
    app.randomCardAdded = None
    app.gold = 100
    app.shopSize = 3
    #this is how I will get randomized values, scenario should happen most of the time.
    app.possibleRooms = ["Enemy", "Shop", "Enemy"]
    #they will have a very base health value, which will be multiplied later.
    #dont need coordinates of enemies
    #this map is a prelimnary map,
    app.difficulty = 1
    app.currLevel = 4
    app.Treasure = False
    app.cardsOriginal = None
    app.roomMapGenList = ["Enemy", "Enemy", "Treasure", "Shop", "Recovery Site", "Enemy"]
    app.map = None
    #need to make it such that 4 is displayed differently
    app.cards = GameDeck([Card("Rest", False, "Defensive", "Heals", 4, 1), Card("Cockroach Crusher", False, "Offensive", "Attacks", 18, 2), Card("Super Defense", False, "Defensive", "Defends", 24, 4), Card("Cockroach Crusher", False, "Offensive", "Attacks", 18, 2), Card("Strike", False, "Offensive", "Attacks", 6, 1), Card("Strike", False, "Offensive", "Attacks", 6, 1), Card("Block", False, "Defensive", "Defends", 6, 1), Card("Block", False, "Defensive", "Defends", 6, 1)])
    app.randomCards = [Card("Strike", True, "Offensive", "Attacks", 6, 1), Card("Super Defense", False, "Defensive", "Defends", 24, 4), Card("On the Offensive", True, "Offensive", "Attacks", 16, 2), Card("Block", False, "Defensive", "Defends", 6, 1), Card("Block", False, "Defensive", "Defends", 6, 1)]
    app.discardCards = DiscardDeck([])
    app.handCards = HandDeck([])
    app.deckColor = 'red'
    app.nowMap = True
    app.Combat = False
    app.Shopping = False
    app.treasureHunting = False
    app.Scenario = False
    app.isBoss = False
    app.hasWin = False
    app.time = time.time()
    app.endTime = 0
    app.totalTime = 0
    app.enemyListonScreen = []
    app.indexListforRemoving = []
    app.radius = 30
    app.mouseX = app.width/2
    app.mouseY = app.height/2
    app.currRoom = None
    app.deckMenu = False
    app.width = 1500
    app.height = 800
    app.selectedCard = None
    app.maxEnergy = 6 - app.difficulty
    app.currEnergy = app.maxEnergy
    app.character = Character(300, 500, 100, 253, 253)
    app.shopChoices = [Item("Energy", app.character, 0), Item("Health", app.character, 0), Item("Damage", app.character, 0.25), Item("Add", app.cards, 0), Item("Upgrade", app.cards, 0), Item("Remove", app.cards, 0)]
    app.treasureChoices = [Item("Energy", app.character, 0), Item("Health", app.character, 0), Item("Damage", app.character, 0.25), Item("Add", app.cards, 0), Item("Upgrade", app.cards, 0)]
    app.currShop = []
    app.myTurn = False
    app.enemyTurn = False
    app.currStage = None
    app.recoveryUsed = False
    app.gameOver = False
    app.onStart = True
    app.removingCard = False
    app.weakenAmount = 0.75
    app.startButtons = [StartButton(150, 325, "Easy"), StartButton(650, 325, "Medium"), StartButton(1150, 325, "Hard")]
    app.draw = 5

    #1, 2 or 3, for easy medium hard.
    #from the Lecture Slide #2 for images.
    

    

            


    #need play card option
    
        #need to be able to get index of card
#Should cards be a set, dictionary, or list? Set is probably not a possibility, probably dictionary?
    
def scalarCalculator(difficulty, currLevel):
    return difficulty * (5 / (currLevel + 1)) + difficulty

        
def calculateIntendedAttack(app, damage, Enemy):
    count = 0
    Enemy.setAttack(rounded(damage + damage * (scalarCalculator(app.difficulty, app.currLevel) * 0.2)))
    for card in app.cards.getCards():
        if card.getType() == "Defensive":
            count += 1
    if isinstance(Enemy, Cockroach):
        if count >= app.cards.getLength() / 2 :
            Enemy.setAttack(0)
    




def generateMap(app, mapList, roomList, difficulty, numberofLevels, startingX, startingY, currentLevel = 0, borderWidth = 1500, borderHeight = 800, r = 30):
    #use previous stage to create map recursively. The map is made differently depending on difficulty. The list give a set choice depending on what the previous room type was.
    if app.difficulty == 1:
        lChoices = [["Enemy", "Shop", "Treasure", "Unknown", "Enemy"],
                    ["Enemy", "Enemy", "Unknown", "Shop", "Enemy", "Recovery Site"],
                    ["Recovery Site", "Treasure", "Unknown", "Enemy", "Shop"],
                    ["Recovery Site", "Treasure", "Unknown", "Enemy", "Shop"],
                    ["Enemy", "Recovery Site", "Unknown", "Treasure", "Enemy", "Enemy"]]
    elif app.difficulty == 2:
        lChoices = [["Enemy", "Enemy", "Treasure", "Unknown", "Unknown", "Enemy"],
                    ["Enemy", "Enemy", "Unknown", "Unknown", "Enemy", "Recovery Site"],
                    ["Enemy", "Recovery Site", "Treasure", "Unknown", "Enemy", "Shop"],
                    ["Enemy", "Recovery Site", "Unknown", "Treasure", "Shop", "Enemy"],
                    ["Enemy", "Recovery Site", "Unknown", "Enemy", "Enemy"]]
    elif app.difficulty == 3:
        lChoices = [["Enemy", "Enemy", "Unknown", "Unknown", "Enemy"],
                    ["Enemy", "Enemy", "Unknown", "Unknown", "Enemy"],
                    ["Enemy", "Unknown", "Enemy"],
                    ["Enemy", "Unknown", "Enemy"],
                    ["Enemy", "Unknown", "Enemy", "Enemy"]]
    #guarentees each randomized map has at least one shop room.
    if currentLevel == numberofLevels:
        count = 0
        for elem in mapList:
            if elem.getRoom() == "Shop":
                count += 1
        if count >= 1:
            return mapList
        else:
            p = random.choice(mapList)
            while p.getRoom() != "Enemy" or p.getRoom() != "Unknown":
                p = random.choice(mapList)
                if p.getLevel() != numberofLevels - 1 or not p.getLevel() <= 1:
                    index = mapList.index(p)
                    mapList.remove(p)
                    p.updateRoom("Shop")
                    mapList.insert(index, p)
                    break
                else:
                    continue
        return mapList
    #ensures final stage is always the final boss
    if currentLevel == 0:
        stage = StageMap(startingX, startingY, "Final Boss", currentLevel)
        mapList.append(stage)
    else:
        roomType = " "
        for num in range(currentLevel + 1):
            if currentLevel == 1:
                roomType = "Recovery Site"
            else:
                for stage in mapList:
                    if roomType == " ":
                        #the or statement will always evaluate the first value, so must randomize which once is first.
                        possibleChoices = ([startingX + 2 * r + num * r*4, startingX - 2 * r + (num * r*4)])
                        random.shuffle(possibleChoices)
                        if (stage.getX() == possibleChoices[0] or stage.getX() == possibleChoices[1]) and stage.getY() == startingY - 2 * r:
                            previousRoom = stage.getRoom()
                            #make it so the first room you enter is always enemy or unknown.
                            if currentLevel == numberofLevels - 1:
                                for elem in lChoices:
                                    for i in range(len(elem) -1, -1, -1):
                                        if elem[i] == "Recovery Site" or elem[i] == "Treasure" or elem[i] == "Shop":
                                            elem.pop(i)
                                #change each input list.
                            if previousRoom == "Recovery Site":
                                roomType = random.choice(lChoices[0])
                            elif previousRoom == "Treasure":
                                roomType = random.choice(lChoices[1])
                            elif previousRoom == "Enemy":
                                #testing
                                roomType = random.choice(lChoices[2])
                            elif previousRoom == "Unknown":
                                roomType = random.choice(lChoices[3])
                            elif previousRoom == "Shop":
                                roomType = random.choice(lChoices[4])
            stage = StageMap(startingX + (num * r*4), startingY, roomType, currentLevel)
            roomType = " "
            mapList.append(stage)
    return generateMap(app, mapList, roomList, app.difficulty, numberofLevels, startingX - 2*r, startingY + 2*r, 1 + currentLevel, borderWidth = 1500, borderHeight = 800, r = 30)


def changeMapRecursive(app, l, mapList, x, y, level):
    return changeMapRecursiveHelper(app, [], mapList, x, y, level)

#function that removes all the non-adjacent paths
def changeMapRecursiveHelper(app, l, mapList, x, y, level, r = 30):
    if level < 0:
        return l
    if level == app.currLevel:
        for stage in mapList:
            if stage.getRoom() == "Final Boss":
                l.append(stage)
    rightNewX = x + 2 *r
    newY = y - 2 *r
    leftNewX = x - 2 * r
    m1 = copy.copy(mapList)
    for index in range (len(m1) - 1, -1, -1):
        stage = m1.pop(index)
        if (rightNewX == stage.getX() and newY == stage.getY()) or (leftNewX == stage.getX() and newY == stage.getY()):
            l.append(stage)
    return list(set(changeMapRecursiveHelper(app, l, mapList, leftNewX, newY, level - 1)).union(set(changeMapRecursiveHelper(app, l, mapList, rightNewX, newY, level - 1))))


def redrawAll(app):
    if app.onStart == True:
        drawImage(image2, 750, 400, width = width2, height = height2, align='center')
        for button in app.startButtons:
            button.draw()
        drawLabel("Algorithmic Ascension", 750, 200, size = 50, align = "center", fill = "yellow")

    elif app.gameOver == False:
        drawLabel(f'{app.gold}G', app.width /30, app.height / 15, size = 30, fill = 'yellow')
        if app.Shopping == True and app.removingCard == False:
            drawImage(image2, 750, 400, width = width2, height = height2, align='center')
            drawLabel(f'{app.gold}G', app.width /30, app.height / 15, size = 30, fill = 'yellow')
            app.cards.draw(app.cards.getLength(), "GameDeck")
            for item in app.currShop:
                item.drawItem()
        elif app.removingCard == True and app.Shopping == True:
            drawImage(image4, 750, 400, width = width4, height = height4, align = "center")
            app.cards.drawAllCardsinDeck()
        elif app.deckMenu == True and app.Shopping == True:
            drawImage(image4, 750, 400, width = width4, height = height4, align = "center")
            app.cards.drawAllCardsinDeck()
        elif app.deckMenu == True:
            drawImage(image4, 750, 400, width = width4, height = height4, align = "center")
            drawLabel("Click 'd' to close the menu and click 'down' to see more cards", app.width / 2, 5, size = 10)
            if app.deckColor == 'red':
                app.cards.drawAllCardsinDeck()
            elif app.deckColor == 'green':
                drawLabel("Click on card to play it", app.width / 2, app.height - app.height / 30, size = 10)
                app.handCards.drawAllCardsinDeck()    
            elif app.deckColor == 'blue':
                app.discardCards.drawAllCardsinDeck()
        elif app.nowMap == True:
            drawImage(image1, 750, 400, width = width1, height = height1, align='center')
            drawLabel(f'{app.gold}G', app.width /30, app.height / 15, size = 30, fill = 'yellow')
            if app.randomCardAdded != None:
                drawLabel(f'The card {app.randomCardAdded.getName()} was added to your deck.', app.width / 4, app.height / 1.5, size = 30, fill = "green")
            if app.recoveryUsed == True:
                drawLabel(f'You recovered 1/3 of your Health.', app.width/ 4, app.height / 1.5, size = 30, fill = "green")
            app.cards.draw(app.cards.getLength(), "GameDeck")
            if isinstance(app.currRoom, TreasureRoom) and app.Treasure == False:
                drawLabel(app.currRoom.getItem().getLabel(), 500, 600, size = 30, fill = "green")
            for stage in app.map:
                drawLabel("Click on red square to view deck", app.width / 2, 5, size = 10)
                drawLabel("Click on map icons to enter a room, you must click on a room at the lowest level. The recovery room heals your character by 1/3 of its max HP.", app.width / 2, 15, size = 10)
                drawLabel(f'HP: {app.character.getHealth()} / {app.character.getMaxHealth()}', app.width - app.width / 15, app.height - app.height / 15, bold = True, size = 30, fill = 'red')
                stage.drawRoom()
                
            #draw card on side
        elif app.Combat == True:
            drawImage(image3, 750, 400, width = width3, height = height3, align='center')
            if app.selectedCard != None:
                drawLabel("Click on the enemy you would like to attack", 750, 100, align = "center", size = 15, fill = "green", bold = True)
                drawLabel("Press 't' to unselect the selected card", 750, 120, align = "center", size = 15, fill = "green", bold = True)
            drawLabel(f'{app.gold}G', app.width /30, app.height / 15, size = 30, fill = 'yellow')
            drawLabel("Press 'r' to end your turn", app.width / 2, 5, size = 10)
            drawLabel("Click on any square to view that deck", app.width / 2, app.height / 30, size = 10)
            app.currRoom.drawEnemies()
            app.character.drawCharacter()
            app.currRoom.drawEnergy(app.currEnergy, app.maxEnergy)
            app.cards.draw(app.cards.getLength(), 'GameDeck')
            app.discardCards.draw(app.discardCards.getLength(), 'DiscardDeck')
            app.handCards.draw(app.handCards.getLength(), "HandDeck")
    
            #draw combat
            #you basically win
        
            #doesnt work because bug with tracking app.cards as not a gamedeck
    elif app.gameOver == True:
        drawImage(image2, 750, 400, width = width2, height = height2, align='center')
        if app.character.getHealth() <= 1:
            drawLabel(f'You have lost to the algorithm in {app.totalTime} seconds :(', app.width / 2, app.height / 2, size = 50, fill = "red")
        else:
            drawLabel(f'You have beaten the algorithm in {app.totalTime} seconds!', app.width / 2, app.height / 2, size = 50, fill = "red")
            if len(app.data) != 0:
                drawLabel(f'The record was for this difficulty {app.data} seconds!', app.width / 2, app.height / 2 + 100, size = 25, fill = "red")
            
def onMousePress(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY
    if app.removingCard == True and app.Shopping == True:
        cards = app.cards.getCards()
        for index in range(len(app.cards.getCards()) - 1, -1, -1):
            if mouseX >= cards[index].getX() and mouseY >= cards[index].getY() and mouseX <= cards[index].getX() + cards[index].getWidth() and mouseY <= cards[index].getY() + cards[index].getHeight():
                app.cards.removeCardatIndex(index)
                app.removingCard = False
    if app.onStart == True:
        for button in app.startButtons:
            if (mouseX >= button.getX() and mouseY >= button.getY() and mouseX <= button.getX() + 200 and mouseY <= button.getY() + 100):
                if button.getDifficulty() == "Easy":
                    app.difficulty = 1
                    app.currLevel = 3
                    app.data = data1
                elif button.getDifficulty() == "Medium":
                    app.difficulty = 2
                    app.currLevel = 5
                    app.data = data2
                elif button.getDifficulty() == "Hard":
                    app.difficulty = 3
                    app.currLevel = 7
                    app.data = data3
        app.map = generateMap(app, [], app.roomMapGenList, app.difficulty, app.currLevel + 1, 750, 100, currentLevel = 0, borderWidth = 1500, borderHeight = 800, r = 30)
        app.onStart = False
    app.mouseX = mouseX
    app.mouseY = mouseY
    if mouseX >= app.cards.getX() and mouseY >= app.cards.getY() and mouseX <= app.cards.getX() + app.cards.getSquare() and mouseY <= app.cards.getY() + app.cards.getSquare():
        app.deckColor = 'red'
        app.deckMenu = True
        #testing shit here
    elif mouseX >= app.discardCards.getX() and mouseY >= app.discardCards.getY() and mouseX <= app.discardCards.getX() + app.discardCards.getSquare() and mouseY <= app.discardCards.getY() + app.discardCards.getSquare():
        app.deckColor = 'blue'
        app.deckMenu = True
    elif mouseX >= app.handCards.getX() and mouseY >= app.handCards.getY() and mouseX <= app.handCards.getX() + app.handCards.getSquare() and mouseY <= app.handCards.getY() + app.handCards.getSquare():
        app.deckColor = 'green'
        app.deckMenu = True
    #where combat goes on currently
    if app.deckColor == 'green' and app.myTurn == True:
        index = 0
        while index < (app.handCards.getLength()):
            card = app.handCards.getCard(index)
            if mouseX >= card.getX() and mouseY >= card.getY() and mouseX <= card.getX() + card.getWidth() and mouseY <= card.getY() + card.getHeight():
                app.selectedCard = card
                if app.currEnergy - card.getCost() >= 0:
                    if card.getType() == "Defensive":
                        if card.getEffect() == "Heals":
                            app.character.heal(card.getDamage())
                        elif card.getEffect() == "Defends":
                            app.character.defend(card.getDamage())  
                        app.discardCards.addCard(app.handCards.getCards().pop(index))
                        app.selectedCard = None
                        app.currEnergy -= card.getCost()
                    app.deckMenu = False
            index += 1
        
                        #print and indication of not having enough energy
    
    if app.Combat == True and app.deckMenu == False and app.selectedCard != None:
        print(app.selectedCard)
        enemies = app.currRoom.getEnemies()
        
        for enemy in enemies:
            print(mouseX, mouseY)
            if (mouseX >= enemy.getX() - enemy.getWidth() / 2) and (mouseY >= enemy.getY() - enemy.getHeight() / 2) and (mouseX <= enemy.getX() + enemy.getWidth() / 2) and (mouseY <= enemy.getY() + enemy.getHeight() / 2):
                print(enemy.getX() + enemy.getWidth() / 2, enemy.getY() + enemy.getHeight() / 2)
                if app.selectedCard.getType() == "Offensive":
                    index = 0
                    
                    while index < (app.handCards.getLength()):
                        print(index)
                        card = app.handCards.getCard(index)
                        print(app.selectedCard is card, card, app.selectedCard)
                        if app.selectedCard is card:
                            if app.currEnergy - card.getCost() >= 0:
                                app.currEnergy -= card.getCost()
                                app.discardCards.addCard(app.handCards.getCards().pop(index))
                                app.selectedCard.doDamage(card.getDamage(), enemy, app.character.getWeaken() * app.character.getStrength())
                                app.selectedCard = None
                                app.currRoom.removeDeadEnemies()
                                    
                            
                            break
                            
                        index += 1
                    
        
                #make it so i can select different enemies later, we are doing one right now.
                
    
            
            
    if app.Shopping == True:
        for item in app.currShop:
            if mouseX >= item.getX() and mouseY >= item.getY() and mouseX <= item.getX() + 200 and mouseY <= item.getY() + 100:
                if item.getCost() <= app.gold:
                    app.currShop.remove(item)
                    app.gold -= item.getCost()
                    if item.getEffect() == "Energy":
                        app.maxEnergy += item.getAmount()
                    elif item.getEffect() == "Remove":
                        app.removingCard = True
                    elif item.getEffect() == "Damage":
                        app.character.setStrength(item.getAmount() * app.character.getStrength())
                    elif item.getEffect() == "Health":
                        app.character.addMaxHealth(item.getAmount())
                        app.character.updateHealth(app.character.getHealth() + item.getAmount())
                    elif item.getEffect() == "Upgrade":
                        r = item.getAmount()
                        app.cards.shuffle()
                        while r > 0:
                            card = app.cards.getCard(r)
                            if card.isUpgraded() == False:
                                card.upgrade()
                                r -= 1
                            else:
                                app.cards.shuffle()
                    elif item.getEffect() == "Add":
                        for i in range(item.getAmount()):
                            app.cards.addCard(random.choice(app.randomCards))
                            
                        
                            #this will create infinite loop while if I have more than those cards upgraded.
                                        
                            
                            
    for stage in app.map:
        if abs(mouseX - stage.getX()) < stage.getRadius() and abs(mouseY - stage.getY()) < stage.getRadius() and app.nowMap == True and stage.getLevel() == app.currLevel:
           roomType = stage.getRoom()
           app.currStage = stage
           app.randomCardAdded = None
           if roomType == "Unknown":
               roomType = app.possibleRooms[random.randrange(len(app.possibleRooms))]
           if roomType == "Enemy":
               app.currRoom = CombatRoom(roomType)
               app.nowMap = False
               app.Combat = True
               app.myTurn = True
               app.character.setWeaken(1)
               s = scalarCalculator(app.difficulty, app.currLevel)
               app.currRoom.setScalar(s)
               app.currRoom.fight()
               app.currEnergy = app.maxEnergy
               for enemy in app.currRoom.getEnemies():
                   enemy.setScalar(scalarCalculator(app.difficulty, app.currLevel))
                   enemy.setHealth()
                   enemy.setBaseHealth()
                   if isinstance(enemy, Cockroach):
                        calculateIntendedAttack(app, random.randrange(6,8), enemy)
                        if enemy.getAttack() == 0:
                            app.character.setWeaken(app.weakenAmount)
                   elif isinstance(enemy, Byte):
                        calculateIntendedAttack(app, random.randrange(8, 10), enemy)
                   elif isinstance(enemy, Pi):
                        calculateIntendedAttack(app, random.randrange(10,20), enemy)
                        if enemy.getAttack() == 0:
                            app.character.setWeaken(app.weakenAmount)
                
               app.cards.shuffle()
               for i in range(app.draw - app.difficulty):
                   if app.cards.getLength() > 0:
                       app.handCards.addCard(app.cards.getCards().pop(0))
           elif roomType == "Shop":
               app.currRoom = ShopRoom()
               app.nowMap = False
               app.Shopping = True
               temp = copy.copy(app.shopChoices)
               for i in range(app.shopSize):
                   random.shuffle(temp)
                   app.currShop.append(temp.pop(0))
               for index in range(len(app.currShop)):
                   app.currShop[index].calculateAmount(scalarCalculator(app.difficulty, app.currLevel))
                   app.currShop[index].setXY(150 + index * 500, 350)
                   
                   
                   
           elif roomType == "Final Boss":
               app.currRoom = CombatRoom(roomType)
               app.nowMap = False
               app.Combat = True
               app.isBoss = True
               app.currEnergy = app.maxEnergy
               app.character.setWeaken(1)
               s = scalarCalculator(app.difficulty, app.currLevel)
               app.currRoom.setScalar(s)
               app.currRoom.fight()
               for enemy in app.currRoom.getEnemies():
                   enemy.setScalar(scalarCalculator(app.difficulty, app.currLevel))
                   enemy.setHealth()
                   enemy.setBaseHealth()
               app.cards.shuffle()
               for i in range(app.draw - app.difficulty):
                   if app.cards.getLength() > 0:
                       app.handCards.addCard(app.cards.getCards().pop(0))
           elif roomType == "Recovery Site":
               app.currRoom = RecoverySiteRoom()
               app.currRoom.restore(app.character)
               app.recoveryUsed = True
               app.map = changeMapRecursive(app, [], app.map, app.currStage.getX(), app.currStage.getY(), app.currLevel)
               app.currLevel -= 1
           elif roomType == 'Treasure':
               app.currRoom = TreasureRoom()
               app.Treasure = True
        
def onKeyPress(app, key):
    #I think thats the right key stroke.
    if key == "d" and app.deckMenu == True:
        app.deckMenu = False
    if key == "d" and app.Shopping == True:
        app.map = changeMapRecursive(app, [], app.map, app.currStage.getX(), app.currStage.getY(), app.currLevel)
        app.currLevel -= 1
        app.Shopping = False
        
        app.nowMap = True
        app.currShop = []
    if key == "t" and app.selectedCard != None:
        app.selectedCard = None
    if key == "r" and app.myTurn == True and app.gameOver == False:
        app.character.setWeaken(1)
        app.myTurn = False
        l = app.currRoom.getEnemies()
        for enemy in l:
            app.character.takeDamage(enemy.getAttack())
            if isinstance(enemy, Cockroach):
                calculateIntendedAttack(app, random.randrange(6,12), enemy)
                if enemy.getAttack() == 0:
                    app.character.setWeaken(app.weakenAmount)
            elif isinstance(enemy, Pi):
                calculateIntendedAttack(app, random.randrange(10,20), enemy)
                if enemy.getAttack() == 0:
                    app.character.setWeaken(app.weakenAmount)
        app.character.resetDefend()
        app.currEnergy = app.maxEnergy
        while app.handCards.getLength() > 0:
            app.discardCards.addCard(app.handCards.getCards().pop())
        for i in range(app.draw - app.difficulty):
            app.cards.shuffle()
            if app.cards.getLength() != 0:
                app.handCards.addCard(app.cards.getCards().pop(0))
            else:
                while app.discardCards.getLength() > 0:
                    app.cards.addCard(app.discardCards.getCards().pop(0))
                app.cards.shuffle()
                app.handCards.addCard(app.cards.getCards().pop(0))
        
        app.myTurn = True
    
    if app.deckMenu == True and key == "down":
        if app.deckColor == "red":
            
            for i in range(16):
                app.cards.addCard(app.cards.getCards().pop(0))
        elif app.deckColor == "blue":
            for i in range(16):
                app.handCards.addCard(app.handCards.getCards().pop(0))
        elif app.deckColor == "blue":
            for i in range(16):
                app.discardCards.addCard(app.discardCards.getCards().pop(0))
        
            
        #somehow scroll to next 16 cards, maybe remove the first 16 from the list, and then put them in a temp list
        
        #add the last 16 removed cards to the front of the card list.
    if app.Combat == True and app.deckMenu == False and key == "right":
        if app.cards.getLength() > 0:
            card = app.cards.removedFirstCard()
            app.discardCards.addCard(card)
    if app.Combat == True and app.deckMenu == False and key == "left":
        if app.cards.getLength() > 0:
            card = app.cards.removedFirstCard()
            app.handCards.addCard(card)
    if app.Combat == True and key == "y":
        app.currEnergy = app.maxEnergy
    

def onStep(app):
    
    if app.map == []:
        app.gameOver = True
        app.endTime = time.time()
        app.totalTime = rounded(app.endTime - app.time)
        app.map = None
        if len(app.data) == 0 or int(app.data) > app.totalTime:
            if app.difficulty == 1:
                with open("highscoreEasy.txt", "w") as file1:
                    file1.write(str(app.totalTime))
            elif app.difficulty == 2:
                with open("highscoreMedium.txt", "w") as file2:
                    file2.write(str(app.totalTime))
            elif app.difficulty == 3:
                with open("highscoreHard.txt", "w") as file3:
                    file3.write(str(app.totalTime))
    if isinstance(app.currRoom, CombatRoom):
        if app.currRoom.getRoom() == "Final Boss" and app.currRoom.getEnemies == []:
            app.gameOver = True
            app.endTime = time.time()
            app.time = rounded(app.endTime - app.time)
            if len(app.data) == 0 or int(app.data) > app.totalTime:
                if app.difficulty == 1:
                    with open("highscoreEasy.txt", "w") as file1:
                        file1.write(str(app.totalTime))
                elif app.difficulty == 2:
                    with open("highscoreMedium.txt", "w") as file2:
                        file2.write(str(app.totalTime))
                elif app.difficulty == 3:
                    with open("highscoreHard.txt", "w") as file3:
                        file3.write(str(app.totalTime))
                
                        
            app.currRoom = None
    if app.character.getHealth() <= 0:
        app.gameOver = True
        app.endTime = time.time()
        app.totalTime = rounded(app.endTime - app.time)
        app.character.updateHealth(1)
    if app.cards.getLength() == 0:
        while app.discardCards.getLength() > 0:
            app.cards.addCard(app.discardCards.getCards().pop(0))
        app.cards.shuffle()
    
    if app.Combat == True and app.currRoom.getEnemies() == []:
        
        random.shuffle(app.randomCards)
        app.randomCardAdded = app.randomCards[0]
        app.cards.addCard(app.randomCards[0])
        
        for card in app.discardCards.getCards():
            app.cards.addCard(card)
        for card in app.handCards.getCards():
            app.cards.addCard(card)
        app.discardCards = DiscardDeck([])
        app.handCards = HandDeck([])
        app.cards.shuffle()
        
        app.map = changeMapRecursive(app, [], app.map, app.currStage.getX(), app.currStage.getY(), app.currLevel)
        
        app.character.resetDefend()
        app.Combat = False
        app.currEnergy = app.maxEnergy
        app.currLevel -= 1
        app.gold += random.randrange(10,20) * app.difficulty #should be a scalar
        app.nowMap = True
        
        
    if app.Treasure == True and isinstance(app.currRoom, TreasureRoom):
        app.map = changeMapRecursive(app, [], app.map, app.currStage.getX(), app.currStage.getY(), app.currLevel)
        app.currLevel -= 1
        item = random.choice(app.treasureChoices)
        item.calculateAmount(scalarCalculator(app.difficulty, app.currLevel))
        app.currRoom.setItem(item)
        if item.getEffect() == "Energy":
            app.maxEnergy += item.getAmount()
        elif item.getEffect() == "Remove":
            app.removingCard = True
        elif item.getEffect() == "Damage":
            app.character.setStrength(item.getAmount() * app.character.getStrength())
        elif item.getEffect() == "Health":
            app.character.addMaxHealth(item.getAmount())
            app.character.updateHealth(app.character.getHealth() + item.getAmount())
        elif item.getEffect() == "Upgrade":
            r = item.getAmount()
            app.cards.shuffle()
            while r > 0:
                card = app.cards.getCard(r)
                if card.isUpgraded() == False:
                    card.upgrade()
                    r -= 1
                else:
                    app.cards.shuffle()
        elif item.getEffect() == "Add":
            for i in range(item.getAmount()):
                app.cards.addCard(random.choice(app.randomCards))

        app.Treasure = False
def main():
    runApp()

main()