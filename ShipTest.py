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
        
    def test_ship_non_overlap_simple(self):
        x5 = Ship.Ship(5)
        x4 = Ship.Ship(4)
        # non overlapping on horizontal
        x5.placeShip(0,0,True)
        x4.placeShip(0,1,True)
        x4.shipsOverlap(x5)
        self.assertTrue(x4.placed)
        self.assertTrue(x4.x == 0)
        self.assertTrue(x4.y == 1)
        # non overlapping on vertical
        x5.placeShip(0,0,False)
        x4.placeShip(1,0,False)
        x4.shipsOverlap(x5)
        self.assertTrue(x4.placed)
        self.assertTrue(x4.x == 1)
        self.assertTrue(x4.y == 0)
        self.assertTrue(x5.placed)
        self.assertTrue(x5.x == 0)
        self.assertTrue(x5.y == 0)

    def test_ship_overlap_x(self):
        x5 = Ship.Ship(5)
        x4 = Ship.Ship(4)
        # overlapping on horizontal
        x5.placeShip(0,0,True)
        x4.placeShip(1,0,True)
        with self.assertRaises(Exception) as context:
            x4.shipsOverlap(x5)
        self.assertFalse(x4.placed)
        self.assertTrue(x4.x == None)
        self.assertTrue(x4.y == None)
        self.assertTrue(x5.placed)
        self.assertTrue(x5.x == 0)
        self.assertTrue(x5.y == 0)

    def test_ship_overlap_y(self):
        x5 = Ship.Ship(5)
        x4 = Ship.Ship(4)
        # overlapping on vertical
        x5.placeShip(0,0,False)
        x4.placeShip(0,1,False)
        with self.assertRaises(Exception) as context:
            x4.shipsOverlap(x5)
        self.assertFalse(x4.placed)
        self.assertTrue(x4.x == None)
        self.assertTrue(x4.y == None)
        # quick check to make sure we didn't clear x5
        self.assertTrue(x5.placed)
        self.assertTrue(x5.x == 0)
        self.assertTrue(x5.y == 0)
        
    def test_ship_overlap_xy(self):
        # test that if one is vert and one horiz that we find overlap
        x5 = Ship.Ship(5)
        x4 = Ship.Ship(4)
        # overlapping at beginning
        x5.placeShip(0,0,False)
        x4.placeShip(0,0,True)
        with self.assertRaises(Exception) as context:
            x4.shipsOverlap(x5)
        self.assertFalse(x4.placed)
        self.assertTrue(x4.x == None)
        self.assertTrue(x4.y == None)
        # this should just catch the bottom of x5
        x4.placeShip(0,4,True)
        with self.assertRaises(Exception) as context:
            x4.shipsOverlap(x5)
        self.assertFalse(x4.placed)
        self.assertTrue(x4.x == None)
        self.assertTrue(x4.y == None)
        # switch x5 to horizontal and make sure we still see overlap
        x5.placeShip(0,0,True)
        x4.placeShip(4,0,False)
        with self.assertRaises(Exception) as context:
            x4.shipsOverlap(x5)
        self.assertFalse(x4.placed)
        self.assertTrue(x4.x == None)
        self.assertTrue(x4.y == None)

        

if __name__ == '__main__':
    unittest.main()
