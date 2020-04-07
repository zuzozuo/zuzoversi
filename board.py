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

    def canPlace(self, x, y): #checks if u can place paw in this place
        if(x == -1 or y == -1):
            return 0

        if(self.board[x][y] != 0):
            print("This position is taken. Try once again!")
            return 0
        else:
            return 1

    
    def placeOnBoard(self, x, y, color): 
       self.board[x][y] = color  #ox - vertical, oy is horizontal

    
    def canPlay(self): #can we still play?
        for x in range(0, self.height):
            for y in range(0, self.width):
                if self.board[x][y] == 0:
                    return 1
        print("The board is full! End of the game :)")
        return 0    
     
           



    
