\# SolaX HEC Register Map



This document records the current understanding of the SolaX HEC Modbus register map.



It is based on reverse engineering performed against a real 7.2 kW SolaX HEC charger.



\## Register Status



| Status | Meaning |

|--------|---------|

| ✅ | Confirmed by testing on real hardware |

| 🟡 | Strong hypothesis based on observed behaviour |

| ❓ | Unknown purpose |



\---



\# Holding Registers



| Register | Constant | Type | Status | Description | Notes |

|---------:|----------|------|:------:|-------------|-------|

| 1600 | CHARGER\_STATUS | uint16 | ❓ | Charger status | Observed value: 70 while charging |

| 1601 | UNKNOWN\_1601 | uint16 | ❓ | Unknown | |

| 1602 | UNKNOWN\_1602 | uint16 | ❓ | Unknown | |

| 1603 | CHARGER\_RATED\_POWER | uint16 | 🟡 | Rated charger power | 7200 on a 7.2 kW charger |

| 1604 | UNKNOWN\_1604 | uint16 | ❓ | Unknown | |

| 1605 | UNKNOWN\_1605 | uint16 | ❓ | Unknown | Observed value: 4 |

| 1606 | UNKNOWN\_1606 | uint16 | ❓ | Unknown | |

| 1607 | UNKNOWN\_1607 | uint16 | ❓ | Unknown | |

| 1608 | UNKNOWN\_1608 | uint16 | ❓ | Unknown | |

| 1609 | UNKNOWN\_1609 | uint16 | ❓ | Unknown | |

| 1610 | UNKNOWN\_1610 | uint16 | ❓ | Unknown | |

| 1611 | UNKNOWN\_1611 | uint16 | ❓ | Unknown | |

| 1612 | UNKNOWN\_1612 | uint16 | ❓ | Unknown | Observed value: 4 |

| 1613 | UNKNOWN\_1613 | uint16 | ❓ | Unknown | |

| 1614 | UNKNOWN\_1614 | uint16 | ❓ | Unknown | |

| 1615 | FAST\_CHARGE\_CURRENT\_SHADOW | uint16 | 🟡 | Mirrors fast charge current | Observed value: 3200 |

| 1616 | UNKNOWN\_1616 | uint16 | ❓ | Unknown | |

| 1617 | UNKNOWN\_1617 | uint16 | ❓ | Unknown | |

| 1618 | UNKNOWN\_1618 | uint16 | ❓ | Unknown | |

| 1619 | UNKNOWN\_1619 | uint16 | ❓ | Unknown | |

| 1620 | UNKNOWN\_1620 | uint16 | ❓ | Unknown | |

| 1621 | UNKNOWN\_1621 | uint16 | ❓ | Unknown | |

| 1622 | UNKNOWN\_1622 | uint16 | ❓ | Unknown | |

| 1623 | UNKNOWN\_1623 | uint16 | ❓ | Unknown | |

| 1624 | UNKNOWN\_1624 | uint16 | ❓ | Unknown | |

| 1625 | UNKNOWN\_1625 | uint16 | ❓ | Unknown | |

| 1626 | UNKNOWN\_1626 | uint16 | ❓ | Unknown | |

| 1627 | UNKNOWN\_1627 | uint16 | ❓ | Unknown | |

| 1628 | UNKNOWN\_1628 | uint16 | ❓ | Unknown | |

| 1629 | UNKNOWN\_1629 | uint16 | ❓ | Unknown | |

| 1630 | UNKNOWN\_1630 | uint16 | ❓ | Unknown | |

| 1631 | UNKNOWN\_1631 | uint16 | ❓ | Unknown | |

| 1632 | UNKNOWN\_1632 | uint16 | ❓ | Unknown | |

| 1633 | UNKNOWN\_1633 | uint16 | ❓ | Unknown | |

| 1634 | UNKNOWN\_1634 | uint16 | ❓ | Boolean flag | Value 1 while charging |

| 1635 | UNKNOWN\_1635 | uint16 | ❓ | Unknown | |

| 1636 | UNKNOWN\_1636 | uint16 | ❓ | Boolean flag | Value 1 while charging |

