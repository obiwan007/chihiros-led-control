"""Module defining Chihiros devices."""

import inspect
import sys
from typing import Callable

from bleak import BleakScanner
from bleak.backends.device import BLEDevice

from ..exception import DeviceNotFound
from .a2 import AII
from .base_device import BaseDevice
from .c2rgb import CIIRGB
from .fallback import Fallback
from .tiny_terrarium_egg import TinyTerrariumEgg
from .wrgb2 import WRGBII
from .wrgb2_pro import WRGBIIPro

CODE2MODEL = {}
for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj) and issubclass(obj, BaseDevice):
        for model_code in obj._model_codes:
            CODE2MODEL[model_code] = obj


def get_model_class_from_name(device_name: str) -> Callable[[BLEDevice], BaseDevice]:
    """Get device class name from device name."""
    return CODE2MODEL.get(device_name[:-12], Fallback)


async def get_device_from_address(device_address: str) -> BaseDevice:
    """Get BLEDevice object from mac address."""
    # TODO Add logger
    ble_dev = await BleakScanner.find_device_by_address(device_address)  # type: ignore
    if ble_dev and ble_dev.name is not None:
        model_class = get_model_class_from_name(ble_dev.name)
        dev: BaseDevice = model_class(ble_dev)
        return dev

    raise DeviceNotFound


__all__ = [
    "TinyTerrariumEgg",
    "AII",
    "WRGBII",
    "WRGBIIPro",
    "CIIRGB",
    "FallBack",
    "BaseDevice",
    "RGBMode",
    "CODE2MODEL",
    "get_device_from_address",
    "get_model_class_from_name",
    "pump",
]
