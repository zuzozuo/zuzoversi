#more content soon
import random

class Computer:
    def __init__(self, color):
        self.score = 0
        self.color = color
        self.isReady = False

    def makeMove(self):
        randomCoords = [random.randint(0,7), random.randint(0,7)]
       # print("Computer tried this coords: {} {}".format(randomCoords[0] + 1, randomCoords[1] + 1))
        return (randomCoords)

    def isMoveReady(self, isMoveOk):
        if(isMoveOk == 1):
            self.isReady = True
        else:
            self.isReady = False

