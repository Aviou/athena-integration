"""Constants for the Athena integration."""
from __future__ import annotations

DOMAIN = "athena"

# Configuration Keys
CONF_HOST = "host"
CONF_PORT = "port"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_DEVICE_TYPE = "device_type"
CONF_SCAN_INTERVAL = "scan_interval"

# Device Types
DEVICE_TYPE_CONTROLLER = "controller"
DEVICE_TYPE_MONITOR = "monitor"
DEVICE_TYPE_SENSOR = "sensor"

DEVICE_TYPES = [
    DEVICE_TYPE_CONTROLLER,
    DEVICE_TYPE_MONITOR, 
    DEVICE_TYPE_SENSOR,
]

# Default Values
DEFAULT_PORT = 80
DEFAULT_SCAN_INTERVAL = 30
DEFAULT_TIMEOUT = 10

# Entity Names
SENSOR_TEMPERATURE = "temperature"
SENSOR_HUMIDITY = "humidity"
SENSOR_PRESSURE = "pressure"
SENSOR_STATUS = "status"
SENSOR_SIGNAL_STRENGTH = "signal_strength"

SWITCH_POWER = "power"
SWITCH_AUTO_MODE = "auto_mode"
SWITCH_ALARM = "alarm"

BINARY_SENSOR_ONLINE = "online"
BINARY_SENSOR_FAULT = "fault"
BINARY_SENSOR_MAINTENANCE = "maintenance"

# Attributes
ATTR_DEVICE_INFO = "device_info"
ATTR_FIRMWARE_VERSION = "firmware_version"
ATTR_HARDWARE_VERSION = "hardware_version"
ATTR_SERIAL_NUMBER = "serial_number"
ATTR_MODEL = "model"
