"""CII RGB device Model."""

from .base_device import BaseDevice


class CIIRGB(BaseDevice):
    """Chihiros WRGB II device Class."""

    _model_name = "CII RGB"
    _model_code = ["DYNCRGP"]
    _colors: dict[str, int] = {
        "red": 0,
        "green": 1,
        "blue": 2,
    }
