class Board:
    x=10
    y=10
    def getBoard(self):
        print ("Got board")
    
    def printBoard(self):
        for i in range(self.y):
            self.printSpacer()
            printstr = ""
            for j in range(self.x):
                printstr = printstr + "| "
            print(printstr)
        self.printSpacer()
            
    def printSpacer(self):
        printstr = ""
        for i in range(self.y * 2):
            printstr = printstr + "-"
        print (printstr)
    
    #def spaceHasShip(self):