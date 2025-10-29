from pydantic import BaseModel
from constants import DeviceType, DeviceState
from typing import Optional


class DeviceOut(BaseModel):
    id: str
    type: DeviceType
    pin: int
    state: DeviceState
    brightness: Optional[float] = None
