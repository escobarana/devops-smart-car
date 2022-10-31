class Autonomy:
    def __init__(self):
        self._avg_consumption: int = 0
        self._current_consumption: int = 0
        self._capacity: int = 100

    # --- GETTERS AND SETTERS --- #
    @property
    def avg_consumption(self):
        return self._avg_consumption

    @avg_consumption.setter
    def avg_consumption(self, val):
        self._avg_consumption = val

    @property
    def current_consumption(self):
        return self._current_consumption

    @current_consumption.setter
    def current_consumption(self, val):
        self._current_consumption = val

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, val):
        self._capacity = val
    # --- GETTERS AND SETTERS --- #

    @property
    def json(self) -> dict:
        return {
            "avg_consumption": self.avg_consumption,
            "current_consumption": self.current_consumption,
            "capacity": self.capacity
        }

    def __str__(self):
        return str(self.json)
