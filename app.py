from flask import Flask
from flask_restx import Api, Resource, fields
from smart_carapi.car_instance.car_singleton import Car
from smart_carapi.helpers.config_mongodb import set_up_mongodb, get_data_from_mongodb, load_data_to_mongodb, \
    update_document
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app,
          version='1.0',
          title='Smart Car REST API',
          description='Documentation of the Smart Car REST API'
          )

ns = api.namespace('cars', description='operations')

# --- START MODELS --- #

autonomy = api.model('Autonomy', {
    'avg_consumption': fields.Integer(required=True, description="The car's average consumption.", min=0),
    'current_consumption': fields.Integer(required=True, description="The car's current consumption.", min=0),
    'capacity': fields.Integer(required=True, description="The car's capacity. Initially 100.", min=0)
})

engine = api.model('Engine', {
    'status': fields.String(required=True,
                            description="The car's engine status. Stop (0), StandBy (1) or Started (2). By default 0."),
    'temperature': fields.Float(required=True, description="The car's engine temperature. Initially 21.0.", min=0.0)
})

seatbelt = api.model('Seatbelt', {
    'position': fields.String(required=True,
                              description="The car's seatbelt position. Front left, front right, back left, back right."),
    'lock': fields.String(required=True,
                          description="The car's seatbelt status. Unlocked (0), locked (1). By default 0.")
})

seat = api.model('Seat', {
    'position': fields.String(required=True,
                              description="The car's seat position. Front left, front right, back left, back right."),
    'occupied': fields.Integer(required=True,
                               description="The car's seat occupancy status. Not occupied (0), occupied (1). By default 0."),
    'belt': fields.Wildcard(fields.Nested(seatbelt))
})

wheel = api.model('Wheel', {
    'position': fields.String(required=True,
                              description="The car's wheel position. Front left, front right, back left, back right."),
    'pressure': fields.Float(required=True, description="The car's wheel pressure. Initially 2.1.", min=0.0)
})

door = api.model('Door', {
    'position': fields.String(required=True,
                              description="The car's door position. Front left, front right, back left, back right, truck."),
    'lock': fields.String(required=True,
                          description="The car's seatbelt status. Unlocked (0), locked (1). By default 0."),
    'window': fields.String(required=True,
                            description="The car's door window status. Opened (1), closed (0). By default 0.")
})
car = api.model('Car', {
    'vin': fields.String(required=True, readonly=True, description="The car's unique identifier"),
    'plate_number': fields.String(required=True, description="The car's plate number"),
    'brand': fields.String(required=True, description="The car's brand"),
    'model': fields.String(required=True, description="The car's model"),
    'color': fields.String(required=True, description="The car's color"),
    'num_doors': fields.Integer(required=False, description='The number of doors the car has. By default, 5 doors.'),
    'num_seats': fields.Integer(required=False, description='The number of seats the car has. By default, 4 seats.'),
    'num_wheels': fields.Integer(required=False, description='The number of wheels the car has. By default, 4 wheels.'),
    'autonomy': fields.Wildcard(fields.Nested(autonomy)),
    'engine': fields.Wildcard(fields.Nested(engine)),
    'seats': fields.Wildcard(fields.String),
    'wheels': fields.Wildcard(fields.String),
    'doors': fields.Wildcard(fields.String),

    # The next fields are only for documenting purposes, for the models of Seat, Wheel and Door to appear in Swagger,
    # they will not appear in the response of the endpoint.
    'seats_prop': fields.Wildcard(fields.Nested(seat)),
    'doors_prop': fields.Wildcard(fields.Nested(door)),
    'wheel_prop': fields.Wildcard(fields.Nested(wheel))

})


# --- END MODELS --- #


