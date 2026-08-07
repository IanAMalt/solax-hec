# \# solax-hec

# 

# A Python library for locally controlling and monitoring SolaX Gen2 HEC EV chargers.

# 

# > \*\*Project Status:\*\* 🚧 Early development

# 

# \## Features

# 

# \### Working

# 

# \- ✅ Local HTTP authentication

# \- ✅ Modbus TCP communication

# \- ✅ Read Holding Registers

# \- ✅ Read Input Registers

# \- ✅ Write Holding Registers

# \- ✅ Change charging mode

# \- ✅ Change fast charge current

# \- ✅ Reverse engineered register map

# 

# \### Planned

# 

# \- 🚧 High-level Python API

# \- 🚧 Home Assistant integration

# \- 🚧 MQTT support

# \- 🚧 Automatic charger discovery

# \- 🚧 Async API

# 

# \## Confirmed Registers

# 

# | Register | Description | Access |

# |----------:|-------------|:------:|

# | 1640 | Fast charge current (×100 A) | RW |

# | 1641 | Charge mode (0=Fast, 1=Eco, 2=Green) | RW |

# | 0 | Grid voltage (×100 V) | R |

# | 12 | Grid frequency (×100 Hz) | R |

# | 4 | Charge current (candidate) | R |

# | 8 | Charge power (candidate) | R |

# 

# \## Repository Structure

# 

# ```

# docs/

# examples/

# solax\_hec/

# tests/

# tools/

# ```

# 

# \## Roadmap

# 

# \- \[x] HTTP authentication

# \- \[x] Modbus communication

# \- \[x] Register discovery

# \- \[ ] High-level client

# \- \[ ] Home Assistant integration

# \- \[ ] Documentation

# \- \[ ] PyPI package

# 

# \## Disclaimer

# 

# This project is not affiliated with or endorsed by SolaX Power.

# 

# It is a community reverse engineering effort intended to provide local control and monitoring of compatible chargers.

