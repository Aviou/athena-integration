"""Select platform for Athena integration."""
from __future__ import annotations

from homeassistant.components.select import SelectEntity
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
    """Set up the select platform."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]

    entities = [
        AthenaModeSelect(coordinator),
        AthenaProfileSelect(coordinator),
    ]

    async_add_entities(entities)


class AthenaSelectEntity(CoordinatorEntity, SelectEntity):
    """Base class for Athena select entities."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator, select_type: str) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._select_type = select_type
        self._attr_unique_id = f"{coordinator.entry.entry_id}_{select_type}"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, coordinator.entry.entry_id)},
            "name": "Athena Device",
            "manufacturer": "Athena",
            "model": coordinator.data.get("device_info", {}).get("model", "Unknown"),
            "sw_version": coordinator.data.get("device_info", {}).get("firmware_version", "Unknown"),
        }


class AthenaModeSelect(AthenaSelectEntity):
    """Mode select entity for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the mode select."""
        super().__init__(coordinator, "mode")
        self._attr_name = "Athena Mode"
        self._attr_options = ["manual", "automatic", "scheduled", "maintenance"]
        self._attr_icon = "mdi:cog"

    @property
    def current_option(self) -> str | None:
        """Return the selected entity option to represent the entity state."""
        return self.coordinator.data.get("mode", "automatic")

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        # TODO: Implement actual device control
        await self.coordinator.async_request_refresh()


class AthenaProfileSelect(AthenaSelectEntity):
    """Profile select entity for Athena device."""

    def __init__(self, coordinator: AthenaDataUpdateCoordinator) -> None:
        """Initialize the profile select."""
        super().__init__(coordinator, "profile")
        self._attr_name = "Athena Profile"
        self._attr_options = ["eco", "normal", "performance", "custom"]
        self._attr_icon = "mdi:account-settings"

    @property
    def current_option(self) -> str | None:
        """Return the selected entity option to represent the entity state."""
        return self.coordinator.data.get("profile", "normal")

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        # TODO: Implement actual device control
        await self.coordinator.async_request_refresh()
