import gatt
import logging
import math
import struct

class SmartGadget:
    def __init__(self, adapter_name, device_mac):
        self.manager = gatt.DeviceManager(adapter_name)
        self.device_mac = device_mac
        self._connect()

    def _connect(self):
        self.device = AnyDevice(mac_address=self.device_mac, manager=self.manager)
        self.device.connect()
        self.manager.run()

    def temperature(self):
        return round(self.device.read_temp(), 1)

    def humidity(self):
        return round(self.device.read_hum(), 0)

    def dew(self):
        return round(self.device.dew_point(), 1)

    def update(self):
        self._connect()

class AnyDevice(gatt.Device):
    t_value = 0
    h_value = 0
    t_uuid = '00002235-b38d-4985-720e-0f993a68ee41'
    h_uuid = '00001235-b38d-4985-720e-0f993a68ee41'

    def connect_succeeded(self):
        super().connect_succeeded()
        logging.debug("[%s] Connected" % (self.mac_address))

    def connect_failed(self, error):
        super().connect_failed(error)
        logging.debug("[%s] Connection failed: %s" % (self.mac_address, str(error)))

    def disconnect_succeeded(self):
        super().disconnect_succeeded()
        logging.debug("[%s] Disconnected" % (self.mac_address))
        self.manager.stop()

    def services_resolved(self):
        super().services_resolved()

        for s in self.services:
            if s.uuid =='00002234-b38d-4985-720e-0f993a68ee41':
                temperature_service = s
            elif s.uuid == '00001234-b38d-4985-720e-0f993a68ee41':
                humidity_service = s

        temperature_characteristic = next(
            c for c in temperature_service.characteristics
            if c.uuid == self.t_uuid)

        humidity_characteristic = next(
            c for c in humidity_service.characteristics
            if c.uuid == self.h_uuid)

        temperature_characteristic.read_value()
        humidity_characteristic.read_value()

    def dew_point(self):
        a = 6.105
        b = 17.27
        c = 237.7
        gamma = math.log(self.h_value / 100) + (b * self.t_value)/(c + self.t_value)
        return (c * gamma)/(b - gamma)

    def characteristic_value_updated(self, characteristic, value):
        value = round(struct.unpack('<f', value)[0], 2)
        if characteristic.uuid == self.t_uuid:
            #print("Temperature (C):", value)
            self.t_value = value
        elif characteristic.uuid == self.h_uuid:
            self.h_value = value
            logging.debug("[%s] Temperature (°C): %.1f -  Humidity (%%): %.0f - Dew point (°C): %.1f" % (self.mac_address, self.t_value, self.h_value, self.dew_point()))
            self.disconnect()

    def read_temp(self):
        return self.t_value

    def read_hum(self):
        return self.h_value

