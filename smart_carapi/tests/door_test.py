import unittest
from smart_carapi.modules.door import Door
from smart_carapi.helpers.position import Position


class DoorTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(DoorTest, self).__init__(*args, **kwargs)
        self.door = Door(Position.front_left)

    def test_state_door(self):
        """
            Test the state behaviour of a car_instance's door
        -OK: door state (open/close) behaves as expected
        """
        # Initially, the door is locked
        self.assertFalse(self.door.lock)
        # Open the door, state changes to True as the door is opened
        self.door.lock_open()
        self.assertTrue(self.door.lock)
        # Close the door, state changes to False as the door is closed
        self.door.lock_close()
        self.assertFalse(self.door.lock)

    def test_state_window(self):
        """
            Test the state behaviour of a car_instance's door window
        -OK: window state (open/close) behaves as expected
        """
        # Initially, the door is locked
        self.assertFalse(self.door.window)
        # Open the door, state changes to True as the door is opened
        self.door.window_open()
        self.assertTrue(self.door.window)
        # Close the door, state changes to False as the door is closed
        self.door.window_close()
        self.assertFalse(self.door.window)

    def test_door_position(self):
        """
            Test the position of the door is correct
        -OK: the position for the door instance is correct and not empty
        """
        self.assertTrue(self.door.position.name in Position.list_names())
        self.assertTrue(self.door.position is not None)
        self.assertFalse(self.door.position == "")


if __name__ == '__main__':
    unittest.main()
