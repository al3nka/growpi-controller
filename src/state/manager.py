from pydantic.v1.fields import DeferredType
from sqlalchemy.orm import Session
from datetime import datetime
from .db import SessionLocal
from state.models.device_state import Device, DeviceState, DeviceType


class StateManager:

    def __init__(self):
        self.session: Session = SessionLocal()

    def save_device(self, type: DeviceType, pin: int, state: DeviceState = DeviceState.OFF, brightness: float = None):
        device_id = f"{type}_{pin}"
        device = self.session.get(Device, device_id)

        if not device:
            device = Device(type=type, pin=pin, state=state, brightness=brightness)
            self.session.add(device)
        else:
            device.state = state
            device.brightness = brightness
            device.last_updated = datetime.now()

        self.session.commit()

    def load_device(self, type: DeviceType, pin: int) -> Device | None:
        device_id = f"{type}_{pin}"
        return self.session.get(Device, device_id)

    def close(self):
        self.session.close()
