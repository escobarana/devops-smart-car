import os.path
import sys
import unittest
src_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/smart_carapi/')
sys.path.append(src_path)
from smart_carapi.modules.autonomy import Autonomy


class AutonomyTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(AutonomyTest, self).__init__(*args, **kwargs)
        self.autonomy = Autonomy()

    def setUp(self):
        sys.path.insert(0, "../smart_carapi")

    def test_avg_consumption(self):
        """
            Test the average consumption is a positive number
        -OK: avg_consumption is positive and not null
        """
        self.assertTrue(self.autonomy.avg_consumption >= 0)
        self.assertFalse(self.autonomy.avg_consumption < 0)
        # set value
        self.autonomy.avg_consumption = 2.3
        self.assertTrue(self.autonomy.avg_consumption == 2.3)

    def test_current_consumption(self):
        """
            Test the current consumption is a positive number
        -OK: current_consumption is positive and not null
        """
        self.assertTrue(self.autonomy.current_consumption >= 0)
        self.assertFalse(self.autonomy.current_consumption < 0)
        # set value
        self.autonomy.current_consumption = 2.3
        self.assertTrue(self.autonomy.current_consumption == 2.3)

    def test_capacity(self):
        """
            Test the capacity is a positive number
        -OK: capacity is positive and not null
        """
        self.assertTrue(self.autonomy.capacity >= 0)
        self.assertFalse(self.autonomy.capacity < 0)
        # initially is set to 100
        self.assertTrue(self.autonomy.capacity == 100)
        # set value
        self.autonomy.capacity = 89
        self.assertTrue(self.autonomy.capacity == 89)


if __name__ == '__main__':
    unittest.main()
