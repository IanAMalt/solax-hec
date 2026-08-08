# solax-hec API

This document describes the public Python API exposed by the `solax-hec` library.

---

# Charger

The primary interface is the `Charger` class.

```python
from solax_hec import Charger

charger = Charger("192.168.0.169")
charger.connect()

# Use the API...

charger.close()
```

---

# Configuration

## fast_charge_current

Returns the configured Fast charging current.

**Type**

```python
float
```

**Units**

```
Amps
```

### Read

```python
charger.fast_charge_current
```

### Write

```python
charger.set_fast_charge_current(16)
```

Valid range:

```
6 A – 32 A
```

---

## charge_mode

Returns the configured charging mode.

**Type**

```python
ChargeMode
```

### Read

```python
charger.charge_mode
```

### Write

```python
from solax_hec.models import ChargeMode

charger.set_charge_mode(ChargeMode.FAST)
```

Supported modes:

- Fast
- Eco
- Green
- Stop

---

# Live Telemetry

## grid_voltage

Current measured grid voltage.

**Type**

```python
float
```

**Units**

```
Volts
```

Example:

```python
charger.grid_voltage
```

---

## grid_frequency

Current measured grid frequency.

**Type**

```python
float
```

**Units**

```
Hz
```

Example:

```python
charger.grid_frequency
```

---

## charging_current

Current charging current.

**Type**

```python
float
```

**Units**

```
Amps
```

Example:

```python
charger.charging_current
```

---

## charging_power

Current charging power.

**Type**

```python
int
```

**Units**

```
Watts
```

Example:

```python
charger.charging_power
```

---

# Typical Example

```python
from solax_hec import Charger

charger = Charger("192.168.0.169")

charger.connect()

print(f"Voltage : {charger.grid_voltage:.2f} V")
print(f"Frequency : {charger.grid_frequency:.2f} Hz")
print(f"Current : {charger.charging_current:.2f} A")
print(f"Power : {charger.charging_power} W")

print(f"Mode : {charger.charge_mode}")
print(f"Fast Limit : {charger.fast_charge_current:.1f} A")

charger.close()
```

---

# Stability

The following API is considered stable:

- `fast_charge_current`
- `set_fast_charge_current()`
- `charge_mode`
- `set_charge_mode()`
- `grid_voltage`
- `grid_frequency`
- `charging_current`
- `charging_power`

Additional telemetry may be added in future releases as more registers are experimentally verified.

