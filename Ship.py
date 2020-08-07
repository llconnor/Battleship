class ShipLenException(Exception):
    """Exception raised for ships being too long or too short
    """

    def __init__(self, message):
        self.message = message

class ShipOutOfBoundsException(Exception):
    """Exception raised for ships being too long or too short
    """

    def __init__(self, message):
        self.message = message

class ShipOverlapException(Exception):
    """
        Exception raised for a ship overlapping another ship
    """

    def __init__(self, message):
        self.message = message


class Ship:
    _MAX_LEN = 5
    _MIN_LEN = 2
    _MIN_X = 0
    _MIN_Y = 0
    _MAX_X = 10
    _MAX_Y = 10
    
    def __init__(self, in_len: int):
        if (in_len < self._MIN_LEN) or (in_len > self._MAX_LEN):
            raise ShipLenException("Ship Length (" + str(in_len) 
                + ") outside valid range Min="
                + str(self._MIN_LEN) + " Max=" + str(self._MAX_LEN))
        self.ship_len = in_len
        self.placed = False
        self.loc = []

	
    def placeShip(self, x:int, y:int, horizontal:bool):
        """ 
            Set the location of the ship.
            x -- x location on the board (traditionally A-J)
            y -- y location on the board (traditionally 1-10)
            horizontal (bool) -- whether the ship is horizontal or not
            
            NOTE: All x,y coordinates are assumed to be the top/left most
            parts of the ship
            Does not check to see whether other ships exist here (checked at 
            Fleet level)
        """
        if x >= self._MAX_X or y >= self._MAX_Y:
            raise ShipOutOfBoundsException("Ship out of bounds: x,y = "
                + str(x) + "," + str(y) + " Max x,y = " + str(self._MAX_X)
                + "," + str(self._MAX_Y))
        if x < self._MIN_X or y < self._MIN_Y:
            raise ShipOutOfBoundsException("Ship out of bounds: x,y = "
                + str(x) + "," + str(y) + " Min x,y = " + str(self._MIN_X)
                + "," + str(self._MIN_Y))
        if horizontal:
            if (x+self.ship_len) > self._MAX_X:
                raise ShipOutOfBoundsException("Ship out of bounds: x = "
                + str(x) + " and len " + str(self.ship_len) + " Max x = " + str(self._MAX_X))
        if horizontal == False:
            if (y+self.ship_len) > self._MAX_Y:
                raise ShipOutOfBoundsException("Ship out of bounds: y = "
                + str(y) + " and len " + str(self.ship_len) + " Max y = " + str(self._MAX_Y)) 
        self.x = x
        self.y = y
        self.horizontal = horizontal
        self.placed = True

    def atLocation(self, x:int, y:int) -> bool:
        """
            Returns True if any part of the ship exists on the x,y range indicated
        """
        """
        *** TODO get this working
        if len(self.loc) == 0:
            self.getShipLoc()
        print ("x,y" + str(x) + str(y))
        print ("Loc = " + str(self.loc))
        for i in self.loc:
            [test_x, test_y] = i
            if test_x == x and test_y == y:
                return True
        return False
        """
        if (x != self.x and y != self.y):
            return False
        if self.horizontal == True:
            if y != self.y:
                return False
            for i in range(self.x, self.x + self.ship_len):
                if i == x:
                    return True
            return False
        else: # self.horizontal == False
            if x != self.x:
                return False
            for i in range(self.y, self.y + self.ship_len):
                if i == y:
                    return True
            return False
        return True
        
    def clearShip(self):
        """
            Resets the values of the ship (used in the case when a ship
            is illegally placed)
        """
        self.x = None
        self.y = None
        self.placed = False

    def printLoc(self) -> str:
        """
            Returns a string for printing the location of a ship
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def shipsOverlap(self, comp_ship):
        """
            Checks whether this ship overlaps with another ship
            If there is an overlap then it throws an ShipOverlapException
            and clears the values for our ship
        """
        # *** TODO I really hate this On^2 implemenation, make this better
        msg = "Ship placed at " + self.printLoc() + " overlaps with Ship at " + comp_ship.printLoc()
        if self.horizontal:
            for i in range(self.x, self.x + self.ship_len):
                if comp_ship.atLocation(i, self.y):
                    self.clearShip()
                    raise ShipOverlapException(msg)
        else: # vertical placement
            for i in range(self.y, self.y + self.ship_len):
                if comp_ship.atLocation(self.x, i):
                    self.clearShip()
                    raise ShipOverlapException(msg)
        # if no exception is raised then we must be goog
    
    def getShipLoc(self):
        """
            Returns a list of x,y pairs for a ship's location
        """
        self.loc = []
        # *** TODO Add in memoization of loc data
        #if len(self.loc) > 0:
        #    return self.loc
        if self.horizontal:
            for i in range(self.x, self.x + self.ship_len):
                self.loc.append([i, self.y])
        else:
            for i in range(self.y, self.y + self.ship_len):
                self.loc.append([self.x, i])
        return self.loc
            