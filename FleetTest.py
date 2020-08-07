import unittest
import Fleet

class TestFleetMethods(unittest.TestCase):
    def test_fleet_placement(self):
        """
            See whether we can (randomly) place a fleet
            Checks exception passing and should (eventually)
            end up with non-overlapping fleet.  Eventually to be
            used in AI
        """
        test_fleet = Fleet.Fleet()
        test_fleet.randomlyPlaceFleet()
        for i in range(1, len(test_fleet.ship_list)):
            # will throw exceptions if there is overlap
            test_fleet.ship_list[0].shipsOverlap(test_fleet.ship_list[i])

    def test_fleet_loc(self):
        test_fleet = Fleet.Fleet()
        exp_loc = []
        for i in range(0, len(test_fleet.ship_list)):
            # will throw exceptions if there is overlap
            test_fleet.ship_list[i].placeShip(i, 2, False)
            for j in range(0, test_fleet.ship_list[i].ship_len):
                exp_loc.append([i,j+2])
        self.assertTrue(exp_loc, test_fleet.getFleetLoc())
        exp_loc = []
        for i in range(0, len(test_fleet.ship_list)):
            # will throw exceptions if there is overlap
            test_fleet.ship_list[i].placeShip(2, i, True)
            for j in range(0, test_fleet.ship_list[i].ship_len):
                exp_loc.append([j+2,i])
        self.assertTrue(exp_loc, test_fleet.getFleetLoc())

if __name__ == '__main__':
    unittest.main()
