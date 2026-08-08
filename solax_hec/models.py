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