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


class Ship:
    _MAX_LEN = 5
    _MIN_LEN = 2
    _MIN_X = 0
    _MIN_Y = 0
    _MAX_X = 10
    _MAX_Y = 10
    
    def __init__(self, len: int):
        if (len < self._MIN_LEN) or (len > self._MAX_LEN):
            raise ShipLenException("Ship Length (" + str(len) 
                + ") outside valid range Min="
                + str(self._MIN_LEN) + " Max=" + str(self._MAX_LEN))
        self.len = len

	
    def placeShip(self, x:int, y:int, horizontal:bool):
        """ 
            Set the location of the ship.
            x -- x location on the board (traditionally A-J)
            y -- y location on the board (traditionally 1-10)
            horizontal (bool) -- whether the ship is horizontal or not
            
            NOTE: All x,y coordinates are assumed to be the top/left most
            parts of the ship
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
            if (x+self.len) > self._MAX_X:
                raise ShipOutOfBoundsException("Ship out of bounds: x = "
                + str(x) + " and len " + str(self.len) + " Max x = " + str(self._MAX_X))
        if horizontal == False:
            if (y+self.len) > self._MAX_Y:
                raise ShipOutOfBoundsException("Ship out of bounds: y = "
                + str(y) + " and len " + str(self.len) + " Max y = " + str(self._MAX_Y)) 
        self.x = x
        self.y = y
        self.horizontal = horizontal

    def atLocation(self, x:int, y:int) -> bool:
        """
            Returns True if any part of the ship exists on the x,y range indicated
        """
        if (x != self.x and y != self.y):
            return False
        if self.horizontal == True:
            if y != self.y:
                return False
            for i in range(self.x, self.x + self.len):
                if i == x:
                    return True
            return False
        else: # self.horizontal == False
            if x != self.x:
                return False
            for i in range(self.y, self.y + self.len):
                if i == y:
                    return True
            return False
        return True