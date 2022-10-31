class Belt:
    def __init__(self, position):
        self._position: str = position
        self._lock: int = 0  # Initially, the belt is unlocked

    # --- GETTERS AND SETTERS --- #
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, val):
        self._position = val

    @property
    def lock(self):
        if self._lock == 'LOCKED':
            return 1
        else:
            return 0

    @lock.setter
    def lock(self, val: bool):
        if val:
            self._lock = 'LOCKED'
        else:
            self._lock = 'UNLOCKED'
    # --- GETTERS AND SETTERS --- #

    @property
    def json(self) -> dict:
        return {"position": self.position,
                "lock": self.lock}

    def __str__(self):
        str(self.json)
