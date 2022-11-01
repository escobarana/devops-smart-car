import os.path
import sys
import unittest
src_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/smart_carapi/')
sys.path.append(src_path)
from smart_carapi.helpers.car_factory import create_car


class CarTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CarTest, self).__init__(*args, **kwargs)
        self.car = create_car()

    def setUp(self):
        sys.path.insert(0, "../smart_carapi")

    def test_singleton(self):
        """
            Test the singleton pattern of the class Car
        -OK: Every car_instance instance created is the same, only one unique instance can be created
        """
        car1 = create_car()
        car2 = create_car()
        self.assertTrue(car1 == car2)

    def test_vin(self):
        """
            Test the vin exists always
        -OK: Every car_instance has a unique vin identifying it, and it's not an empty string
        """
        self.assertTrue(self.car.vin)
        self.assertFalse(self.car.vin.__eq__(""))

    def test_plate_num(self):
        """
            Test the plate number exists always
        -OK: Every car_instance has a unique plate number identifying it, and it's not an empty string
        """
        self.assertTrue(self.car.plate_number)
        self.assertFalse(self.car.plate_number.__eq__(""))

    def test_car_doors(self):
        """
            Test the minimum number of doors in a car_instance
        -OK: The number of doors are correct
        """
        # Test the default number of doors when creating the car_instance
        self.assertTrue(self.car.num_doors == 5)

    def test_car_seats(self):
        """
            Test the minimum number of seats in a car_instance
        -OK: The number of seats are correct
        """
        # Test the default number of seats when creating the car_instance
        self.assertTrue(self.car.num_seats == 4)

    def test_car_wheels(self):
        """
            Test the minimum number of wheels in a car_instance
        -OK: The number of wheels are correct
        """
        # Test the default number of seats when creating the car_instance
        self.assertTrue(self.car.num_wheels == 4)

    def test_car_engine(self):
        """
            Test the car_instance engine is present
        -OK: The car_instance engine exists
        """
        self.assertTrue(self.car.engine is not None)

    def test_car_autonomy(self):
        """
            Test the car_instance autonomy module is present
        -OK: The car_instance autonomy module exists
        """
        self.assertTrue(self.car.autonomy is not None)


if __name__ == '__main__':
    unittest.main()
