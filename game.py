#more content soon
from board import Board 
from player import Player
from computer import Computer

#justinitialthings

board = Board()
player = Player("X")
computer = Computer("Z")

playerMove = True
computerMove = False

print("==============================================================")
print("\n\tWelcome! It's zuzoversi game!")
print("\tFirst coord is vertical position, and second is horizontal!\n")
print("===============START=====GAME==================================\n")

board.printBoard() 


#Game loop
while(board.canPlay() == 1):

    if playerMove:
        playerCoords = player.makeMove()

        if(board.canPlace(playerCoords[0], playerCoords[1]) == 1 and board.canPlay() == 1):            
            player.isMoveReady(1)
        else:
            player.isMoveReady(0)
        
        if player.isReady:
            playerMove = False
            board.placeOnBoard(playerCoords[0], playerCoords[1], player.color)
            computerMove = True
            board.printBoard()

    elif computerMove:
        computerCoords = computer.makeMove()

        if(board.canPlace(computerCoords[0], computerCoords[1])):
            computer.isMoveReady(1)
        else:
            computer.isMoveReady(0)

        if computer.isReady:
            computerMove = False
            board.placeOnBoard(computerCoords[0],computerCoords[1],computer.color)
            playerMove = True
            board.printBoard()
            






    #draw
     #board.printBoard()