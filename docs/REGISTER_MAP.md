\# SolaX HEC Register Map



This document records the current understanding of the SolaX Gen2 HEC Modbus register map.



Only registers that have been experimentally verified under multiple real-world operating conditions are marked as \*\*Confirmed\*\*.



\---



\# Confirmed Input Registers



These registers provide live telemetry from the charger.



| Register | Hex | Description | Units | Access | Status |

|---------:|:---:|-------------|------:|:------:|:------:|

| 0 | 0x0000 | Grid Voltage | ×100 V | R | ✅ Confirmed |

| 4 | 0x0004 | Charging Current | ×100 A | R | ✅ Confirmed |

| 8 | 0x0008 | Charging Power | W | R | ✅ Confirmed |

| 12 | 0x000C | Grid Frequency | ×100 Hz | R | ✅ Confirmed |



\---



\# Confirmed Holding Registers



These registers control charger configuration.



| Register | Hex | Description | Units | Access | Status |

|---------:|:---:|-------------|------:|:------:|:------:|

| 1640 | 0x0668 | Fast Charge Current | ×100 A | RW | ✅ Confirmed |

| 1641 | 0x0669 | Charge Mode | Enum | RW | ✅ Confirmed |



Charge Mode values:



| Value | Mode |

|------:|------|

| 0 | Fast |

| 1 | Eco |

| 2 | Green |

| 3 | Stop \*(currently believed, requires final confirmation)\* |



\---



\# Confirmed Mirror Registers



These registers appear to duplicate confirmed telemetry values.



| Register | Mirrors | Notes |

|---------:|---------|-------|

| 11 | Charging Power | Mirrors Register 8 |

| 58 | Charging Current | Mirrors Register 4 |

| 61 | Charging Power | Mirrors Register 8 |

| 64 | Charging Power | Mirrors Register 8 |



These are currently retained for documentation purposes only. The Python API uses the primary register for each measurement.



\---



\# Registers of Interest



These registers consistently change during charging but have not yet been positively identified.



| Register | Notes |

|---------:|-------|

| 27 | Scales proportionally with charging load. Purpose currently unknown. |

| 43 | Continuously increasing value. Appears to be a counter or timer. |



\---



\# Validation



The confirmed telemetry registers have been verified during multiple operating conditions, including:



\- Vehicle connected (idle)

\- Vehicle charging

\- Approximately 6 A charging

\- Approximately 8 A charging

\- Approximately 12 A charging

\- Approximately 13 A charging

\- Approximately 16 A charging

\- Approximately 18 A charging



Validation was performed by comparing live charger behaviour against Modbus telemetry while changing the configured charging current and allowing the charger to stabilise after each change.



\---



\# Design Philosophy



This project intentionally separates \*\*confirmed knowledge\*\* from \*\*ongoing reverse engineering\*\*.



A register is only promoted to \*\*Confirmed\*\* after repeated experimental verification.



Candidate or speculative registers should remain documented in the `docs/experiments/` directory until sufficient evidence exists to promote them into this document.



This approach keeps the public API stable while allowing reverse engineering to continue independently.

