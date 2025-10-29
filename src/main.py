import logging
import threading

from fastapi import FastAPI

from api.routes import pump
from api.routes import devices
from controller.gpio_pump_controller import GPIOPumpController
from controller.runner import DeviceRunner
from state.container import state_manager
from state.init_db import init_db
from constants import DeviceType

logging.basicConfig(
    level=logging.INFO,  # minimum level to capture
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

init_db()

pump_controller_2 = GPIOPumpController(control_pin=2)
pump_controller_3 = GPIOPumpController(control_pin=3)

state_manager.save_device(DeviceType.PUMP, pump_controller_2.control_pin)
state_manager.save_device(DeviceType.PUMP, pump_controller_3.control_pin)
controllers = {
    f"{DeviceType.PUMP}_{pump_controller_2.control_pin}": pump_controller_2,
    f"{DeviceType.PUMP}_{pump_controller_3.control_pin}": pump_controller_3,
}

# Initialize and start device runner
runner = DeviceRunner(controllers=controllers, state_manager=state_manager, poll_interval=1.0)
runner_thread = threading.Thread(target=runner.start, daemon=True)
runner_thread.start()

app = FastAPI(title="Growbox API")
app.include_router(pump.router)
app.include_router(devices.router)
