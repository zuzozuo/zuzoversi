#more content soon
from board import Board 
from player import Player
from computer import Computer


print("==============================================================")
print("\n\tWelcome! It's zuzoversi game!\n")
print("==============================================================\n")
print("1. Computer vs Player\n")
print("2. Random board generator\n")
MODE = int(input("Chose number to select mode: \n"))
print("==============================================================")

if MODE == 1:
    print("==============================================================")
    print("\tFirst coord is vertical position(row), and second is horizontal(column)!\n")
    print("===============START=====GAME==================================\n")

    #initalize  game
    board = Board()
    player = Player(1)
    computer = Computer(2)

    playerMove = True
    computerMove = False

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

elif MODE == 2:

    howMany = int(input("Give me number from 4 to 64: "))

    board = Board()

    if howMany == 4:
        board.printBoard()

    elif howMany > 4 and howMany <=64:
        board.randomBoard(howMany)     

    else:
        print("Wrong number of paws :(")

else:
    print("Wrong input my dear!")

