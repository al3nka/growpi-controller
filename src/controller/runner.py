import logging
import time

from controller.light_controller import LightController
from controller.pump_controller import PumpController
from state.manager import StateManager
from state.models.device_state import DeviceState, Device


logger = logging.getLogger()


class DeviceRunner:
    def __init__(self, controllers: dict[str, PumpController | LightController], state_manager: StateManager, poll_interval=1.0):
        self.controllers = controllers
        self.state_manager = state_manager
        self.poll_interval = poll_interval
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            self.tick()
            time.sleep(self.poll_interval)

    def stop(self):
        self.running = False

    def tick(self):
        for device_id, controller in self.controllers.items():
            db_device = self.state_manager.session.get(Device, device_id)
            if not db_device:
                continue
            if controller.state != db_device.state:
                logger.info(f"tick in progress: controller state {controller.state}, db state {db_device.state}, are equal: {controller.state == db_device.state}")
                if db_device.state == DeviceState.ON:
                    controller.turn_on()
                else:
                    controller.turn_off()
