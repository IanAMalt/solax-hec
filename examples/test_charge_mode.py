"""
Simple example demonstrating reading and writing the charger mode.

Run from the project root with:

    python -m examples.test_charge_mode
"""

from solax_hec.client import Charger
from solax_hec.models import ChargeMode

HOST = "192.168.0.169"

charger = Charger(HOST)

try:
    print("Connecting...")
    charger.connect()

    current_mode = charger.charge_mode
    print(f"Current mode : {current_mode}")

    print("Writing the same mode back...")
    charger.set_charge_mode(current_mode)

    print("Reading it again...")
    print(f"Current mode : {charger.charge_mode}")

    print("Success!")

finally:
    charger.close()