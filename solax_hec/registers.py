"""Known SolaX HEC Modbus register definitions.

Only registers that have been experimentally verified should be added here.
"""


class InputRegisters:
    """Input registers."""

    GRID_VOLTAGE = 0          # x100 V

    CHARGING_CURRENT = 4      # x100 A
    CHARGING_POWER = 8        # W

    GRID_FREQUENCY = 12       # x100 Hz

    # Mirrors

    CHARGING_CURRENT_MIRROR = 58

    CHARGING_POWER_MIRROR_1 = 11
    CHARGING_POWER_MIRROR_2 = 61
    CHARGING_POWER_MIRROR_3 = 64


class HoldingRegisters:
    """Holding registers."""

    FAST_CHARGE_CURRENT = 1640
    CHARGE_MODE = 1641
    CHARGER_USE_MODE = 1549

    UNKNOWN_1642 = 1642