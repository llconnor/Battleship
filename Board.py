import Fleet
class Board:
    _XSIZE=10
    _YSIZE=10
    NOTHING=0
    MISS=1
    HIT=2
    SHIP=3
    
    def __init__(self):
        self.shipboard = [[self.NOTHING for i in range(10)] for j in range(10)]        

        # update shipboard with the location of our fleet
    def mapFleet (self, fleet:Fleet):
        fleet_loc = fleet.getFleetLoc()
        for fleet_ship in fleet_loc:
            for ship_xy in fleet_ship:
                x = ship_xy[0]
                y = ship_xy[1]
                self.placeVal(self.SHIP, x, y)
        print (self.shipboard)
                
    def placeVal(self, val:int, x:int, y:int):
        self.shipboard[x][y] = val

    def printBoard(self):
        for i in range(self._YSIZE):
            self.printSpacer()
            printstr = ""
            for j in range(self._XSIZE):
                printstr = printstr + "|"
                printstr = printstr + self.printCell(i,j)
            print(printstr)
        self.printSpacer()
    
    def printCell(self, x:int, y:int) -> str:
        val = self.shipboard[y][x]
        if val == 0:
            return " "
        if val == 1: # miss
            return "0"
        if val == 2: # hit
            return "X"
        if val == 3: # my ship
            return "S"
        raise Exception("Cell at loc " + str(x) + "," + str(y) + " undefined board value")
    
    def printSpacer(self):
        printstr = ""
        for i in range(self._YSIZE * 2):
            printstr = printstr + "-"
        print (printstr)
    
    #def spaceHasShip(self):