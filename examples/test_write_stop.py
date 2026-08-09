"""Test writing the HEC charger use mode."""

import time

from solax_hec import Charger
from solax_hec.models import ChargerUseMode


HOST = "192.168.0.169"


def read_mode(charger: Charger) -> ChargerUseMode:
    """Read and return the current charger use mode."""

    mode = charger.charger_use_mode

    print(f"Read back: {mode}")
    print(f"Raw value: {mode.value}")

    return mode


def test_mode(charger: Charger, mode: ChargerUseMode) -> None:
    """Set and verify a charger use mode."""

    print()
    print(f"Setting charger use mode to {mode}...")

    charger.set_charger_use_mode(mode)

    print("Waiting 3 seconds for charger to update...")
    time.sleep(3)

    read_back = read_mode(charger)

    if read_back != mode:
        print(
            f"WARNING: Expected {mode}, "
            f"but charger reported {read_back}"
        )
        return

    print("OK")


def main() -> None:
    """Run the charger use mode write tests."""

    charger = Charger(HOST)

    print("Connecting...")

    if not charger.connect():
        print("Failed to connect.")
        return

    try:
        print("Current charger use mode before test:")
        read_mode(charger)

        test_mode(charger, ChargerUseMode.STOP)

        print()
        print("STOP write test complete.")

        print()
        print("Now testing FAST...")
        test_mode(charger, ChargerUseMode.FAST)

        print()
        print("Charger use mode write test complete.")

    finally:
        charger.close()


if __name__ == "__main__":
    main()