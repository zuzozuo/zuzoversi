import random
class Board:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 2, 0, 0, 0],
                    [0, 0, 0, 2, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]
        self.width = 8
        self.height = 8
        self.toFlip = []
        self.scores = [0, 0]
    
    def printBoard(self): 

        print(" +  1  2  3  4  5  6  7  8  +")
        print("    _  _  _  _  _  _  _  _  ")        

        for x in range(0, self.height):
            print("{}|".format(x+1), end = "  ")
            for y in range(0, self.width):
                print(self.board[x][y], end = "  ")

            print("|", end = "")
            print('\n')
        print(" +  -  -  -  -  -  -  -  -  +")

    def canPlace(self, x, y, currentColor, opponentColor, isComputerMoving): #checks if u can place paw in this place
        #isComputerMoving - temp var for hiding info about bad computer moves
        if(x == -1 or y == -1):
            return 0

        if(self.board[x][y] != 0):
            if not isComputerMoving:
                print("This position is taken. Try once again!")
            return 0
        elif(self.chceckDirection(x, y, currentColor, opponentColor) == 0):
            if not isComputerMoving:            
                print("You can't place your paw here!")
            return 0
        else:
            return 1
    
    def chceckDirection(self, x, y, currentColor, opponentColor):
        #checking x and y direction 
        directions = [[-1,-1],[0, -1], [1,-1], [-1,0], [1,0], [-1,1], [0,1], [1,1]] #we don't check [0, 0], because it's the position where we are currently
        

        for xdir, ydir in directions: 
            checkx = x
            checky = y

            checkx += xdir
            checky += ydir

            while self.areCoordsCorrect(checkx, checky) and self.isOnBoard(checkx,checky, opponentColor) == 1:
                checkx+= xdir
                checky+= ydir
                
                if self.areCoordsCorrect(checkx, checky) and self.isOnBoard(checkx, checky, currentColor) == 1:
                    while True:
                        checkx -= xdir
                        checky -=ydir
                        if(checkx == x and checky == y):
                            break
                        self.toFlip.append([checkx,checky])

        if len(self.toFlip) == 0: #Turn is correct if at least one paw can be flipped
            return 0  
        else: 
            return 1         

       
    def isOnBoard(self, x, y, color):
        if(self.board[x][y] == color):
            return 1
        else:
            return 0
    
    def areCoordsCorrect(self, x, y):
        if (x >= 0 and x <=7 and y >=0 and y <=7):
            return 1
        else: 
            return 0
    
    def placeOnBoard(self, x, y, color): 
       self.board[x][y] = color  #ox - vertical, oy is horizontal

       for xToFlip,yToFlip in self.toFlip:
           self.board[xToFlip][yToFlip] = color
        
       self.toFlip = []
    
    def countScores(self, playerColor, opponentColor):
        playerScore = 0
        opponentScore = 0

        for x in range(0, self.height):
            for y in range(0, self.width):
                if(self.board[x][y] == playerColor):
                    playerScore +=1
                elif(self.board[x][y] == opponentColor):
                    opponentScore +=1
        self.scores = [playerScore, opponentScore]

    
    def canPlay(self): #can we still play?
        for x in range(0, self.height):
            for y in range(0, self.width):
                if self.board[x][y] == 0:
                    return 1
        print("The board is full! End of the game :)")
        return 0    

    def printScore(self): #it should be like your scores and opponent's scores, it's temporary soluton

        print("\nYour score is: {}".format(self.scores[0]))
        print("\nComputer score is: {}\n".format(self.scores[1]))

    def randomBoard(self, howMany):
        COLOR1 = 1
        COLOR2 = 2

        color1Move = True
        color2Move = False
        i = 0
        coords1 = [0, 0]
        coords2 = [0, 0]

        while( i < howMany - 4):  
            
            if color1Move:              

                if (self.canPlace(coords1[0], coords1[1], COLOR1, COLOR2, True)):
                    self.placeOnBoard(coords1[0], coords1[1], COLOR1)
                    color1Move = False
                    color2Move = True
                    i+=1
                else:
                    coords1 = [random.randint(0,7), random.randint(0,7)]

            if color2Move:
                if (self.canPlace(coords2[0], coords2[1], COLOR2, COLOR1, True)):
                    self.placeOnBoard(coords2[0], coords2[1], COLOR2)
                    color2Move = False
                    color1Move = True
                    i+=1
                else:
                    coords2 = [random.randint(0,7), random.randint(0,7)]
            
        self.countScores(COLOR1, COLOR2)
        self.printBoard()

        print("There are {} paws of 1 color and {} of 2 color".format(self.scores[0], self.scores[1]))





        
     
