import os.path
import sys
import unittest
src_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/smart_carapi/')
sys.path.append(src_path)
import smart_carapi.flask_app as tested_app
import json


class FlaskAppTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(FlaskAppTest, self).__init__(*args, **kwargs)

    def setUp(self):
        """
            Test initial setup of the flask app
        -OK: Set up is fine
        """
        sys.path.insert(0, "../smart_carapi")
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_main_endpoint(self):
        """
            Test get main route
        -OK: Status code 200
        """
        r = self.app.get('/')
        self.assertEqual(r.status_code, 200)

    def test_get_cars_endpoint(self):
        """
            Test get /cars/ route
        -OK: Status code 200
        """
        r = self.app.get('/cars/')
        self.assertEqual(r.status_code, 200)

    def test_get_car_endpoint(self):
        """
            Test get /cars/<vin> route
        -OK: Status code 200
        """
        r = self.app.get('/cars/VF1RFD00653635032')
        self.assertEqual(r.status_code, 200)

    def test_get_car_notfound_endpoint(self):
        """
            Test get /cars/<vin> route with non-existent <vin>
        -OK: Status code 404
        """
        r = self.app.get('/cars/VF1RFD05653655032')
        self.assertEqual(r.status_code, 404)

    def test_put_car_endpoint(self):
        """
            Test put /cars/<vin> route (update car)
        -OK: Status code 200
        """
        r = self.app.put('/cars/VF1RFD00653635032',
                         content_type='application/json',
                         data=json.dumps(
                             {"autonomy": {"avg_consumption": 61, "current_consumption": 24, "capacity": 71}}))
        self.assertEqual(r.status_code, 200)

    def test_get_car_autonomy_endpoint(self):
        """
            Test get /cars/<vin>/autonomy route
        -OK: Status code 200
        """
        r = self.app.get('/cars/VF1RFD00653635032/autonomy')
        self.assertEqual(r.status_code, 200)

    def test_get_car_engine_endpoint(self):
        """
            Test get /cars/<vin>/engine route
        -OK: Status code 200
        """
        r = self.app.get('/cars/VF1RFD00653635032/engine')
        self.assertEqual(r.status_code, 200)

    def test_get_car_seats_endpoint(self):
        """
            Test get /cars/<vin>/seats route
        -OK: Status code 200
        """
        r = self.app.get('/cars/VF1RFD00653635032/seats')
        self.assertEqual(r.status_code, 200)

    def test_get_car_wheels_endpoint(self):
        """
            Test get /cars/<vin>/wheels route
        -OK: Status code 200
        """
        r = self.app.get('/cars/VF1RFD00653635032/wheels')
        self.assertEqual(r.status_code, 200)

    def test_get_car_doors_endpoint(self):
        """
            Test get /cars/<vin>/doors route
        -OK: Status code 200
        """
        r = self.app.get('/cars/VF1RFD00653635032/doors')
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
