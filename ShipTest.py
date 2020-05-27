import unittest
import Ship

class TestShipMethods(unittest.TestCase):
    def test_shipBadSizes(self):
        # too big
        with self.assertRaises(Exception) as context:
            x6 = Ship.Ship(6)
        self.assertTrue('outside valid range' in str(context.exception))

        # too small
        with self.assertRaises(Exception) as context:
            x2 = Ship.Ship(1)
        self.assertTrue('outside valid range' in str(context.exception))

        # negative
        with self.assertRaises(Exception) as context:
            x2 = Ship.Ship(-3)
        self.assertTrue('outside valid range' in str(context.exception))
        
    def test_shipPlacementLegal(self):
        x2 = Ship.Ship(2)
        x3 = Ship.Ship(3)
        x4 = Ship.Ship(4)
        x5 = Ship.Ship(5)
        x2.placeShip(0,0,True)
        x3.placeShip(0,1,True)
        x4.placeShip(0,2,True)
        x5.placeShip(0,3,True)
    
    def test_shipPlacementOutOfBounds(self):
        x2 = Ship.Ship(2)
        with self.assertRaises(Exception) as context:
            x2.placeShip(0, 10,True)
        self.assertTrue('Ship out of bounds' in str(context.exception))
        with self.assertRaises(Exception) as context:
            x2.placeShip(10, 0,True)
        self.assertTrue('Ship out of bounds' in str(context.exception))
        with self.assertRaises(Exception) as context:
            x2.placeShip(0, -1,True)
        self.assertTrue('Ship out of bounds' in str(context.exception))
        with self.assertRaises(Exception) as context:
            x2.placeShip(-1, 0,True)
        self.assertTrue('Ship out of bounds' in str(context.exception))
    
    def test_shipPlacementStretchesOutOfBounds(self):
        x2 = Ship.Ship(2)
        with self.assertRaises(Exception) as context:
            x2.placeShip(0, 9, False)
        self.assertTrue('Ship out of bounds' in str(context.exception))
        x2 = Ship.Ship(2)
        with self.assertRaises(Exception) as context:
            x2.placeShip(9, 0, True)
        self.assertTrue('Ship out of bounds' in str(context.exception))
    
    def test_atLocation(self):
        x2 = Ship.Ship(2)
        x2.placeShip(0,0, True)
        self.assertTrue(x2.atLocation(0,0))
        
    def test_location_not_x_y(self):
        x2 = Ship.Ship(2)
        x2.placeShip(0,0, True)
        self.assertFalse(x2.atLocation(1,1))
    
    def test_location_ship_not_at_start_horizontal(self):
        x5 = Ship.Ship(5)
        
        # ship should be between x=4,8 & y=5)
        x5.placeShip(4,5,True)
        self.assertTrue(x5.atLocation(4,5))
        self.assertTrue(x5.atLocation(5,5))
        self.assertTrue(x5.atLocation(6,5))
        self.assertTrue(x5.atLocation(7,5))
        self.assertTrue(x5.atLocation(8,5))
        
        # misses 1 to the right
        self.assertFalse(x5.atLocation(9,5))
        
        # missses 1 to the left
        self.assertFalse(x5.atLocation(3,5))
        
    def test_location_ship_not_at_start_vertical(self):
        x5 = Ship.Ship(5)
        
        # ship should be between x=2 & y=3,7)
        x5.placeShip(2,3,False)
        self.assertTrue(x5.atLocation(2,3))
        self.assertTrue(x5.atLocation(2,4))
        self.assertTrue(x5.atLocation(2,5))
        self.assertTrue(x5.atLocation(2,6))
        self.assertTrue(x5.atLocation(2,7))
        
        # misses 1 to the bottom
        self.assertFalse(x5.atLocation(2,8))
        
        # missses 1 to the top
        self.assertFalse(x5.atLocation(2,2))


if __name__ == '__main__':
    unittest.main()
