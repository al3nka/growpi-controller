from enum import Enum as PyEnum


class DeviceState(PyEnum):
    OFF = "OFF"
    ON = "ON"
    ERROR = "ERROR"


class DeviceType(PyEnum):
    LAMP = "LAMP"
    PUMP = "PUMP"