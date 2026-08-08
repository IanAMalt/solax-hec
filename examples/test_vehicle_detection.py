"""
Discover which registers change when a vehicle is plugged in.

Run twice:
    1. With no vehicle plugged in.
    2. With a vehicle plugged in.

Compare the results.
"""

from solax_hec.modbus import ModbusConnection

HOST = "192.168.0.169"

mb = ModbusConnection(HOST)

try:
    print("Connecting...")
    mb.connect()

    print(f"{'Dec':>5} {'Hex':>6} {'Value':>8}")
    print("-" * 25)

    for reg in range(1600, 1661):
        try:
            value = mb.read_holding(reg)
            print(f"{reg:5d} 0x{reg:04X} {value:8}")
        except Exception:
            pass

finally:
    mb.close()