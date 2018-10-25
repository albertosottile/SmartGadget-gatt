import gatt
import struct

manager = gatt.DeviceManager(adapter_name='hci0')

class AnyDevice(gatt.Device):
    def services_resolved(self):
        super().services_resolved()

        logger_service = next(
            s for s in self.services
            if s.uuid == '0000f234-b38d-4985-720e-0f993a68ee41')

        newest_characteristic = next(
            c for c in logger_service.characteristics
            if c.uuid == '0000f236-b38d-4985-720e-0f993a68ee41')

        newest_characteristic.read_value()

    def characteristic_value_updated(self, characteristic, value):
        #print(characteristic.uuid)
        value = struct.unpack('<Q', value)[0]
        print("Newest timestamp:", value)


device = AnyDevice(mac_address='E9:28:88:82:2B:E2', manager=manager)
device.connect()

manager.run()
