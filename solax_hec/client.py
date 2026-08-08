"""
High-level client for the SolaX HEC charger.
"""

from .modbus import ModbusConnection
from .models import ChargeMode
from .registers import HoldingRegisters, InputRegisters


class Charger:
    """High-level interface to a SolaX HEC charger."""

    def __init__(self, host: str):
        self.modbus = ModbusConnection(host)

    def connect(self):
        """Connect to the charger."""
        return self.modbus.connect()

    def close(self):
        """Close the connection."""
        self.modbus.close()

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

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

        if not 6 <= amps <= 32:
            raise ValueError(
                "Fast charge current must be between 6A and 32A."
            )

        self.modbus.write_holding(
            HoldingRegisters.FAST_CHARGE_CURRENT,
            int(round(amps * 100)),
        )

    @property
    def charge_mode(self) -> ChargeMode:
        """
        Return the current charging mode.
        """
        value = self.modbus.read_holding(
            HoldingRegisters.CHARGE_MODE
        )
        return ChargeMode(value)

    def set_charge_mode(self, mode: ChargeMode):
        """
        Set the charger operating mode.
        """

        if not isinstance(mode, ChargeMode):
            raise TypeError("mode must be a ChargeMode")

        self.modbus.write_holding(
            HoldingRegisters.CHARGE_MODE,
            mode.value,
        )

    # ------------------------------------------------------------------
    # Live Telemetry
    # ------------------------------------------------------------------

    @property
    def grid_voltage(self) -> float:
        """
        Return the measured grid voltage in volts.
        """
        value = self.modbus.read_input(
            InputRegisters.GRID_VOLTAGE
        )
        return value / 100.0

    @property
    def grid_frequency(self) -> float:
        """
        Return the measured grid frequency in Hz.
        """
        value = self.modbus.read_input(
            InputRegisters.GRID_FREQUENCY
        )
        return value / 100.0

    @property
    def charging_current(self) -> float:
        """
        Return the current charging current in amps.
        """
        value = self.modbus.read_input(
            InputRegisters.CHARGING_CURRENT
        )
        return value / 100.0

    @property
    def charging_power(self) -> int:
        """
        Return the current charging power in watts.
        """
        return self.modbus.read_input(
            InputRegisters.CHARGING_POWER
        )