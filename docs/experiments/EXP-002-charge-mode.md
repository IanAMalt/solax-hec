\# EXP-002 – Charge Mode



\## Objective



Determine how the charger stores the configured charging mode.



\---



\## Hardware



\- Charger: SolaX HEC 7.2 kW

\- Interface: Modbus TCP



\---



\## Registers Investigated



| Register | Purpose |

|----------|---------|

| 1641 | Candidate charge mode register |



\---



\## Procedure



1\. Read register 1641.

2\. Change charger mode.

3\. Read register again.

4\. Write values via Modbus.

5\. Confirm charger changes mode.

6\. Read register again.



\---



\## Results



| Value | Mode |

|------:|------|

| 0 | Fast |

| 1 | Eco |



\---



\## Verification



\### Read



Verified.



\### Write



Verified.



\---



\## Conclusion



Register \*\*1641\*\* stores the charger operating mode.



It is a read/write holding register.



Status:



\*\*CONFIRMED\*\*

