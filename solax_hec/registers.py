"""
Known SolaX HEC Modbus register definitions.

Only registers that have been experimentally verified should be added here.
"""


class HoldingRegisters:
    """Holding registers."""

    FAST_CHARGE_CURRENT = 1640
    CHARGE_MODE = 1641
    UNKNOWN_1642 = 1642