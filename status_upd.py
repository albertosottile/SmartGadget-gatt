import gatt
import math
import struct

manager = gatt.DeviceManager(adapter_name='hci0')

t_uuid = '00002235-b38d-4985-720e-0f993a68ee41'
h_uuid = '00001235-b38d-4985-720e-0f993a68ee41'

class AnyDevice(gatt.Device):
    t_value = 0
    h_value = 0

    def services_resolved(self):
        super().services_resolved()

        for s in self.services:
            if s.uuid =='00002234-b38d-4985-720e-0f993a68ee41':
                temperature_service = s
            elif s.uuid == '00001234-b38d-4985-720e-0f993a68ee41':
                humidity_service = s

        temperature_characteristic = next(
            c for c in temperature_service.characteristics
            if c.uuid == t_uuid)

        humidity_characteristic = next(
            c for c in humidity_service.characteristics
            if c.uuid == h_uuid)

        temperature_characteristic.enable_notifications()
        humidity_characteristic.enable_notifications()

    def dew_point(self, temp, hum):
        a = 6.105
        b = 17.27
        c = 237.7
        gamma = math.log(hum / 100) + (b * temp)/(c + temp)
        return (c * gamma)/(b - gamma) 

    def characteristic_enable_notification_succedeed(self, characteristic):
        print("Subscription to change notifications - SUCCESS")

    def characteristic_enable_notification_failed(self, characteristic):
        print("Subscription to change notifications - FAIL!")

    def characteristic_value_updated(self, characteristic, value):
        value = round(struct.unpack('<f', value)[0], 1)
        if characteristic.uuid == t_uuid:
            #print("Temperature (C):", value)
            self.t_value = value
        elif characteristic.uuid == h_uuid:
            self.h_value = value
            print("Temperature (C): %.1f -  Humidity (%%): %.0f - Dew point (C): %.1f" % (self.t_value, self.h_value, self.dew_point(self.t_value, self.h_value)))


device = AnyDevice(mac_address='E9:28:88:82:2B:E2', manager=manager)
device.connect()

manager.run()
