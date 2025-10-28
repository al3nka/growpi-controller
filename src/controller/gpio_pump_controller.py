import logging

from constants import DeviceState
from controller.pump_controller import PumpController
import RPi.GPIO as GPIO


logger = logging.getLogger()


class GPIOPumpController(PumpController):

    def __init__(self, control_pin: int):
        logger.info("Initializing pump controller")
        super().__init__(control_pin)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._control_pin, GPIO.OUT)

    def turn_on(self):
        self._state = DeviceState.ON
        logger.info(f"State of pump on pin {self.control_pin} is ON")
        GPIO.output(self._control_pin, GPIO.HIGH)

    def turn_off(self):
        self._state = DeviceState.OFF
        logger.info(f"State of pump on pin {self.control_pin} is OFF")
        GPIO.output(self._control_pin, GPIO.LOW)

    @property
    def state(self) -> DeviceState:
        return self._state

    def cleanup(self):
        logger.info(f"Running cleanup for pump on pin {self.control_pin}")
        GPIO.output(self._control_pin, GPIO.LOW)
        GPIO.cleanup(self._control_pin)
