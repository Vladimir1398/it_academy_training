# Абстрактный класс SmartDevice: Объявите атрибуты 
# device_name и _is_on (по умолчанию False). Создайте 
# обычные методы turn_on() и turn_off(), а также абстрактное 
# свойство status_report, возвращающее строку о текущем 
# состоянии прибора. 
# Промежуточный или специализированный класс: 
# • SmartLight — добавляет атрибут brightness (яркость от 
# 0 до 100) и метод ее изменения. Реализует status_report. 
# • SmartThermostat — добавляет target_temp (целевая 
# температура). Реализует status_report. 
# • SmartLock — переопределяет методы 
# включения/выключения на логику блокировки и 
# разблокировки двери. 
# Проверка: Создайте класс-контроллер SmartHomeHub, 
# который хранит список устройств и имеет метод turn_all_off(), 
# выключающий все приборы разом.


from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, device_name):
        self.device_name = device_name
        self._is_on = False

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False

    @property
    @abstractmethod
    def status_report(self):
        pass


class SmartLight(SmartDevice):
    def __init__(self, device_name, brightness=100):
        super().__init__(device_name)
        self.brightness = brightness

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Яркость 0..100")
        self._brightness = value

    @property
    def status_report(self):
        return f"Лампа {self.device_name}: {'вкл' if self._is_on else 'выкл'}, {self._brightness}%"


class SmartThermostat(SmartDevice):
    def __init__(self, device_name, target_temp=22.0):
        super().__init__(device_name)
        self.target_temp = target_temp

    @property
    def status_report(self):
        return f"Термостат {self.device_name}: {'вкл' if self._is_on else 'выкл'}, {self.target_temp}°C"


class SmartLock(SmartDevice):
    def __init__(self, device_name):
        super().__init__(device_name)
        self._is_on = True

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False

    @property
    def status_report(self):
        return f"Замок {self.device_name}: {'заблокирован' if self._is_on else 'разблокирован'}"



light = SmartLight("Люстра", 80)
thermo = SmartThermostat("Спальня", 21.5)
lock = SmartLock("Дверь")

light.turn_on()
thermo.turn_on()

print(light.status_report)
print(thermo.status_report)
print(lock.status_report)

light.turn_off()
thermo.turn_off()
lock.turn_off()

print("--- после выключения ---")
print(light.status_report)
print(thermo.status_report)
print(lock.status_report)   