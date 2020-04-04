class Board:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]
        self.width = 8
        self.height = 8
        self.x = 0
        self.y = 0
    
    def printBoard(self): 

        print(" +  1  2  3  4  5  6  7  8  +")
        print("    _  _  _  _  _  _  _  _  ")        

        for x in range(0, self.height):
            print("{}|".format(x), end = "  ")
            for y in range(0, self.width):
                print(self.board[x][y], end = "  ")

            print("|", end = "")
            print('\n')
        print(" +  -  -  -  -  -  -  -  -  +")

    def getPosition(self):
        DIGITS1TO8 = "1 2 3 4 5 6 7 8".split()
        position = input("Enter a position: ")
        if (len(position) == 2 and position[0] in DIGITS1TO8 and position[1] in DIGITS1TO8):
            self.x = int(position[0])-1
            self.y = int(position[1])-1
        else:
            print("Something went wrong! Try again!")

    
    def insertPaw(self, x, y):
        if x > 8 or x < 0:
            print("Wrong  x position! Try once again!")
            return 0

        if y > 8 or y < 0:
            print("Wrong y position! Try once again!")
            return 0

        if(self.board[self.x][self.y] != 0):
            print("This position is taken. Try once again!")
            return 0

        self.board[self.x][self.y] ="x"  #oś x jako pionowa, oś y jako pozioma

        return 0
    
    def canPlay(self): #can we still play?
        for x in range(0, self.height):
            for y in range(0, self.width):
                if self.board[x][y] == 0:
                    return 1
        return 0
    
    #def canPlace(self, x, y): #checks if u can place paw in this place 
    
    def update(self):
        while(self.canPlay() == 1):
            self.getPosition()
            self.insertPaw(self.x, self.y)
            self.printBoard()









            



    
