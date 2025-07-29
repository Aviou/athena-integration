"""Sensor platform for Athena integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    PERCENTAGE,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    UnitOfPressure,
    UnitOfTemperature,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DOMAIN,
    SENSOR_HUMIDITY,
    SENSOR_PRESSURE,
    SENSOR_SIGNAL_STRENGTH,
    SENSOR_STATUS,
    SENSOR_TEMPERATURE,
)
from .coordinator import AthenaDataUpdateCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]

    entities = [
        AthenaTemperatureSensor(coordinator),
        AthenaHumiditySensor(coordinator),
        AthenaPressureSensor(coordinator),
        AthenaSignalStrengthSensor(coordinator),
        AthenaStatusSensor(coordinator),
    ]

    async_add_entities(entities)


class AthenaSensorEntity(CoordinatorEntity, SensorEntity):
    """Base class for Athena sensors."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator, sensor_type: str) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._sensor_type = sensor_type
        self._attr_unique_id = f"{coordinator.entry.entry_id}_{sensor_type}"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, coordinator.entry.entry_id)},
            "name": "Athena Device",
            "manufacturer": "Athena",
            "model": coordinator.data.get("device_info", {}).get("model", "Unknown"),
            "sw_version": coordinator.data.get("device_info", {}).get("firmware_version", "Unknown"),
        }


class AthenaTemperatureSensor(AthenaSensorEntity):
    """Temperature sensor for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the temperature sensor."""
        super().__init__(coordinator, SENSOR_TEMPERATURE)
        self._attr_name = "Athena Temperature"
        self._attr_device_class = SensorDeviceClass.TEMPERATURE
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS

    @property
    def native_value(self) -> float | None:
        """Return the state of the sensor."""
        return self.coordinator.data.get("temperature")


class AthenaHumiditySensor(AthenaSensorEntity):
    """Humidity sensor for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the humidity sensor."""
        super().__init__(coordinator, SENSOR_HUMIDITY)
        self._attr_name = "Athena Humidity"
        self._attr_device_class = SensorDeviceClass.HUMIDITY
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_native_unit_of_measurement = PERCENTAGE

    @property
    def native_value(self) -> float | None:
        """Return the state of the sensor."""
        return self.coordinator.data.get("humidity")


class AthenaPressureSensor(AthenaSensorEntity):
    """Pressure sensor for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the pressure sensor."""
        super().__init__(coordinator, SENSOR_PRESSURE)
        self._attr_name = "Athena Pressure"
        self._attr_device_class = SensorDeviceClass.ATMOSPHERIC_PRESSURE
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_native_unit_of_measurement = UnitOfPressure.HPA

    @property
    def native_value(self) -> float | None:
        """Return the state of the sensor."""
        return self.coordinator.data.get("pressure")


class AthenaSignalStrengthSensor(AthenaSensorEntity):
    """Signal strength sensor for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the signal strength sensor."""
        super().__init__(coordinator, SENSOR_SIGNAL_STRENGTH)
        self._attr_name = "Athena Signal Strength"
        self._attr_device_class = SensorDeviceClass.SIGNAL_STRENGTH
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_native_unit_of_measurement = SIGNAL_STRENGTH_DECIBELS_MILLIWATT

    @property
    def native_value(self) -> int | None:
        """Return the state of the sensor."""
        return self.coordinator.data.get("signal_strength")


class AthenaStatusSensor(AthenaSensorEntity):
    """Status sensor for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the status sensor."""
        super().__init__(coordinator, SENSOR_STATUS)
        self._attr_name = "Athena Status"

    @property
    def native_value(self) -> str | None:
        """Return the state of the sensor."""
        return self.coordinator.data.get("status")
