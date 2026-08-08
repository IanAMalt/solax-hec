"""
Analyse multiple SolaX input register snapshots.

Each CSV should have two columns:

Register,Value

Example:

python tools/analyse_snapshots.py \
    input_waiting.csv \
    input_charging.csv \
    input_charging_fast.csv \
    input_charging_fast_16.csv \
    input_chargin_eco.csv
"""

import csv
import os
import sys


def load_csv(filename):
    data = {}

    with open(filename, newline="") as f:
        reader = csv.reader(f)

        # Skip header if present
        first = next(reader)

        try:
            int(first[0])
            data[int(first[0])] = int(first[1])
        except ValueError:
            pass

        for row in reader:
            if len(row) < 2:
                continue

            try:
                reg = int(row[0])
                value = int(row[1])
                data[reg] = value
            except ValueError:
                continue

    return data


def main():

    if len(sys.argv) < 3:
        print("Usage:")
        print("python analyse_snapshots.py file1.csv file2.csv [...]")
        return

    snapshots = []

    for filename in sys.argv[1:]:
        snapshots.append(
            (
                os.path.basename(filename),
                load_csv(filename),
            )
        )

    registers = sorted(
        set().union(*(d.keys() for _, d in snapshots))
    )

    headers = ["Register"] + [name for name, _ in snapshots]

    widths = [10] + [18] * (len(headers) - 1)

    for h, w in zip(headers, widths):
        print(f"{h:<{w}}", end="")
    print()

    print("-" * sum(widths))

    interesting = 0

    for reg in registers:

        values = []

        for _, data in snapshots:
            values.append(data.get(reg, ""))

        if len(set(values)) == 1:
            continue

        interesting += 1

        print(f"{reg:<10}", end="")

        for value in values:
            print(f"{str(value):<{18}}", end="")

        print()

    print()
    print(f"Interesting registers: {interesting}")


if __name__ == "__main__":
    main()