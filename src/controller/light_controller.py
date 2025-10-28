from abc import ABC, abstractmethod

from constants import DeviceState


class LightController(ABC):
    state: DeviceState
    brightness: float

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def get_state(self) -> DeviceState:
        pass

    @abstractmethod
    def set_brightness(self, brightness: float):
        pass
