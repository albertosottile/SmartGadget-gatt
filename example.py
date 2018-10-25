import smartgadget

sm = smartgadget.SmartGadget(adapter_name='hci0', device_mac='E9:28:88:82:2B:E2')

print("SmartGadget: Temperature (°C): %.1f -  Humidity (%%): %.0f - Dew point (°C): %.1f" % (sm.temperature(), sm.humidity(), sm.dew()))
