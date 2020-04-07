#more content soon

class Player:
    def __init__(self, color):
        self.color = color
        self.score = 0
        self.isReady = False
        self.coords = []

    def addPlayerScore(self, count): #score function draft
        if(self.score >= 0):
            self.score += count
        else:
            self.score = 0

    def isMoveReady(self, isMoveOk):
        if(isMoveOk == 1):
            self.isReady = True
        else:
            self.isReady = False
            
    
    def makeMove(self):
        self.isReady = False
        DIGITS1TO8 = "1 2 3 4 5 6 7 8".split()
        position = input("Enter a position: ")
        if (len(position) == 2 and position[0] in DIGITS1TO8 and position[1] in DIGITS1TO8):
            return [int(position[0])-1, int(position[1])-1]

        else:
            print("Wrong move! Try again!")
            return [-1, -1]
            
    

    