class CarDAO(object):
    def __init__(self):
        self.car_data = get_data_from_mongodb()

    def list(self) -> list:
        return self.car_data

    def get(self, vin: str) -> dict:
        for car in self.car_data:
            if car['vin'] == vin:
                return car
        logging.error("Car {} doesn't exist".format(vin))
        api.abort(404, "Car {} doesn't exist".format(vin))

    def get_autonomy(self, vin: str) -> dict:
        for car in self.car_data:
            if car['vin'] == vin:
                return car['autonomy']
        logging.error("Car {} doesn't exist".format(vin))
        api.abort(404, "Car {} doesn't exist".format(vin))

    def get_engine(self, vin: str) -> dict:
        for car in self.car_data:
            if car['vin'] == vin:
                return car['engine']
        logging.error("Car {} doesn't exist".format(vin))
        api.abort(404, "Car {} doesn't exist".format(vin))

    def get_wheels(self, vin: str) -> dict:
        for car in self.car_data:
            if car['vin'] == vin:
                return car['wheels']
        logging.error("Car {} doesn't exist".format(vin))
        api.abort(404, "Car {} doesn't exist".format(vin))

    def get_seats(self, vin: str) -> dict:
        for car in self.car_data:
            if car['vin'] == vin:
                return car['seats']
        logging.error("Car {} doesn't exist".format(vin))
        api.abort(404, "Car {} doesn't exist".format(vin))

    def get_doors(self, vin: str) -> dict:
        for car in self.car_data:
            if car['vin'] == vin:
                return car['doors']
        logging.error("Car {} doesn't exist".format(vin))
        api.abort(404, "Car {} doesn't exist".format(vin))

    def create(self, new_car: dict) -> dict:
        load_data_to_mongodb(Car(**new_car))
        return self.car_data

    def update(self, vin: str, payload: dict) -> dict:
        new_car_ = {}
        for car in self.car_data:
            if car['vin'] == vin:
                update_document(vin, payload)
        return new_car_


logging.info('Setting up MongoDB ... ')
set_up_mongodb()

logging.info('Creating Car DAO ... ')
DAO = CarDAO()


# starter_car = Car(vin='VF1RFD00653635032', plate_number='1234ABC', brand='DSTI', model='alpha',
#                   color='White', num_seats=4, num_doors=5, num_wheels=4)
# DAO.create(starter_car.json())


# --- START ENDPOINTS --- #


@ns.route('/')
class CarList(Resource):
    """Shows a list of all cars, and lets you POST to add/modify cars"""

    @ns.doc('list_cars')
    @ns.marshal_list_with(car, skip_none=True)
    def get(self):
        """List all cars"""
        return DAO.list()

    @ns.doc('create_car')
    @ns.expect(car)
    @ns.marshal_with(car, code=201)
    def post(self):
        """Create a new car"""
        return DAO.create(api.payload), 201


@ns.route('/<string:vin>/autonomy')
@ns.response(404, 'Car not found')
@ns.param('vin', 'The car identifier')
class Autonomy(Resource):
    @ns.doc('get_car_autonomy')
    @ns.marshal_with(autonomy, skip_none=True)
    def get(self, vin):
        """Fetch a given resource"""
        return DAO.get_autonomy(vin)


@ns.route('/<string:vin>/engine')
@ns.response(404, 'Car not found')
@ns.param('vin', 'The car identifier')
class Engine(Resource):
    @ns.doc('get_car_engine')
    @ns.marshal_with(engine, skip_none=True)
    def get(self, vin):
        """Fetch a given resource"""
        return DAO.get_engine(vin)


@ns.route('/<string:vin>/wheels')
@ns.response(404, 'Car not found')
@ns.param('vin', 'The car identifier')
class Wheels(Resource):
    @ns.doc('get_car_wheels')
    @ns.marshal_with(wheel, skip_none=True)
    def get(self, vin):
        """Fetch a given resource"""
        return DAO.get_wheels(vin)


@ns.route('/<string:vin>/seats')
@ns.response(404, 'Car not found')
@ns.param('vin', 'The car identifier')
class Seats(Resource):
    @ns.doc('get_car_seats')
    @ns.marshal_with(seat, skip_none=True)
    def get(self, vin):
        """Fetch a given resource"""
        return DAO.get_seats(vin)


@ns.route('/<string:vin>/doors')
@ns.response(404, 'Car not found')
@ns.param('vin', 'The car identifier')
class Doors(Resource):
    @ns.doc('get_car_doors')
    @ns.marshal_with(door, skip_none=True)
    def get(self, vin):
        """Fetch a given resource"""
        return DAO.get_doors(vin)


@ns.route('/<string:vin>')
@ns.response(404, 'Car not found')
@ns.param('vin', 'The car identifier')
class Car(Resource):
    """Show a single car item and lets you delete them"""

    @ns.doc('get_car')
    @ns.marshal_with(car, skip_none=True)
    def get(self, vin):
        """Fetch a given resource"""
        return DAO.get(vin)

    @ns.expect(car)
    @ns.marshal_with(car)
    def put(self, vin):
        """Update a car given its vin"""
        return DAO.update(vin, api.payload)


# --- END ENDPOINTS --- #


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
