from sqlalchemy import Column, Integer, String, Float, Enum, DateTime
from sqlalchemy.orm import validates
from datetime import datetime

from constants import DeviceType, DeviceState
from state.db import Base


class Device(Base):
    #todo: make sure id is updated if type or pin values change
    __tablename__ = "device_state"

    id = Column(String, primary_key=True)
    type = Column(Enum(DeviceType), nullable=False)
    state = Column(Enum(DeviceState), default=DeviceState.OFF)
    brightness = Column(Float, nullable=True)
    pin = Column(Integer, nullable=False)
    last_updated = Column(DateTime, default=datetime.now())

    def __init__(self, type, pin, state=DeviceState.OFF, brightness=None):
        self.type = type
        self.pin = pin
        self.state = state
        self.brightness = brightness
        self.id = f"{type}_{pin}"
