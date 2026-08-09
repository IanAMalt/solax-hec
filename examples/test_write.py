"""Test writing and reading SolaX HEC charging modes."""

from solax_hec import Charger
from solax_hec.models import ChargeMode


HOST = "192.168.0.169"


def test_mode(charger: Charger, mode: ChargeMode) -> None:
    """Write and verify a charging mode."""

    print(f"Setting charge mode to {mode}...")

    charger.set_charge_mode(mode)

    actual = charger.charge_mode

    print(f"Read back: {actual}")

    if actual != mode:
        raise RuntimeError(
            f"Expected {mode} but charger returned {actual}"
        )

    print("OK")
    print()


def main() -> None:
    """Run charging-mode write tests."""

    charger = Charger(HOST)

    print("Connecting...")

    if not charger.connect():
        print("Failed to connect.")
        return

    try:
        print(f"Charge mode before tests: {charger.charge_mode}")
        print()

        test_mode(charger, ChargeMode.FAST)
        test_mode(charger, ChargeMode.ECO)
        test_mode(charger, ChargeMode.GREEN)
        test_mode(charger, ChargeMode.FAST)

        print("All charge mode write tests passed!")

    finally:
        charger.close()


if __name__ == "__main__":
    main()