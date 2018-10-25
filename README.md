# SmartGadget-GATT
This module uses the [Bluetooth GATT SDK](https://github.com/getsenic/gatt-python) to retrieve data from a [Sensirion SHT31 SmartGadget](https://www.sensirion.com/en/environmental-sensors/humidity-sensors/development-kit/) Development Kit. 

This sensor measures temperature and humidity in a room, and communicates using Bluetooth LE (SMART, Bluetooth 4.0).

Requirements:
- Python 3.4+
- [Bluetooth GATT SDK for Python](https://github.com/getsenic/gatt-python)
- a Bluetooth LE (4.0) enabled adapter

Usage: 
```python
import smartgadget

sm = smartgadget.SmartGadget(adapter_name='hci0', device_mac='E9:28:88:82:2B:E2')

print("SmartGadget: Temperature (°C): %.1f" % (sm.temperature())
print("SmartGadget: Humidity (%%): %.0f" % (sm.humidity())
print("SmartGadget Dew point (°C): %.1f" % (sm.dew()))
```

See the documentation of the Bluetooth GATT SDK for info about device scanning and how to get the MAC address of the sensor.
Tested on a Raspberry Pi Model 3 with Raspbian 9.
See the gatt-examples folder for further details and low-level code. 

Credits to the manufacturer code:
- https://github.com/Sensirion/SmartGadget-iOS
- https://github.com/Sensirion/SmartGadget-Firmware
