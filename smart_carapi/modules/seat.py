from modules.belt import Belt


class Seat:

    def __init__(self, position):
        self._position: str = position
        self._belt = Belt(position=self.position)
        self._occupied: int = 0  # 0: not occupied - 1: occupied

    # --- GETTERS AND SETTERS --- #
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, val: str):
        self._position = val

    @property
    def belt(self):
        return self._belt.json

    @belt.setter
    def belt(self, val: int):
        self._belt = Belt(position=val)

    @property
    def occupied(self):
        return self._occupied

    @occupied.setter
    def occupied(self, val: int):
        self._occupied = val

    # --- GETTERS AND SETTERS --- #
    def seat_occupy(self):
        self.occupied = 1

    def set_vacancy(self):
        self.occupied = 0

    @property
    def json(self) -> dict:
        return {
            "position": self.position,
            "belt": self.belt,
            "occupied": self.occupied
        }

    def __str__(self):
        str(self.json)
