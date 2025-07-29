"""Binary sensor platform for Athena integration."""
from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import BINARY_SENSOR_FAULT, BINARY_SENSOR_MAINTENANCE, BINARY_SENSOR_ONLINE, DOMAIN
from .coordinator import AthenaDataUpdateCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the binary sensor platform."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]

    entities = [
        AthenaOnlineBinarySensor(coordinator),
        AthenaFaultBinarySensor(coordinator),
        AthenaMaintenanceBinarySensor(coordinator),
    ]

    async_add_entities(entities)


class AthenaBinarySensorEntity(CoordinatorEntity, BinarySensorEntity):
    """Base class for Athena binary sensors."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator, sensor_type: str) -> None:
        """Initialize the binary sensor."""
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


class AthenaOnlineBinarySensor(AthenaBinarySensorEntity):
    """Online status binary sensor for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the online binary sensor."""
        super().__init__(coordinator, BINARY_SENSOR_ONLINE)
        self._attr_name = "Athena Online"
        self._attr_device_class = BinarySensorDeviceClass.CONNECTIVITY

    @property
    def is_on(self) -> bool | None:
        """Return true if the binary sensor is on."""
        return self.coordinator.data.get("online")


class AthenaFaultBinarySensor(AthenaBinarySensorEntity):
    """Fault binary sensor for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the fault binary sensor."""
        super().__init__(coordinator, BINARY_SENSOR_FAULT)
        self._attr_name = "Athena Fault"
        self._attr_device_class = BinarySensorDeviceClass.PROBLEM

    @property
    def is_on(self) -> bool | None:
        """Return true if the binary sensor is on."""
        return self.coordinator.data.get("fault")


class AthenaMaintenanceBinarySensor(AthenaBinarySensorEntity):
    """Maintenance binary sensor for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the maintenance binary sensor."""
        super().__init__(coordinator, BINARY_SENSOR_MAINTENANCE)
        self._attr_name = "Athena Maintenance"
        self._attr_device_class = BinarySensorDeviceClass.RUNNING

    @property
    def is_on(self) -> bool | None:
        """Return true if the binary sensor is on."""
        return self.coordinator.data.get("maintenance")
