from abc import ABC, abstractmethod

from constants import DeviceState


class PumpController(ABC):
    _state: DeviceState
    _control_pin: int

    def __init__(self, control_pin: int):
        self._state = DeviceState.OFF
        self._control_pin = control_pin

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @property
    @abstractmethod
    def state(self) -> DeviceState:
        pass

    @property
    def control_pin(self):
        return self._control_pin

    @abstractmethod
    def cleanup(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(pin={self.control_pin})"
