"""
Watch selected SolaX HEC Input Registers.

This tool continuously displays a shortlist of candidate telemetry
registers and highlights any values that change.

Press CTRL+C to stop.
"""

import time
from datetime import datetime

from solax_hec.modbus import ModbusConnection


HOST = "192.168.0.169"
DEVICE_ID = 1

# Candidate telemetry registers
WATCH = [
    0,
    4,
    8,
    11,
    12,
    16,
    27,
    43,
    58,
    61,
    64,
]

REFRESH_SECONDS = 1.0


def clear():
    print("\033[2J\033[H", end="")


def timestamp():
    return datetime.now().strftime("%H:%M:%S")


def main():

    conn = ModbusConnection(HOST, DEVICE_ID)

    print("Connecting...")

    if not conn.connect():
        print("Failed to connect.")
        return

    previous = {}

    try:

        while True:

            values = {}

            for reg in WATCH:
                try:
                    values[reg] = conn.read_input(reg)
                except Exception:
                    values[reg] = None

            clear()

            print("SolaX HEC Input Register Watch")
            print(f"Time: {timestamp()}")
            print()

            print(f"{'Reg':>5} {'Hex':>8} {'Value':>10} {'Δ':>8}")
            print("-" * 36)

            for reg in WATCH:

                value = values[reg]

                if value is None:
                    display = "ERR"
                    delta = ""
                else:
                    display = str(value)

                    if reg not in previous:
                        delta = "-"
                    else:
                        diff = value - previous[reg]

                        if diff == 0:
                            delta = "0"
                        elif diff > 0:
                            delta = f"+{diff}"
                        else:
                            delta = str(diff)

                print(
                    f"{reg:5d} "
                    f"0x{reg:04X} "
                    f"{display:>10} "
                    f"{delta:>8}"
                )

            previous = values.copy()

            time.sleep(REFRESH_SECONDS)

    except KeyboardInterrupt:

        print()
        print("Stopping...")

    finally:

        conn.close()


if __name__ == "__main__":
    main()