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

if __name__ == '__main__':
    unittest.main()
