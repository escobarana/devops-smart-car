import unittest
from modules.seat import Seat
from helpers.position import Position


class SeatTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(SeatTest, self).__init__(*args, **kwargs)
        self.seat = Seat(Position.front_left)

    def test_seat_position(self):
        """
            Test the position of the seat is correct
        -OK: the position for the seat instance is correct and not empty
        """
        self.assertTrue(self.seat.position.name in Position.list_names())
        self.assertTrue(self.seat.position is not None)
        self.assertFalse(self.seat.position == "")

    def test_seat_belt_position(self):
        """
            Test the position of the seat and the belt
        -OK: seat and belt are in the same position
        """
        self.assertTrue(self.seat.position == self.seat.belt['position'])

    def test_belt_state(self):
        """
            Test the state of the seatbelt (locked/unlocked)
        -OK: seatbelt state behaves as expected
        """
        # Initially, the seatbelt is unlocked for any seat
        self.assertTrue(self.seat.belt['lock'].__eq__("UNLOCKED"))
        # Lock the belt
        self.seat.belt['lock'] = True
        self.assertTrue(self.seat.belt['lock'].__eq__("LOCKED"))

    def test_seat_occupancy(self):
        """
            Test the occupancy of the seat
        -OK: seat occupancy behaves as expected
        """
        # Initially, the seat is not occupied
        self.assertTrue(self.seat.occupied.__eq__(0))
        # Someone sits
        self.seat.occupied = 1
        self.assertTrue(self.seat.occupied.__eq__(1))


if __name__ == '__main__':
    unittest.main()
