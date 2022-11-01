import os.path
import sys
import unittest
src_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/smart_carapi/')
sys.path.append(src_path)
from smart_carapi.modules.engine import Engine


class EngineTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(EngineTest, self).__init__(*args, **kwargs)
        self.engine = Engine()

    def setUp(self):
        sys.path.insert(0, "../smart_carapi")

    def test_status_engine(self):
        """
            Test the engine status behaviour of a car_instance [stop, ready, standby]
        -OK: engine status behaves as expected
        """
        # Initially, the engine is not started
        self.assertFalse(self.engine.status.__eq__(2))
        self.assertTrue(self.engine.status.__eq__(0))
        # Start the engine
        self.engine.start()
        self.assertTrue(self.engine.status.__eq__(2))
        # Put engine in StandBy
        self.engine.standby()
        self.assertFalse(self.engine.status.__eq__(2))
        self.assertTrue(self.engine.status.__eq__(1))
        # Stop the engine
        self.engine.stop()
        self.assertFalse(self.engine.status.__eq__(1))
        self.assertTrue(self.engine.status.__eq__(0))

    def test_temperature_engine(self):
        """
            Test the temperature of the car_instance engine
        -OK: engine temperature is a positive number
        """
        self.assertFalse(self.engine.temperature < 0)
        self.assertTrue(self.engine.temperature >= 0)
        # Initially, the temperature is set to 21.0ºC
        self.assertTrue(self.engine.temperature == 21)
        # Update temperature
        self.engine.temperature = 20
        self.assertTrue(self.engine.temperature == 20)


if __name__ == '__main__':
    unittest.main()
