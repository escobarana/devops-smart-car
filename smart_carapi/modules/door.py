class Door:
    def __init__(self, position):
        self._position: str = position
        self._lock: int = 0
        self._window: int = 0

    # --- GETTERS AND SETTERS --- #
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, val: str):
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

    @property
    def window(self):
        if self._window == 'OPEN':
            return 1
        else:
            return 0

    @window.setter
    def window(self, val: int):
        if val:
            self._window = 'OPEN'
        else:
            self._window = 'CLOSE'
    # --- GETTERS AND SETTERS --- #

    def lock_open(self):
        self.lock = 1

    def lock_close(self):
        self.lock = 0

    def window_open(self):
        self.window = 1

    def window_close(self):
        self.window = 0

    @property
    def json(self) -> dict:
        return {
            "position": self.position,
            "lock": self.lock,
            "window": self.window
        }

    def __str__(self):
        return str(self.json)
