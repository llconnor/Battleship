import Player
import Shot

if __name__ == '__main__':
    player1 = Player.Player()
    player2 = Player.Player()
    
    print("P1 Board")
    player1.printBoards()
    print("P2 Board")
    player2.printBoards()
    for i in range(0, 100):
        shot = player1.makeShot()
        result = player2.addShot(shot)
#        player1.sendResult(result)

#        shot = player1.makeShot()
#        result = player2.addShot(shot)
#        player1.sendResult(result)

    #print("P1 Board")
    #player1.printBoards()
    print("P2 Board")
    player2.printBoards()
    
        
    #fleet = Fleet.Fleet()
    #fleet.randomlyPlaceFleet()
    #print (fleet.getFleetLoc())
    #board.mapFleet(fleet)
    #board.printBoard()
    
# *** Todo list
# Prevent repeats of shots at the same location
# Add sink/game end logic
# Develop actual game logic
# Fix todos
