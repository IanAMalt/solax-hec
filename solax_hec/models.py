from enum import Enum


class ChargeMode(Enum):
    FAST = 0
    ECO = 1

    def __str__(self):
        return self.name.capitalize()