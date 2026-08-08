\# solax-hec



A Python library for locally controlling and monitoring SolaX Gen2 HEC EV chargers over Modbus TCP.



> \*\*Project Status:\*\* 🚧 Active development (Core SDK functional)



\---



\## Features



\### Working



\- ✅ Local HTTP authentication

\- ✅ Modbus TCP communication

\- ✅ High-level Python API

\- ✅ Read Fast charge current

\- ✅ Set Fast charge current

\- ✅ Read charge mode

\- ✅ Set charge mode

\- ✅ Read live charging current

\- ✅ Read live charging power

\- ✅ Read grid voltage

\- ✅ Read grid frequency

\- ✅ Reverse engineered register map



\### Planned



\- 🚧 Home Assistant integration

\- 🚧 MQTT support

\- 🚧 Automatic charger discovery

\- 🚧 Async API

\- 🚧 Additional telemetry

\- 🚧 Fault/status reporting



\---



\## Example



```python

from solax\_hec import Charger



charger = Charger("192.168.0.169")



charger.connect()



print(f"Grid Voltage      : {charger.grid\_voltage:.2f} V")

print(f"Grid Frequency    : {charger.grid\_frequency:.2f} Hz")

print(f"Charging Current  : {charger.charging\_current:.2f} A")

print(f"Charging Power    : {charger.charging\_power} W")



print(f"Fast Current      : {charger.fast\_charge\_current:.1f} A")

print(f"Charge Mode       : {charger.charge\_mode}")



charger.close()

```



\---



\## Confirmed Registers



| Register | Description | Access |

|---------:|-----------------------------------------|:------:|

| 0 | Grid voltage (×100 V) | R |

| 4 | Charging current (×100 A) | R |

| 8 | Charging power (W) | R |

| 12 | Grid frequency (×100 Hz) | R |

| 58 | Charging current (mirror) | R |

| 61 | Charging power (mirror) | R |

| 64 | Charging power (mirror) | R |

| 1640 | Fast charge current (×100 A) | RW |

| 1641 | Charge mode (0=Fast, 1=Eco, 2=Green) | RW |



\---



\## Repository Structure



```

docs/

examples/

solax\_hec/

tests/

tools/

```



\---



\## Roadmap



\- \[x] HTTP authentication

\- \[x] Modbus TCP communication

\- \[x] Register discovery

\- \[x] High-level Python client

\- \[ ] Home Assistant integration

\- \[ ] MQTT support

\- \[ ] Additional telemetry

\- \[ ] Documentation

\- \[ ] PyPI package



\---



\## Project Philosophy



This project focuses on providing a clean, well-documented Python SDK for locally controlling and monitoring SolaX Gen2 HEC chargers.



Registers are only marked as \*\*confirmed\*\* after they have been experimentally verified under multiple real-world operating conditions. Reverse engineering continues, but stability and correctness take priority over exposing undocumented functionality.



\---



\## Disclaimer



This project is not affiliated with or endorsed by SolaX Power.



It is a community reverse engineering effort intended to provide local control and monitoring of compatible chargers.

