"""Switch platform for Athena integration."""
from __future__ import annotations

from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, SWITCH_AUTO_MODE, SWITCH_POWER
from .coordinator import AthenaDataUpdateCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the switch platform."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]

    entities = [
        AthenaPowerSwitch(coordinator),
        AthenaAutoModeSwitch(coordinator),
    ]

    async_add_entities(entities)


class AthenaSwitchEntity(CoordinatorEntity, SwitchEntity):
    """Base class for Athena switches."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator, switch_type: str) -> None:
        """Initialize the switch."""
        super().__init__(coordinator)
        self._switch_type = switch_type
        self._attr_unique_id = f"{coordinator.entry.entry_id}_{switch_type}"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, coordinator.entry.entry_id)},
            "name": "Athena Device",
            "manufacturer": "Athena",
            "model": coordinator.data.get("device_info", {}).get("model", "Unknown"),
            "sw_version": coordinator.data.get("device_info", {}).get("firmware_version", "Unknown"),
        }


class AthenaPowerSwitch(AthenaSwitchEntity):
    """Power switch for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the power switch."""
        super().__init__(coordinator, SWITCH_POWER)
        self._attr_name = "Athena Power"
        self._attr_icon = "mdi:power"

    @property
    def is_on(self) -> bool | None:
        """Return true if switch is on."""
        return self.coordinator.data.get("power")

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""
        # TODO: Implement actual device control
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""
        # TODO: Implement actual device control
        await self.coordinator.async_request_refresh()


class AthenaAutoModeSwitch(AthenaSwitchEntity):
    """Auto mode switch for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the auto mode switch."""
        super().__init__(coordinator, SWITCH_AUTO_MODE)
        self._attr_name = "Athena Auto Mode"
        self._attr_icon = "mdi:auto-mode"

    @property
    def is_on(self) -> bool | None:
        """Return true if switch is on."""
        return self.coordinator.data.get("auto_mode")

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""
        # TODO: Implement actual device control
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""
        # TODO: Implement actual device control
        await self.coordinator.async_request_refresh()
