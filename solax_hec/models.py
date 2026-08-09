"""Models for the SolaX HEC charger."""

from enum import Enum


class ChargeMode(Enum):
    """Charging modes supported by the SolaX HEC charger."""

    FAST = 0
    ECO = 1
    GREEN = 2

    def __str__(self) -> str:
        """Return a human-readable mode name."""
        return self.name.capitalize()


class ChargerUseMode(Enum):
    """Charger use modes supported by the SolaX HEC charger."""

    STOP = 0
    FAST = 1
    ECO = 2
    GREEN = 3

    def __str__(self) -> str:
        """Return a human-readable use mode name."""
        return self.name.capitalize()