\# Input Register Analysis



This section documents the current understanding of the SolaX HEC \*\*Input Registers\*\*.



Unlike the Holding Registers, these appear to contain \*\*live telemetry\*\* rather than configuration.



Status values are based on comparison of multiple captures under different operating conditions:



\- Waiting (vehicle connected, not charging)

\- Charging

\- Fast Charging (32 A)

\- Fast Charging (16 A)

\- Eco Charging



\---



\# Confidence Levels



| Status | Meaning |

|---------|---------|

| ✅ | Confirmed by experiment |

| 🟢 | Very strong hypothesis |

| 🟡 | Strong hypothesis |

| ❓ | Unknown |



\---



\# Telemetry Groups



\## Group A – Grid Voltage



| Property | Value |

|----------|------|

| Primary Register | 0 |

| Mirror Register | 1281 |

| Status | 🟢 |

| Scaling | ÷100 |

| Candidate Name | GRID\_VOLTAGE |



\### Evidence



| Waiting | Charging | Fast 32A | Fast 16A | Eco |

|---------:|---------:|----------:|----------:|----:|

|23586|23500|23290|23355|23400|



Interpreted values:



| Waiting | Charging | Fast 32A | Fast 16A | Eco |

|---------:|---------:|----------:|----------:|----:|

|235.86 V|235.00 V|232.90 V|233.55 V|234.00 V|



\### Assessment



Behaviour is entirely consistent with UK mains voltage reducing under increasing load.



\---



\## Group B – Grid Frequency



| Property | Value |

|----------|------|

| Primary Register | 12 |

| Mirror Register | None observed |

| Status | 🟢 |

| Scaling | ÷100 |

| Candidate Name | GRID\_FREQUENCY |



\### Evidence



| Waiting | Charging | Fast 32A | Fast 16A | Eco |

|---------:|---------:|----------:|----------:|----:|

|4986|4984|4996|4992|4994|



Interpreted values:



49.86 Hz



49.84 Hz



49.96 Hz



49.92 Hz



49.94 Hz



\### Assessment



Values remain close to nominal UK mains frequency under all operating conditions.



\---



\## Group C – Dynamic Measurement A



| Property | Value |

|----------|------|

| Primary Register | 4 |

| Mirrors | 58, 1285 |

| Status | 🟡 |

| Candidate Name | UNKNOWN\_DYNAMIC\_A |



\### Evidence



| Waiting | Charging | Fast 32A | Fast 16A | Eco |

|---------:|---------:|----------:|----------:|----:|

|0|610|2018|1610|608|



\### Assessment



Strong correlation with charging activity.



Not yet identified.



Possible candidates:



\- Charging power

\- Requested power

\- Output current

\- PWM related measurement



Further validation required.



\---



\## Group D – Dynamic Measurement B



| Property | Value |

|----------|------|

| Primary Register | 8 |

| Mirrors | 11, 61, 64, 256, 1289, 1292, 2305, 2308 |

| Status | 🟡 |

| Candidate Name | UNKNOWN\_DYNAMIC\_B |



\### Evidence



| Waiting | Charging | Fast 32A | Fast 16A | Eco |

|---------:|---------:|----------:|----------:|----:|

|0|1425|4687|3769|1422|



\### Assessment



Very strong correlation with charging activity.



Likely represents an important live measurement.



Relationship to Group C not yet understood.



\---



\## Group E – Dynamic Measurement C



| Property | Value |

|----------|------|

| Primary Register | 16 |

| Mirror Register |1303|

| Status | 🟡 |

| Candidate Name | UNKNOWN\_DYNAMIC\_C |



\### Evidence



| Waiting | Charging | Fast 32A | Fast 16A | Eco |

|---------:|---------:|----------:|----------:|----:|

|423|423|426|429|428|



\### Assessment



Small variation.



Possibly temperature, duty cycle or another slowly changing analogue measurement.



\---



\## Group F – Unknown Scaled Measurement



| Property | Value |

|----------|------|

| Primary Register |27|

| Status |🟡|

| Candidate Name |UNKNOWN\_SCALED|



\### Evidence



| Waiting | Charging | Fast 32A | Fast 16A | Eco |

|---------:|---------:|----------:|----------:|----:|

|1000|100|333|266|100|



\### Assessment



Clearly scaled.



Meaning unknown.



\---



\## Group G – Unknown Counter



| Property | Value |

|----------|------|

| Primary Register |43|

| Status |❓|

| Candidate Name |UNKNOWN\_COUNTER|



\### Evidence



| Waiting | Charging | Fast 32A | Fast 16A | Eco |

|---------:|---------:|----------:|----------:|----:|

|1568|42|857|1207|969|



Assessment currently inconclusive.



\---



\# Mirror Groups



The following register groups appear to contain duplicate or mirrored measurements.



| Primary | Mirrors |

|----------|---------|

|0|1281|

|4|58,1285|

|8|11,61,64,256,1289,1292,2305,2308|

|16|1303|



These should be treated as a single logical measurement until evidence suggests otherwise.



\---



\# Outstanding Validation



Before promoting any hypothesis to the public API:



\- Verify scaling against independent measurements.

\- Correlate with Home Assistant values.

\- Correlate with charger LCD/app values.

\- Confirm behaviour across multiple charging currents.

\- Confirm behaviour after firmware updates.



Only then should a register be promoted to \*\*Confirmed\*\*.

