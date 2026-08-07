from .enums import ChargeMode
from . import registers

class SolaxHECClient:
    """High-level client skeleton.

    TODO:
      * integrate HTTP login/session
      * integrate Modbus TCP backend
      * expose telemetry as Python properties
    """

    def __init__(self, host:str, username:str="", password:str=""):
        self.host=host
        self.username=username
        self.password=password

    def login(self):
        raise NotImplementedError("Reuse your existing api.py/crypto.py implementation")

    def set_mode(self, mode:ChargeMode):
        raise NotImplementedError

    def set_fast_current(self, amps:float):
        raise NotImplementedError
