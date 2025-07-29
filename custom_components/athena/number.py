"""Number platform for Athena integration."""
from __future__ import annotations

from homeassistant.components.number import NumberEntity, NumberMode
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import AthenaDataUpdateCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the number platform."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]

    entities = [
        AthenaThresholdNumber(coordinator),
        AthenaIntervalNumber(coordinator),
    ]

    async_add_entities(entities)


class AthenaNumberEntity(CoordinatorEntity, NumberEntity):
    """Base class for Athena number entities."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator, number_type: str) -> None:
        """Initialize the number entity."""
        super().__init__(coordinator)
        self._number_type = number_type
        self._attr_unique_id = f"{coordinator.entry.entry_id}_{number_type}"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, coordinator.entry.entry_id)},
            "name": "Athena Device",
            "manufacturer": "Athena",
            "model": coordinator.data.get("device_info", {}).get("model", "Unknown"),
            "sw_version": coordinator.data.get("device_info", {}).get("firmware_version", "Unknown"),
        }


class AthenaThresholdNumber(AthenaNumberEntity):
    """Threshold number entity for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the threshold number."""
        super().__init__(coordinator, "threshold")
        self._attr_name = "Athena Threshold"
        self._attr_native_min_value = 0
        self._attr_native_max_value = 100
        self._attr_native_step = 1
        self._attr_mode = NumberMode.SLIDER
        self._attr_icon = "mdi:tune"

    @property
    def native_value(self) -> float | None:
        """Return the entity value to represent the entity state."""
        return self.coordinator.data.get("threshold", 50)

    async def async_set_native_value(self, value: float) -> None:
        """Set new value."""
        # TODO: Implement actual device control
        await self.coordinator.async_request_refresh()


class AthenaIntervalNumber(AthenaNumberEntity):
    """Interval number entity for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the interval number."""
        super().__init__(coordinator, "interval")
        self._attr_name = "Athena Interval"
        self._attr_native_min_value = 10
        self._attr_native_max_value = 300
        self._attr_native_step = 10
        self._attr_mode = NumberMode.BOX
        self._attr_native_unit_of_measurement = "s"
        self._attr_icon = "mdi:timer"

    @property
    def native_value(self) -> float | None:
        """Return the entity value to represent the entity state."""
        return self.coordinator.data.get("interval", 60)

    async def async_set_native_value(self, value: float) -> None:
        """Set new value."""
        # TODO: Implement actual device control
        await self.coordinator.async_request_refresh()
