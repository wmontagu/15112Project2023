import math
import copy
from cmu_graphics import *
from card import *

class GameDeck:
    def __init__(self, cards, Screenwidth = 1500, Screenheight = 800, borderWidth = 3, deckColor = 'red'):
        self.cards = cards
        self.width = Screenwidth 
        self.height = Screenheight
        self.borderWidth = borderWidth
        self.deckColor = deckColor
        imageFilename = 'attackcard.png'
        imPIL = Image.open(imageFilename)
        self.image3 = CMUImage(imPIL)
        imageFilename = 'defensecard.png'
        imPIL = Image.open(imageFilename)
        self.image4 = CMUImage(imPIL)
    def __repr__(self):
        return f'{self.cards}'
    def getCards(self):
        return self.cards
    def getLength(self):
        return len(self.cards)
    def getX(self):
        return self.width/15
    def getY(self):
        return self.height - self.height / 6
    def getSquare(self):
        return self.width/8
    def getCard(self, index):
        return self.cards[index]
    def defensiveLabel(upgraded, effect, damage):
        return f'{effect} you by {damage}.'
    def offensiveLabel(upgraded, effect, damage):
        #must make it so that it creates a new line when the text becomes too large.
        return f'{effect} a selected enemy by {damage}.'
    def updatedeckColor(self, color):
        self.deckColor = color
    def getColor(self):
        return self.deckColor
    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self, amountofCards, Type):
        if Type == 'GameDeck':
            GameDeck.updatedeckColor(self, 'red')
            drawRect(self.width/15, self.height - self.height /6, self.width/8, self.width/8, fill = self.deckColor)
            drawLabel(f'{amountofCards}', self.width/15 + self.width/16, self.height - self.height /6 + self.width/16, size = self.width / 15, align = "center")
            drawLabel("Draw Deck", self.width/15 + self.width/16, self.height - self.height /4 + self.width/16, size = self.width / 45, align = "center")
        elif Type == 'DiscardDeck':
            GameDeck.updatedeckColor(self, 'blue')
            drawRect(self.width - self.width/15 - self.width/8, self.height - self.height /6, self.width/8, self.width/8, fill = self.deckColor)
            drawLabel(f'{amountofCards}', self.width - self.width/15 - self.width/8 + self.width/16, self.height - self.height /6 + self.width/16, size = self.width / 15, align = "center")
            drawLabel("Discard Deck", self.width - self.width/15 - self.width/8 + self.width/16, self.height - self.height /4 + self.width/16, size = self.width / 45, align = "center")
        elif Type == 'HandDeck':
            GameDeck.updatedeckColor(self, 'green')
            drawRect(self.width/2 - self.width/16, self.height - self.height/6, self.width/8, self.width/8, fill = self.deckColor)
            drawLabel(f'{amountofCards}', self.width/2 - self.width/16 + self.width/16, self.height - self.height /6 + self.width/16, size = self.width / 15, align = "center")
            drawLabel("Hand", self.width/2 - self.width/16 + self.width/16, self.height - self.height /4 + self.width/16, size = self.width / 45, align = "center")
        #add all the keys together of the cards
    def drawAllCardsinDeck(self, maxCardsonScreen = 16):
        cardIndexPlacementPass = []
        for cardIndex in range(len(self.cards)):
            multipler = cardIndex % 4
            magicX = self.width/30 + self.width//4 * multipler + self.width//100
            magicY = self.height / 400 + (cardIndex//4 * (self.height/4 + self.height / 400)) + self.height / 100
            self.cards[cardIndex].updateX(magicX)
            self.cards[cardIndex].updateY(magicY)
            cardWidth, cardHeight = self.width / 6, self.height / 4.5
            self.cards[cardIndex].updateWidth(cardWidth)
            self.cards[cardIndex].updateHeight(cardHeight)
            card = self.cards[cardIndex]
            name = card.getName()
            color = "yellow"
            if card.isUpgraded() == True:
                name = card.getName() + "+"
                color = "green"
                #add damage to card
            if card.getType() == "Offensive":
                drawImage(self.image3, magicX, magicY, width = cardWidth, height = cardHeight)
            elif card.getType() == "Defensive":
                drawImage(self.image4, magicX, magicY, width = cardWidth, height = cardHeight)
            drawRect(magicX, magicY, cardWidth, cardHeight, fill = None, borderWidth = self.borderWidth, border = "black")
            drawLabel(name, magicX + cardWidth / 2, magicY + cardHeight / 20, size = 15, fill = color)
            drawLabel(card.getType(), magicX + cardWidth / 2, magicY + cardHeight / 7, size = 15, fill = "yellow")
            drawLabel(card.getCost(), magicX + cardWidth - cardWidth / 10, magicY + cardHeight / 10, size = 15, fill = color, align = "center")
            drawCircle(magicX + cardWidth - cardWidth / 10, magicY + cardHeight / 10, self.height / 80, fill = None, borderWidth = self.width/400, border = "white")
            if card.getType() == "Defensive":
                drawLabel(GameDeck.defensiveLabel(card.isUpgraded(), card.getEffect(), card.getDamage()), magicX + cardWidth / 2, magicY + cardHeight / 2, size = 15, fill = "white", align = "center")
                #draw defensive line label
            elif card.getType() == "Offensive":
                drawLabel(GameDeck.offensiveLabel(card.isUpgraded(), card.getEffect(), card.getDamage()), magicX + cardWidth / 2, magicY + cardHeight / 2, size = 15, fill = "white", align = "center")
                #draw offensive line label
            elif card.getType() == "Spell":
                pass
                #draw spell line label
        return cardIndexPlacementPass
    def addCard(self, card):
        self.cards.append(card)
    def removedFirstCard(self):
        return self.cards.pop(0)
    def removeCardatIndex(self, index):
        self.cards.pop(index)
class DiscardDeck(GameDeck):
    def __init__(self, cards):
    #need changing sprits
        super().__init__(cards)
        self.cards = cards
    def drawCombatDiscard(self, amountofCards):
        GameDeck.updatedeckColor(self, 'blue')
        drawRect(self.width - self.width/15 - self.width/8, self.height - self.height /6, self.width/8, self.width/8, fill = super().getColor())
        drawLabel(f'{amountofCards}', self.width - self.width/15 - self.width/8 + self.width/16, self.height - self.height /6 + self.width/16, size = self.width / 15, align = "center")     
    def getX(self):
        return self.width - self.width/15 - self.width/8
    def getY(self):
        return self.height - self.height / 6
class HandDeck(GameDeck):
    def __init__(self, cards):
        super().__init__(cards)
        self.cards = cards
    def drawHand(self, amountofCards):
        GameDeck.updatedeckColor(self, 'green')
        drawRect(self.width/2 - self.width/16, self.height - self.height/6, self.width/8, self.width/8, fill = super().getColor())
        drawLabel(f'{amountofCards}', self.width/2 - self.width/16 + self.width/16, self.height - self.height /6 + self.width/16, size = self.width / 15, align = "center")          
    def getX(self):
        return self.width/2 - self.width/16
    def getY(self):
        return self.height - self.height/6


