from .modbus import ModbusConnection


class Charger:
    """High-level interface to a SolaX HEC charger."""

    def __init__(self, host: str):
        self.modbus = ModbusConnection(host)

    def connect(self):
        self.modbus.connect()

    def close(self):
        self.modbus.close()