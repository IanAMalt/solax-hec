"""
Simple example demonstrating the Modbus wrapper.

Run from the project root with:

    python -m examples.test_modbus
"""

from solax_hec.modbus import ModbusConnection
from solax_hec.registers import HoldingRegisters

HOST = "192.168.0.169"

mb = ModbusConnection(HOST)

try:
    print("Connecting...")
    mb.connect()

    print(
        "Fast charge current:",
        mb.read_holding(HoldingRegisters.FAST_CHARGE_CURRENT),
    )

    print(
        "Charge mode:",
        mb.read_holding(HoldingRegisters.CHARGE_MODE),
    )

    print(
        "Unknown 1642:",
        mb.read_holding(HoldingRegisters.UNKNOWN_1642),
    )

    print("Success!")

finally:
    mb.close()