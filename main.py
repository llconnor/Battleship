import Board
import Ship

if __name__ == '__main__':
    print("Hello World")
    board = Board.Board()
    board.printBoard()
    sub = Ship.Ship(6)
    sub.placeShip(0,0, True)
    sub.getLocation()