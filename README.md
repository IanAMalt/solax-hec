# solax-hec

> **IMPORTANT SAFETY WARNING — v0.1.2**
>
> Version **0.1.2 should not be used with a live SolaX HEC charger**. During live testing, the charger stopped charging while the integration using this library was enabled and returned to normal operation when the integration was disabled. A subsequent read-only Home Assistant build operated normally while the charger was charging.
>
> The exact Modbus write responsible has not yet been conclusively identified. Treat the writable register map in v0.1.2 as experimental and unsafe for production use until independently verified.

A Python library for locally controlling and monitoring SolaX Gen2 HEC EV chargers over Modbus TCP.

**Project Status:** 🚧 Active development. The register map is still being reverse engineered.

## Features

### Working / experimentally verified

- Local HTTP authentication
- Modbus TCP communication
- High-level Python API
- Read Fast charge current
- Read live charging current
- Read live charging power
- Read grid voltage
- Read grid frequency
- Reverse engineered register map

### Experimental / currently unsafe

- Set Fast charge current
- Set charge mode

**Do not use the writable controls from v0.1.2 with a live charger.**

## Example

```python
from solax_hec import Charger

charger = Charger("192.168.0.169")
charger.connect()

print(f"Grid Voltage      : {charger.grid_voltage:.2f} V")
print(f"Grid Frequency    : {charger.grid_frequency:.2f} Hz")
print(f"Charging Current  : {charger.charging_current:.2f} A")
print(f"Charging Power    : {charger.charging_power} W")
print(f"Fast Current      : {charger.fast_charge_current:.1f} A")
print(f"Charge Mode       : {charger.charge_mode}")

charger.close()
```

## Confirmed read registers

| Register | Description | Access |
|---------:|-----------------------------------------|:------:|
| 0 | Grid voltage (×100 V) | R |
| 4 | Charging current (×100 A) | R |
| 8 | Charging power (W) | R |
| 12 | Grid frequency (×100 Hz) | R |
| 58 | Charging current (mirror) | R |
| 61 | Charging power (mirror) | R |
| 64 | Charging power (mirror) | R |
| 1640 | Fast charge current (×100 A) | **R only pending verification** |
| 1641 | Charge mode | **R only pending verification** |

## Safety / reverse-engineering policy

Registers are only promoted to writable controls after their address, value encoding, persistence behaviour, and interaction with the HEC charging state machine have been independently verified.

This project communicates directly with a mains-connected EV charger. Experimental writes can affect charging behaviour. Do not assume that a register is safe to write merely because reading it produces a plausible value.

## Disclaimer

This project is not affiliated with or endorsed by SolaX Power.

It is a community reverse engineering effort intended to provide local monitoring and, only where independently verified, control of compatible chargers.