| 1637 | UNKNOWN\_1637 | uint16 | ❓ | Unknown | |

| 1638 | UNKNOWN\_1638 | uint16 | ❓ | Unknown | |

| 1639 | UNKNOWN\_1639 | uint16 | ❓ | Unknown | |

| 1640 | FAST\_CHARGE\_CURRENT | uint16 | ✅ | Fast charge current | Read/write. Stored as current ×100 |

| 1641 | CHARGE\_MODE | enum | ✅ | Charger operating mode | 0 = Fast, 1 = Eco |

| 1642 | UNKNOWN\_1642 | uint16 | ❓ | Unknown | |

| 1643 | UNKNOWN\_1643 | uint16 | ❓ | Unknown | |

| 1644 | UNKNOWN\_1644 | uint16 | ❓ | Boolean flag | Value 1 while charging |

| 1645 | UNKNOWN\_1645 | uint16 | ❓ | Boolean flag | Value 1 while charging |

| 1646 | UNKNOWN\_1646 | uint16 | ❓ | Unknown | |

| 1647 | UNKNOWN\_1647 | uint16 | ❓ | Unknown | |

| 1648 | UNKNOWN\_1648 | uint16 | ❓ | Status code | Observed value: 3 while charging |

| 1649 | UNKNOWN\_1649 | uint16 | ❓ | Unknown | |

| 1650 | UNKNOWN\_1650 | uint16 | ❓ | Percentage? | Observed value: 100 |

| 1651 | UNKNOWN\_1651 | uint16 | ❓ | Unknown | |

| 1652 | UNKNOWN\_1652 | uint16 | ❓ | Unknown | |

| 1653 | UNKNOWN\_1653 | uint16 | ❓ | State code | Observed value: 5 while charging |

| 1654 | UNKNOWN\_1654 | uint16 | ❓ | Unknown | |

| 1655 | UNKNOWN\_1655 | uint16 | ❓ | Status code | Observed value: 3 |

| 1656 | UNKNOWN\_1656 | uint16 | ❓ | Unknown | Observed value: 12601 |

| 1657 | UNKNOWN\_1657 | uint16 | ❓ | Unknown | Observed value: 12846 |

| 1658 | UNKNOWN\_1658 | uint16 | ❓ | Unknown | Observed value: 12598 |

| 1659 | UNKNOWN\_1659 | uint16 | ❓ | Unknown | Observed value: 14382 |

| 1660 | UNKNOWN\_1660 | uint16 | ❓ | Unknown | Observed value: 12334 |



\---



\# Confirmed Behaviour



\## Register 1640 – Fast Charge Current



\*\*Status:\*\* ✅ Confirmed



\- Read/write

\- Stored as amps × 100



Examples:



| Register Value | Current |

|--------------:|--------:|

| 600 | 6.00 A |

| 1600 | 16.00 A |

| 3200 | 32.00 A |



\---



\## Register 1641 – Charge Mode



\*\*Status:\*\* ✅ Confirmed



| Value | Mode |

|------:|------|

| 0 | Fast |

| 1 | Eco |



Read/write verified on real hardware.



\---



\# Test Platform



Testing performed using:



\- SolaX HEC 7.2 kW charger

\- Modbus TCP

\- Python 3.10

\- pymodbus

\- Firmware version: \*(to be recorded)\*



\---



\# Future Investigation



\## High Priority



\- Vehicle connected

\- Charging active

\- Cable locked

\- Charger state

\- Fault codes

\- Session energy

\- Grid voltage

\- Grid current

\- Power

\- Temperature



\## Medium Priority



\- Firmware version

\- Serial number

\- Hardware revision

\- Uptime



\## Low Priority



\- Manufacturing information

\- Diagnostic counters

\- Reserved registers



\---



\# Changelog



\## 2026-08-08



\### Confirmed



\- Register 1640 – Fast charge current

\- Register 1641 – Charge mode



\### Strong hypotheses



\- Register 1603 – Rated charger power

\- Register 1615 – Shadow copy of fast charge current



\### Unknown



Remaining registers are under active investigation.

