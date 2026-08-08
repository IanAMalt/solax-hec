from solax_hec import Charger
from solax_hec.registers import HoldingRegisters


HOST = "192.168.0.169"


def main():
    charger = Charger(HOST)

    print("Connecting...")

    if not charger.connect():
        print("Failed to connect.")
        return

    try:
        print(f"Grid voltage       : {charger.grid_voltage:.2f} V")
        print(f"Grid frequency     : {charger.grid_frequency:.2f} Hz")
        print(f"Charging current   : {charger.charging_current:.2f} A")
        print(f"Charging power     : {charger.charging_power} W")
        print(f"Fast charge current: {charger.fast_charge_current:.1f} A")
        print(f"Charge mode        : {charger.charge_mode}")

        raw_mode = charger.modbus.read_holding(
            HoldingRegisters.CHARGE_MODE
        )

        print(f"Charge mode raw    : {raw_mode}")

        print()
        print("Success!")

    finally:
        charger.close()


if __name__ == "__main__":
    main()