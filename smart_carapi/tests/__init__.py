import os.path
import sys
import unittest
src_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/smart_carapi/')
sys.path.append(src_path)
# sys.path.extend(['..\\devops-smart-car\\smart_carapi'])
from autonomy_test import AutonomyTest
from car_test import CarTest
from door_test import DoorTest
from engine_test import EngineTest
from flask_test import FlaskAppTest
from mongodb_test import MongoDBTest
from seat_belt_test import SeatTest
from wheel_test import WheelTest

if __name__ == '__main__':
    unittest.main()
