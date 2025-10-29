from fastapi import APIRouter

from state.container import state_manager
from constants import DeviceType, DeviceState

router = APIRouter(prefix="/pump", tags=["pump"])


@router.post("/{pin}/start")
def start_pump(pin: int):
    state_manager.save_device(type=DeviceType.PUMP, pin=pin, state=DeviceState.ON)


@router.post("/{pin}/stop")
def stop_pump(pin: int):
    state_manager.save_device(type=DeviceType.PUMP, pin=pin, state=DeviceState.OFF)


@router.get("/{pin}")
def pin_status(pin: int):
    pin_state_values = state_manager.load_device(type=DeviceType.PUMP, pin=pin)
    return {"state": pin_state_values.state}
