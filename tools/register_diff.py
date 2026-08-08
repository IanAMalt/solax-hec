#!/usr/bin/env python3
"""
Register snapshot and diff tool for SolaX HEC chargers.

Usage:

Take a snapshot:
    python tools/register_diff.py snapshot before.json

Take another:
    python tools/register_diff.py snapshot after.json

Compare:
    python tools/register_diff.py diff before.json after.json
"""

import json
import sys

from solax_hec.modbus import ModbusConnection

HOST = "192.168.0.169"


def take_snapshot(filename):
    mb = ModbusConnection(HOST)

    try:
        print("Connecting...")
        mb.connect()

        data = {}

        for reg in range(1600, 1661):
            try:
                data[reg] = mb.read_holding(reg)
            except Exception:
                data[reg] = None

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Saved {filename}")

    finally:
        mb.close()


def diff(before_file, after_file):
    with open(before_file) as f:
        before = json.load(f)

    with open(after_file) as f:
        after = json.load(f)

    print()
    print("Changed registers")
    print("-----------------")

    changes = 0

    for reg in sorted(before.keys(), key=int):
        if before[reg] != after[reg]:
            print(
                f"{reg}: {before[reg]} -> {after[reg]}"
            )
            changes += 1

    if changes == 0:
        print("No changes.")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return

    command = sys.argv[1]

    if command == "snapshot":
        take_snapshot(sys.argv[2])

    elif command == "diff":
        diff(sys.argv[2], sys.argv[3])

    else:
        print(__doc__)


if __name__ == "__main__":
    main()