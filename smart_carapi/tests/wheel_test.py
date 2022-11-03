import unittest
from modules.wheel import Wheel
from helpers.position import Position


class WheelTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(WheelTest, self).__init__(*args, **kwargs)
        self.wheel = Wheel(Position.front_left)

    def test_wheel_position(self):
        """
            Test the position of the wheel is correct
        -OK: the position for the wheel instance is correct and not empty
        """
        self.assertTrue(self.wheel.position.name in Position.list_names())
        self.assertTrue(self.wheel.position is not None)
        self.assertFalse(self.wheel.position == "")

    def test_wheel_pressure(self):
        """
            Test the pressure of the wheel is correct
        -OK: the pressure for the wheel instance is positive and initially 2.2
        """
        self.assertTrue(self.wheel.pressure > 0)
        self.assertFalse(self.wheel.pressure <= 0)
        # Initially wheel pressure is set to 2.2
        self.assertTrue(self.wheel.pressure == 2.2)
        # Update wheel pressure
        self.wheel.pressure = 2.0
        self.assertTrue(self.wheel.pressure == 2.0)


if __name__ == '__main__':
    unittest.main()
