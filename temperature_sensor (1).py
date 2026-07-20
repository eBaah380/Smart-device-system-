import random
from smart_device import SmartDevice
class TemperatureSensor(SmartDevice):
    def __init__(self, name, device_id, temperature=25.0):
        super().__init__(name, device_id)
        self.__temperature = temperature

    @property
    def temperature(self):
               return self.__temperature
    def read_temperature(self):
        if not self.power_status:
            print(f"[{self.name}] is OFF. Turn it on to read temperature.")
            return None
        self.__temperature += random.uniform(-0.5, 0.5)
        print(f"[{self.name}] current temperature: {self.__temperature:.1f} C")
        return self.__temperature

    def display_info(self):
        super().display_info()
        print(f"Temperature : {self.__temperature:.1f} C")
