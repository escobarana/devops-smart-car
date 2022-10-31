import unittest
from smart_carapi.helpers.config_mongodb import update_document, get_data_from_mongodb, load_data_to_mongodb, \
    set_up_mongodb, client
from car_instance.car_singleton import Car


class MongoDBTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MongoDBTest, self).__init__(*args, **kwargs)

    def test_mongodb_connection(self):
        """
            Test the correct connection with mongodb
        -OK: connected to mongodb
        """
        self.assertTrue(client.server_info())

    def test_mongodb_database_collection(self):
        """
            Test that the database and collection are created
        -OK: Database and collection are created in mongodb
        """
        set_up_mongodb()

        self.assertTrue("smartcars" in client.list_database_names())

        db = client['smartcars']
        self.assertTrue("cars_data" in db.list_collection_names())

    def test_mongodb_only_one_car(self):
        """
            Test that the mongodb collection contains exactly one car
        -OK: Database collection contains exactly one document
        """
        self.assertTrue(len(get_data_from_mongodb()) == 1)

    def test_mongodb_load_data(self):
        """
            Test loading data to mongodb, no cars with same vin are allowed
        -OK: Load data
        """
        starter_car = Car(vin='VF1RFD00653635032', plate_number='1234ABC', brand='DSTI', model='alpha',
                          color='White', num_seats=4, num_doors=5, num_wheels=4).json

        load_data_to_mongodb(document=starter_car)

        self.assertTrue(len(get_data_from_mongodb()) == 1)

    def test_mongodb_update_document(self):
        """
            Test updating document in mongodb
        -OK: Update car document
        """
        payload = {"autonomy": {"avg_consumption": 61, "current_consumption": 24, "capacity": 71}}
        vin = 'VF1RFD00653635032'

        update_document(vin=vin, payload=payload)

        self.assertTrue(len(get_data_from_mongodb()) == 1)


if __name__ == '__main__':
    unittest.main()
