import Board
import Ship
import Fleet

if __name__ == '__main__':
    board = Board.Board()
    board.printBoard()
    fleet = Fleet.Fleet()
    fleet.randomlyPlaceFleet()
    print (fleet.getFleetLoc())
    
# *** Todo list
# Finish board printing logic
# Add shooting logic
# Add hit/sink detections
# Fix todos