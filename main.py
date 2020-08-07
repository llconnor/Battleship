import Board
import Ship
import Fleet

if __name__ == '__main__':
    p1_board = Board.Board()
    p1_hitboard = Board.Board()
    p2_board = Board.Board()
    p2_hitboard = Board.Board()
    
    p1_fleet = Fleet.Fleet()
    p2_fleet = Fleet.Fleet()
    
    p1_fleet.randomlyPlaceFleet()
    p2_fleet.randomlyPlaceFleet()
    
    p1_board.mapFleet(p1_fleet)
    p2_board.mapFleet(p2_fleet)
    
    print("P1 Board")
    p1_board.printBoard()
    print("P2 Board")
    p2_board.printBoard()
    
    #fleet = Fleet.Fleet()
    #fleet.randomlyPlaceFleet()
    #print (fleet.getFleetLoc())
    #board.mapFleet(fleet)
    #board.printBoard()
    
# *** Todo list
# Add shooting logic
# Add hit/sink detections
# Fix todos