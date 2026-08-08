from pymodbus.client import ModbusTcpClient


class ModbusConnection:
    """Low-level Modbus TCP connection to a SolaX HEC charger."""

    def __init__(self, host: str, device_id: int = 1, port: int = 502):
        self.host = host
        self.port = port
        self.device_id = device_id
        self.client = ModbusTcpClient(host=host, port=port)

    def connect(self) -> bool:
        return self.client.connect()

    def close(self):
        self.client.close()

    def read_input(self, register: int) -> int:
        rr = self.client.read_input_registers(
            register,
            count=1,
            device_id=self.device_id,
        )

        if rr.isError():
            raise RuntimeError(f"Failed to read input register {register}")

        return rr.registers[0]

    def read_holding(self, register: int) -> int:
        rr = self.client.read_holding_registers(
            register,
            count=1,
            device_id=self.device_id,
        )

        if rr.isError():
            raise RuntimeError(f"Failed to read holding register {register}")

        return rr.registers[0]

    def write_holding(self, register: int, value: int):
        rr = self.client.write_register(
            register,
            value,
            device_id=self.device_id,
        )

        if rr.isError():
            raise RuntimeError(f"Failed to write register {register}")

        return rr