"""
Simple example demonstrating the high-level Charger API.

Run from the project root with:

    python -m examples.test_modbus
"""

from solax_hec.client import Charger
from solax_hec.registers import HoldingRegisters

HOST = "192.168.0.169"

charger = Charger(HOST)

try:
    print("Connecting...")
    charger.connect()

    print(
        "Fast charge current:",
        charger.modbus.read_holding(HoldingRegisters.FAST_CHARGE_CURRENT),
    )

    print(
        "Charge mode:",
        charger.modbus.read_holding(HoldingRegisters.CHARGE_MODE),
    )

    print(
        "Unknown 1642:",
        charger.modbus.read_holding(HoldingRegisters.UNKNOWN_1642),
    )

    print("Success!")

finally:
    charger.close()