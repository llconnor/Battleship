import random
import Ship

class Fleet:
    # *** TODO consolidate our constants
    _MAX_X = 9
    _MAX_Y = 9

    def __init__(self):
        self.ship_list = []
        self.ship_list.append(Ship.Ship(2))
        self.ship_list.append(Ship.Ship(3))
        self.ship_list.append(Ship.Ship(3))
        self.ship_list.append(Ship.Ship(4))
        self.ship_list.append(Ship.Ship(5))

    def placeShip(self, num_ship:int, x:int, y:int, horizontal:bool):
        # Place the ship (if there is overlap or an illegal placement then
        # we'll undo it later
        self.ship_list[num_ship].placeShip(x,y,horizontal)
        for i in range(len(self.ship_list)):
            if num_ship != i:
                if self.ship_list[i].placed:
                    self.ship_list[num_ship].shipsOverlap(self.ship_list[i])
        # *** Catch exceptions and unwind ship placement            

    def randomlyPlaceFleet(self):
        for i in range(len(self.ship_list)):
            success = False
            while not success:
                rand_x = random.randint(0, self._MAX_X)
                rand_y = random.randint(0, self._MAX_Y)
                rand_hor = bool(random.getrandbits(1))
                try:
                    print("Placing ship (i,x,y,horizontal)" + str(i) + str(rand_x) + str(rand_y) + str(rand_hor))
                    self.placeShip(i, rand_x, rand_y, rand_hor)
                    success = True
                except:
                # *** TODO figure out why we can't see except ShipOverlapException:
                # We want to check against overlap and overflow
                    pass