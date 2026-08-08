\# EXP-001 – Fast Charge Current



\## Objective



Determine which Modbus register stores the configured Fast charging current.



\---



\## Hardware



\- Charger: SolaX HEC 7.2 kW

\- Interface: Modbus TCP

\- Library: pymodbus



\---



\## Registers Investigated



| Register | Purpose |

|----------|---------|

| 1640 | Candidate fast charge current register |



\---



\## Procedure



1\. Read register 1640.

2\. Change Fast charge current from the charger.

3\. Read register 1640 again.

4\. Change the current using Modbus.

5\. Confirm the charger reflects the new value.

6\. Read register again.



\---



\## Results



| Register | Value | Meaning |

|----------|------:|---------|

| 1640 | 3200 | 32.00 A |



Observed scaling:



```

Stored value = Amps × 100

```



Examples:



| Register | Current |

|----------|---------|

| 600 | 6.00 A |

| 1600 | 16.00 A |

| 3200 | 32.00 A |



\---



\## Verification



\### Read



Verified.



\### Write



Verified.



\### Scaling



Verified.



\---



\## Conclusion



Register \*\*1640\*\* stores the configured Fast charging current.



It is a read/write holding register.



Values are stored as \*\*amps ×100\*\*.



Status:



\*\*CONFIRMED\*\*

