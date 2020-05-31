class Board:
    _XSIZE=10
    _YSIZE=10
    NOTHING=0
    MISS=1
    HIT=2
    SHIP=3
    
    def __init__(self):
        self.shipboard = [[0]*self._YSIZE]*self._XSIZE 
    
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
        val = self.shipboard[x][y]
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