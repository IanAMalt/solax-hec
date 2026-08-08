"""
Simple example demonstrating the high-level Charger API.

Run from the project root with:

    python -m examples.test_modbus
"""

from solax_hec.client import Charger

HOST = "192.168.0.169"

charger = Charger(HOST)

try:
    print("Connecting...")
    charger.connect()

    print(f"Fast charge current : {charger.fast_charge_current:.1f} A")
    print(f"Charge mode         : {charger.charge_mode}")

    print("Success!")

finally:
    charger.close()