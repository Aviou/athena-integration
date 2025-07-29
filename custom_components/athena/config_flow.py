"""Config flow for Athena integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_PORT, CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError

from .const import (
    CONF_DEVICE_TYPE,
    CONF_SCAN_INTERVAL,
    DEFAULT_PORT,
    DEFAULT_SCAN_INTERVAL,
    DEVICE_TYPES,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
        vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
        vol.Required(CONF_USERNAME): str,
        vol.Required(CONF_PASSWORD): str,
        vol.Required(CONF_DEVICE_TYPE): vol.In(DEVICE_TYPES),
        vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): int,
    }
)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect.
    
    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """
    # TODO: Implement actual connection validation
    # For now, we'll do basic validation
    
    if not data[CONF_HOST]:
        raise InvalidHost
    
    if data[CONF_PORT] < 1 or data[CONF_PORT] > 65535:
        raise InvalidPort
    
    if not data[CONF_USERNAME] or not data[CONF_PASSWORD]:
        raise InvalidAuth
    
    # Return info that you want to store in the config entry.
    return {"title": f"Athena {data[CONF_DEVICE_TYPE].title()} ({data[CONF_HOST]})"}


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Athena."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except InvalidHost:
                errors["base"] = "invalid_host"
            except InvalidPort:
                errors["base"] = "invalid_port"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                # Create unique ID based on host and device type
                unique_id = f"{user_input[CONF_HOST]}_{user_input[CONF_DEVICE_TYPE]}"
                await self.async_set_unique_id(unique_id)
                self._abort_if_unique_id_configured()
                
                return self.async_create_entry(title=info["title"], data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidAuth(HomeAssistantError):
    """Error to indicate there is invalid auth."""


class InvalidHost(HomeAssistantError):
    """Error to indicate invalid host."""


class InvalidPort(HomeAssistantError):
    """Error to indicate invalid port."""
