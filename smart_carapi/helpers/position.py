# importing enum for enumerations
from enum import Enum


# creating enumerations using class
class Position(Enum):
    """
        This class represents the position in which the doors, wheels, seats, etc appear in the car
    """
    front_left = 0
    front_right = 1
    back_left = 2
    back_right = 3
    trunk = 4

    @classmethod
    def list_names(cls):
        """
            This method lists all position names of the enum class
        :return: List of position names
        """
        return list(map(lambda c: c.name, cls))
