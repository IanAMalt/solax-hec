\# SolaX HEC Python API



This document describes the intended public API of the library.



It is a design target rather than a description of the current implementation.



\---



\# Creating a charger



```python

from solax\_hec import Charger



charger = Charger("192.168.0.169")



charger.connect()

```



\---



\# Reading configuration



```python

charger.fast\_charge\_current

charger.charge\_mode

```



Example:



```python

print(charger.fast\_charge\_current)

\# 32.0



print(charger.charge\_mode)

\# ChargeMode.FAST

```



\---



\# Changing configuration



```python

charger.set\_fast\_charge\_current(16)



charger.set\_charge\_mode(ChargeMode.ECO)

```



\---



\# Charger status



```python

charger.is\_vehicle\_connected



charger.is\_charging



charger.is\_faulted



charger.status

```



\---



\# Grid information



```python

charger.grid\_voltage



charger.grid\_frequency



charger.grid\_power

```



\---



\# Charging session



```python

charger.session\_energy



charger.session\_duration



charger.vehicle\_soc

```



\---



\# Device information



```python

charger.serial\_number



charger.model



charger.firmware\_version



charger.hardware\_version

```



\---



\# Control



```python

charger.start\_charge()



charger.stop\_charge()



charger.reboot()

```



\---



\# Diagnostics



```python

charger.last\_error



charger.temperature



charger.uptime

```



\---



\# Future features



\- HTTP authentication

\- Automatic charger discovery

\- Firmware update support

\- Event callbacks

\- Home Assistant integration

\- Async API

\- MQTT bridge

