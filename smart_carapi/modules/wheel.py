class Wheel:
    def __init__(self, position):
        self._position: str = position
        self._pressure: float = 2.2

    # --- GETTERS AND SETTERS --- #
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, val: str):
        self._position = val

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, val: int):
        self._pressure = val

    # --- GETTERS AND SETTERS --- #

    @property
    def json(self) -> dict:
        return {
            "position": self.position,
            "pressure": self.pressure
        }

    def __str__(self):
        str(self.json)
