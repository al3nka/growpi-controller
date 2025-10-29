from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.state.db import get_session
from src.state.models.device_state import Device
from src.api.schemas import DeviceOut

router = APIRouter()


@router.get("/devices", response_model=list[DeviceOut])
def get_all_devices(session: Session = Depends(get_session)):
    devices = session.query(Device).all()
    return [
        DeviceOut(
            id=device.id,
            type=device.type,
            pin=device.pin,
            state=device.state,
            brightness=device.brightness
        )
        for device in devices
    ]
