class Engine:
    def __init__(self):
        self._status: int = 0  # 0: stop - 1: standby - 2: started
        self._temperature: float = 21.0

    # --- GETTERS AND SETTERS --- #
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, val: int):
        self._status = val

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, val: float):
        self._temperature = val

    # --- GETTERS AND SETTERS --- #

    def stop(self):
        """
            This function stops the engine
        """
        self.status = 0

    def standby(self):
        """
            This function starts the engine
        """
        self.status = 1

    def start(self):
        """
            This function starts the engine
        """
        self.status = 2

    def get_status(self):
        """
            This function returns the status in text
        """
        if self._status == 0:
            res = "OFF"
        elif self._status == 1:
            res = "STANDBY"
        else:
            res = "ON"

        return res

    @property
    def json(self) -> dict:
        return {
            "status": self.get_status(),
            "temperature": self.temperature
        }

    def __str__(self):
        return str(self.json)
