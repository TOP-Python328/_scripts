"""Демонстратор наблюдателя: реализация с интерфейсами."""

from abc import ABC, abstractmethod
from datetime import datetime as dt
from time import sleep


class Patient(ABC):
    """Интерфейс для наблюдаемого объекта."""
    def __init__(self, name: str):
        self.name = name
        self.__monitors: list['Monitor'] = []
    
    @abstractmethod
    def get_parameter(self, parameter: str):
        pass
    
    @abstractmethod
    def set_parameter(self, parameter: str, value):
        pass
    
    def add_monitor(self, device: 'Monitor'):
        """Подписка экземпляра наблюдателя."""
        self.__monitors.append(device)
    
    def remove_monitor(self, device: 'Monitor'):
        """Отмена подписки экземпляра наблюдателя."""
        self.__monitors.remove(device)
    
    def update_monitors(self):
        """Уведомление подписанных наблюдателей."""
        for device in self.__monitors:
            device.update(self)


class COVIDPatient(Patient):
    """Наблюдаемый объект."""
    def __init__(self, name: str):
        super().__init__(name)
        self.__parameters = {
            'температура': 37.0,
            'пульс': 90,
            'сатурация': 95,
        }
    
    def get_parameter(self, parameter: str):
        return self.__parameters[parameter]
    
    def set_parameter(self, parameter: str, value):
        self.__parameters[parameter] = value
        self.update_monitors()


class Monitor(ABC):
    """Интерфейс для наблюдателей."""
    @abstractmethod
    def update(self, patient: Patient):
        pass
    
    @staticmethod
    def info_message(message: str):
        """Реакция наблюдателя."""
        print(f'НОРМАЛЬНО — {message}')
    
    @staticmethod
    def warn_message(message: str):
        """Реакция наблюдателя."""
        print(f'ПРЕДУПРЕЖДЕНИЕ — {message}')
    
    @staticmethod
    def emrg_message(message: str):
        """Реакция наблюдателя."""
        print(f'КРИТИЧНО! {message}')


class Thermometer(Monitor):
    """Наблюдатель температуры."""
    def update(self, subject: Patient):
        temperature = subject.get_parameter('температура')
        message = f'ТЕМПЕРАТУРА: {subject.name} - {temperature}'
        if 36.4 <= temperature <= 37.1:
            self.info_message(message)
        elif 37.1 < temperature < 38.3:
            self.warn_message(message)
        else:
            self.emrg_message(message)


class Heartbeat(Monitor):
    """Наблюдатель пульса."""
    def update(self, subject: Patient):
        heartrate = subject.get_parameter('пульс')
        message = f'ПУЛЬС: {subject.name} - {heartrate}'
        if heartrate < 100:
            self.info_message(message)
        elif 100 <= heartrate <= 110:
            self.warn_message(message)
        else:
            self.emrg_message(message)


class Oxymeter(Monitor):
    """Наблюдатель сатурации."""
    def update(self, subject: Patient):
        saturation = subject.get_parameter('сатурация')
        message = f'САТУРАЦИЯ: {subject.name} - {saturation}'
        if 95 <= saturation:
            self.info_message(message)
        elif 93 < saturation < 95:
            self.warn_message(message)
        else:
            self.emrg_message(message)


if __name__ == '__main__':
    # тесты
    oleg = COVIDPatient('Олег')
    
    monitor = [
        Thermometer(),
        Heartbeat(),
        Oxymeter()
    ]
    for sensor in monitor:
        oleg.add_monitor(sensor)
    
    start_temp = oleg.get_parameter('температура')
    start_beat = oleg.get_parameter('пульс')
    start_oxy = oleg.get_parameter('сатурация')
    
    for i in range(1, 61):
        print(f'\n{dt.now():%H:%M:%S}')
        oleg.set_parameter('температура', start_temp+i*0.05)
        oleg.set_parameter('пульс', round(start_beat+i*0.4))
        oleg.set_parameter('сатурация', round(start_oxy-i*0.03))
        sleep(1)

