import string
import random
from smart_carapi.car_instance.car_singleton import Car

colors = ['RED', 'BLUE', 'PURPLE', 'BLACK', 'GREEN', 'WHITE', 'YELLOW', 'GRAY', 'PINK', 'ORANGE', 'NAVY BLUE', 'BROWN',
          'BEIGE', 'AQUA', 'MAROON', 'KHAKI', 'DARK RED', 'SEA GREEN', 'GOLDEN', 'BRONZE', 'AZURE', 'SILVER', 'TEAL']

brands = ['TESLA', 'BMW', 'PEUGEOT', 'MINI', 'FERRARI', 'RENAULT', 'FORD', 'OPEL', 'MERCEDES', 'PORSCHE', 'DACIA',
          'CITROËN', 'LAMBORGHINI', 'LAND ROVER', 'CUPRA', 'KIA', 'SEAT', 'SUZUKI', 'AUDI', 'CHEVROLET', 'HYUNDAI']

models = ['alpha', 'beta', 'gamma']

letters = string.ascii_uppercase


def create_car() -> Car:
    """
        Method to initialize an instance Car randomly [mainly test purposes]
    :return: Car object
    """
    return Car(vin='VF1RFD00'+str(random.randint(100000000, 999999999)),
               plate_number=str(random.randint(1000, 9999)).join(random.choice(letters) for i in range(3)),
               color=colors[random.randint(0, len(colors) - 1)],
               brand=brands[random.randint(0, len(brands) - 1)],
               model=models[random.randint(0, len(models) - 1)],
               num_doors=5,
               num_seats=4,
               num_wheels=4)
