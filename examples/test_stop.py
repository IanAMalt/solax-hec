"""Read the HEC charger use mode register."""

from solax_hec import Charger


HOST = "192.168.0.169"

CHARGER_USE_MODE_REGISTER = 1549


def main() -> None:
    """Read the charger use mode."""

    charger = Charger(HOST)

    print("Connecting...")

    if not charger.connect():
        print("Failed to connect.")
        return

    try:
        value = charger.modbus.read_holding(
            CHARGER_USE_MODE_REGISTER
        )

        print()
        print("Charger Use Mode")
        print("-----------------")
        print(f"Register : {CHARGER_USE_MODE_REGISTER}")
        print(f"Hex      : 0x{CHARGER_USE_MODE_REGISTER:03X}")
        print(f"Raw value: {value}")

    finally:
        charger.close()


if __name__ == "__main__":
    main()
