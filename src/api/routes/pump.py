from fastapi import APIRouter

from state.container import state_manager
from constants import DeviceType, DeviceState

pump_router = APIRouter(prefix="/pump", tags=["pump"])


@pump_router.post("/pump/{pin}/start")
def start_pump(pin: int):
    state_manager.save_device(type=DeviceType.PUMP, pin=pin, state=DeviceState.ON)


@pump_router.post("/pump/{pin}/stop")
def stop_pump(pin: int):
    state_manager.save_device(type=DeviceType.PUMP, pin=pin, state=DeviceState.OFF)


@pump_router.get("/pump/{pin}")
def pin_status(pin: int):
    pin_state_values = state_manager.load_device(type=DeviceType.PUMP, pin=pin)
    return {"state": pin_state_values.state}
