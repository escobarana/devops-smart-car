import pymongo
import os
from smart_carapi.car_instance.car_singleton import Car
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


def get_client():
    if os.environ['ENVIRONMENT'] == 'LOCAL':
        client = pymongo.MongoClient("mongodb://localhost:27017/")
    elif os.environ['ENVIRONMENT'] == 'PRODUCTION':
        client = pymongo.MongoClient(f"mongodb://{os.environ['MONGO_INITDB_ROOT_USERNAME']}:"
                                     f"{os.environ['MONGO_INITDB_ROOT_PASSWORD']}@mongodb:27017/")
    else:
        client = None

    return client


def set_up_mongodb():
    """
        Set up function for MongoDB to create the initial database and collection where to store the data.
        Also, the initial car is created.
    :return: None
    """
    try:
        db = get_client()["smartcars"]
        collection = db["cars_data"]
        starter_car = Car(vin='VF1RFD00653635032', plate_number='1234ABC', brand='DSTI', model='alpha',
                          color='White', num_seats=4, num_doors=5, num_wheels=4).json
        load_data_to_mongodb(document=starter_car)
    except:
        logging.info(f"Cannot connect to database")


def load_data_to_mongodb(document: dict, collection: str = "cars_data", db: str = 'smartcars'):
    """
        Function to load a document to MongoDB
    :param  db: Database name
    :param  collection: Collection name
    :param  document: Document to load to MongoDB
    :return: None
    """
    try:
        database = get_client()[db]
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
    except:
        logging.info(f"Cannot connect to database")


def update_document(vin: str, payload: dict, collection: str = "cars_data", db: str = 'smartcars'):
    """
        Function to retrieve documents from MongoDB
    :param vin: Car unique identifier
    :param  db: Database name
    :param  collection: Collection name
    :param  payload: Query to update document
    :return: None
    """
    try:
        database = get_client()[db]
        col = database[collection]

        logging.info(f"Updating Car {vin} ...")

        car = col.find_one({'vin': vin})

        col.find_one_and_update({"_id": car['_id']},
                                {"$set": payload})
    except:
        logging.info(f"Cannot connect to database")


def get_data_from_mongodb(collection: str = "cars_data", db: str = 'smartcars'):
    """
        Function to retrieve documents from MongoDB
    :param  db: Database name
    :param  collection: Collection name
    :return: List of documents
    """
    my_list = []

    try:
        database = get_client()[db]
        col = database[collection]

        logging.info(f"Retrieving data from database {database}, collection {collection} ...")

        for car in col.find():
            my_list.append(car)
    except:
        logging.info(f"Cannot connect to database")

    return my_list
