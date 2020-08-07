import Fleet
import Shot
class Board:
    # *** TODO Make global const file
    _XSIZE=10
    _YSIZE=10
    NOTHING=0
    MISS=1
    HIT=2
    SHIP=3
    
    def __init__(self):
        self.shipboard = [[self.NOTHING for i in range(10)] for j in range(10)]
        self.shotlist = []

    def addFleet(self, fleet:Fleet):
        """
            used to add a (already placed) fleet to the board
        """
        print ("ADDING FLEET")
        self.fleet = fleet
        
    def mapFleet (self):
        """
            update shipboard with the location of our fleet
        """
        fleet_loc = self.fleet.getFleetLoc()
        for fleet_ship in fleet_loc:
            for ship_xy in fleet_ship:
                x = ship_xy[0]
                y = ship_xy[1]
                self.placeVal(self.SHIP, x, y)
        self.mapShots()
        #print (self.shipboard)

    def mapShots (self):
        for shot in self.shotlist:
            shot.printShot()
            if self.fleet.shipAt(shot.getX, shot.getY):
                self.placeVal(self.HIT, shot.getX, shot.getY)
                print ("HIT")
            else:
                self.placeVal(self.MISS, shot.getX, shot.getY)
                print ("MISS")
        
    def mapShot(self, shot:Shot):
        if self.fleet.shipAt(shot.getX(), shot.getY()):
            self.placeVal(self.HIT, shot.getX(), shot.getY())
            print ("HIT")
        else:
            self.placeVal(self.MISS, shot.getX(), shot.getY())
            print ("MISS")

    def addShot (self, shot:Shot):
        self.shotlist.append(shot)
        self.mapShot(shot)
        
        
    def placeVal(self, val:int, x:int, y:int):
        self.shipboard[x][y] = val

    def printBoard(self):
        for i in range(self._YSIZE):
            self.printSpacer()
            printstr = ""
            for j in range(self._XSIZE):
                printstr = printstr + "|"
                printstr = printstr + self.printCell(i,j)
            print(printstr + "|")
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
        for i in range(((self._YSIZE + 1) * 2) - 1):
            printstr = printstr + "-"
        print (printstr)
