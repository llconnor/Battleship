import random

class Shot:
    _XSIZE=10
    _YSIZE=10

    def __init__(self, rand:bool=True):
        self._x = 0
        self._y = 0
        if rand == True:
            self._x = random.randint(0, self._XSIZE-1)
            self._y = random.randint(0, self._YSIZE-1)

    def getX(self) -> int:
        return self._x

    def getY(self) -> int:
        return self._y

    # used to pump directly into a 2d array (since the values are swapped)
    def getInvPair(self):
        return [y,x]

    def printShot(self):
        printstr = "Making shot at " + str(self._x)
        printstr += "," + str(self._y)
        print (printstr)
