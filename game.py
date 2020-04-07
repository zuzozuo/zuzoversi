#more content soon
from board import Board 
from player import Player
from computer import Computer

#justinitialthings

board = Board()
player = Player(1)
computer = Computer(2)

playerMove = True
computerMove = False

print("==============================================================")
print("\n\tWelcome! It's zuzoversi game!")
print("\tFirst coord is vertical position(row), and second is horizontal(column)!\n")
print("===============START=====GAME==================================\n")

board.printBoard() 


#Game loop
while(board.canPlay() == 1):

    if playerMove:
        playerCoords = player.makeMove()

        if(board.canPlace(playerCoords[0], playerCoords[1], player.color, computer.color, False)):            
            player.isMoveReady(1)
        else:
            player.isMoveReady(0)
        
        if player.isReady:
            playerMove = False
            board.placeOnBoard(playerCoords[0], playerCoords[1], player.color)
            board.countScores(player.color, computer.color)
            computerMove = True
            board.printBoard()
            board.printScore()

    elif computerMove:
        computerCoords = computer.makeMove()

        if(board.canPlace(computerCoords[0], computerCoords[1], computer.color, player.color, True)):
            computer.isMoveReady(1)
        else:
            computer.isMoveReady(0)

        if computer.isReady:
            computerMove = False
            board.placeOnBoard(computerCoords[0],computerCoords[1],computer.color)
            board.countScores(player.color, computer.color) #it should be in opposite order
            playerMove = True
            board.printBoard()
            board.printScore()