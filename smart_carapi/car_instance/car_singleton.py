from helpers.position import Position
from modules import Autonomy, Door, Engine, Seat, Wheel


class Car(object):
    _car_instance = None  # Initialize the instance to 'None' for Singleton Pattern

    _vin: str = ""
    _plate_number: str = ""
    _brand: str = ""
    _model: str = ""
    _color: str = ""
    _num_doors: int = 0
    _num_seats: int = 0
    _num_wheels: int = 0

    # None private attributes
    autonomy: Autonomy = None
    engine: Engine = None
    seats: list = None
    wheels: list = None
    doors: list = None  # The trunk of a car_instance is considered as a door

    def __new__(cls, vin: str,
                plate_number: str,
                brand: str,
                model: str,
                color: str,
                num_seats: int = 4,
                num_doors: int = 5,
                num_wheels: int = 4,
                autonomy=None,
                engine=None,
                doors=None,
                seats=None,
                wheels=None):
        if cls._car_instance is None:
            # Creating the car_instance object
            cls._car_instance = super(Car, cls).__new__(cls)

            # Initialization
            cls._vin = vin
            cls._plate_number = plate_number
            cls._brand = brand
            cls._model = model
            cls._color = color
            cls._num_seats = num_seats
            cls._num_doors = num_doors
            cls._num_wheels = num_wheels

            # sensors
            cls.autonomy = Autonomy()
            cls.engine = Engine()
            cls.doors = Car.default_doors(num_doors)
            cls.seats = Car.default_seats(num_seats)
            cls.wheels = Car.default_wheels(num_wheels)

        return cls._car_instance

    # --- GETTERS AND SETTERS --- #
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, val: str):
        self._vin = val

    @property
    def plate_number(self):
        return self._plate_number

    @plate_number.setter
    def plate_number(self, val: str):
        self._plate_number = val

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, val: str):
        self._brand = val

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, val: str):
        self._model = val

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, val: str):
        self._color = val

    @property
    def num_seats(self):
        return self._num_seats

    @staticmethod
    def default_seats(num_seats: int) -> list:
        result = []
        for pos in range(num_seats):
            result.append(Seat(position=Position(pos).name).json)
        return result

    @num_seats.setter
    def num_seats(self, val):
        self._num_seats = val
        self.seats = Car.default_seats(val)

    @property
    def num_doors(self):
        return self._num_doors

    @staticmethod
    def default_doors(num_doors: int) -> list:
        result = []
        for pos in range(num_doors):
            result.append(Door(position=Position(pos).name).json)
        return result

    @num_doors.setter
    def num_doors(self, val):
        self._num_doors = val
        self.doors = Car.default_doors(val)

    @property
    def num_wheels(self):
        return self._num_wheels

    @staticmethod
    def default_wheels(num_wheels: int) -> list:
        result = []
        for pos in range(num_wheels):
            result.append(Wheel(position=Position(pos).name).json)
        return result

    @num_wheels.setter
    def num_wheels(self, val):
        self._num_wheels = val
        self.wheels = Car.default_wheels(val)

    # --- GETTERS AND SETTERS --- #

    @property
    def json(self):
        return {
            "vin": self.vin,
            "plate_number": self.plate_number,
            "brand": self.brand,
            "model": self.model,
            "color": self.color,
            "num_seats": self.num_seats,
            "num_doors": self.num_doors,
            "num_wheels": self.num_wheels,
            "autonomy": self.autonomy.json,
            "engine": self.engine.json,
            "doors": [v for v in self.doors],
            "seats": [v for v in self.seats],
            "wheels": [v for v in self.wheels],
        }

    def __str__(self):
        return str(self.json)
