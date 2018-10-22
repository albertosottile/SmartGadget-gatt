import gatt
import struct

manager = gatt.DeviceManager(adapter_name='hci0')

class AnyDevice(gatt.Device):
    def services_resolved(self):
        super().services_resolved()

        temperature_service = next(
            s for s in self.services
            if s.uuid == '00002234-b38d-4985-720e-0f993a68ee41')

        temperature_characteristic = next(
            c for c in temperature_service.characteristics
            if c.uuid == '00002235-b38d-4985-720e-0f993a68ee41')

        temperature_characteristic.enable_notifications()

    def characteristic_enable_notification_succedeed(self, characteristic):
        print("Subscription to change notifications - SUCCESS")

    def characteristic_enable_notification_failed(self, characteristic):
        print("Subscription to change notifications - FAIL!")

    def characteristic_value_updated(self, characteristic, value):
        temp_value = round(struct.unpack('<f', value)[0], 2)
        print("Temperature:", temp_value)

device = AnyDevice(mac_address='E9:28:88:82:2B:E2', manager=manager)
device.connect()

manager.run()
