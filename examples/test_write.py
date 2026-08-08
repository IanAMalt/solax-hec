from solax_hec.client import Charger

HOST = "192.168.0.169"

charger = Charger(HOST)

try:
    print("Connecting...")
    charger.connect()

    current = charger.fast_charge_current
    print(f"Current setting : {current:.1f} A")

    print("Writing the same value back...")
    charger.set_fast_charge_current(current)

    print("Reading it again...")
    print(f"Current setting : {charger.fast_charge_current:.1f} A")

    print("Success!")

finally:
    charger.close()