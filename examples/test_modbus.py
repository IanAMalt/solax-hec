from solax_hec.modbus import ModbusConnection

HOST = "192.168.0.169"

mb = ModbusConnection(HOST)

try:
    print("Connecting...")
    mb.connect()

    print("1640:", mb.read_holding(1640))
    print("1641:", mb.read_holding(1641))
    print("1642:", mb.read_holding(1642))

    print("Success!")

finally:
    mb.close()