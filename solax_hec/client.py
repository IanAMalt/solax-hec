"""
High-level client for the SolaX HEC charger.
"""

from .modbus import ModbusConnection
from .registers import HoldingRegisters


class Charger:
    """High-level interface to a SolaX HEC charger."""

    def __init__(self, host: str):
        self.modbus = ModbusConnection(host)

    def connect(self):
        """Connect to the charger."""
        self.modbus.connect()

    def close(self):
        """Close the connection to the charger."""
        self.modbus.close()

    @property
    def fast_charge_current(self) -> float:
        """
        Return the configured Fast charging current in amps.
        """
        value = self.modbus.read_holding(
            HoldingRegisters.FAST_CHARGE_CURRENT
        )
        return value / 100.0

    def set_fast_charge_current(self, amps: float):
        """
        Set the Fast charging current in amps.
        """

        if amps < 6 or amps > 32:
            raise ValueError("Fast charge current must be between 6A and 32A.")

        value = int(round(amps * 100))

        self.modbus.write_holding(
            HoldingRegisters.FAST_CHARGE_CURRENT,
            value,
        )

    @property
    def charge_mode(self) -> str:
        """
        Return the current charging mode.
        """

        value = self.modbus.read_holding(
            HoldingRegisters.CHARGE_MODE
        )

        modes = {
            0: "Fast",
            1: "Eco",
        }

        return modes.get(value, f"Unknown ({value})")