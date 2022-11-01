import pymongo
from smart_carapi.car_instance.car_singleton import Car
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")


def set_up_mongodb():
    """
        Set up function for MongoDB to create the initial database and collection where to store the data.
        Also, the initial car is created.
    :return: None
    """
    db = client["smartcars"]
    collection = db["cars_data"]
    starter_car = Car(vin='VF1RFD00653635032', plate_number='1234ABC', brand='DSTI', model='alpha',
                      color='White', num_seats=4, num_doors=5, num_wheels=4).json
    load_data_to_mongodb(document=starter_car)


def load_data_to_mongodb(document: dict, collection: str = "cars_data", db: str = 'smartcars'):
    """
        Function to load a document to MongoDB
    :param  db: Database name
    :param  collection: Collection name
    :param  document: Document to load to MongoDB
    :return: None
    """
    database = client[db]
    collection = database[collection]

    logging.info(f"Loading data to database {database}, collection {collection} ...")

    if get_data_from_mongodb():
        for car in get_data_from_mongodb():
            if document['vin'] == car['vin']:
                logging.warning(f"Car {document['vin']} already exists")
                # print('Car already exists')
            else:
                collection.insert_one(document)
    else:
        collection.insert_one(document)


def update_document(vin: str, payload: dict, collection: str = "cars_data", db: str = 'smartcars'):
    """
        Function to retrieve documents from MongoDB
    :param vin: Car unique identifier
    :param  db: Database name
    :param  collection: Collection name
    :param  payload: Query to update document
    :return: None
    """
    database = client[db]
    col = database[collection]

    logging.info(f"Updating Car {vin} ...")

    car = col.find_one({'vin': vin})

    col.find_one_and_update({"_id": car['_id']},
                            {"$set": payload})


def get_data_from_mongodb(collection: str = "cars_data", db: str = 'smartcars'):
    """
        Function to retrieve documents from MongoDB
    :param  db: Database name
    :param  collection: Collection name
    :return: List of documents
    """
    my_list = []

    database = client[db]
    col = database[collection]

    logging.info(f"Retrieving data from database {database}, collection {collection} ...")

    for car in col.find():
        my_list.append(car)

    return my_list
