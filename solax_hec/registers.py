from dataclasses import dataclass

@dataclass(frozen=True)
class Register:
    address:int
    name:str
    unit:str=""
    scale:float=1.0
    writable:bool=False

FAST_CURRENT=Register(1640,"Fast Current","A",0.01,True)
MODE=Register(1641,"Mode","",1.0,True)

GRID_VOLTAGE=Register(0,"Grid Voltage","V",0.01)
GRID_FREQUENCY=Register(12,"Grid Frequency","Hz",0.01)
CHARGE_CURRENT=Register(4,"Charge Current","A",0.01)
CHARGE_POWER=Register(8,"Charge Power","W",1.0)
