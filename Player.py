import Board
import Fleet
import Shot

class Player:
    # *** TODO Figure out how to handle human players (subClass or bool)
    def __init__(self, comp:bool=True):
        self._shipboard = Board.Board()
        self._hitboard = Board.Board()
        fleet = Fleet.Fleet()
        self._comp = comp
        if self._comp==True:
            fleet.randomlyPlaceFleet()
            self._shipboard.addFleet(fleet)
            self._shipboard.mapFleet()

    def printBoards(self):
        self._hitboard.printBoard()
        self._shipboard.printBoard()

    # *** TODO: Add in logic for human players
    def makeShot(self) -> Shot:
        return Shot.Shot(self._comp)

    # *** TODO: Add in logic to see whether ship is sunk/game ends/etc
    def addShot(self, shot:Shot):
        self._shipboard.addShot(shot)


    def sendResult(self, result:int):
        print ("NOT IMPLEMENTED YET") # *** TODO
