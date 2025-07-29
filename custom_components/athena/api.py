"""API client for Athena device communication."""
from __future__ import annotations

import asyncio
import json
import logging
from typing import Any, Dict, Optional

import aiohttp

from .const import DEFAULT_TIMEOUT

_LOGGER = logging.getLogger(__name__)


class AthenaAPIClient:
    """API client for communicating with Athena devices."""

    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> None:
        """Initialize the API client."""
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout
        self.base_url = f"http://{host}:{port}"
        self._session: Optional[aiohttp.ClientSession] = None

    async def _get_session(self) -> aiohttp.ClientSession:
        """Get or create an aiohttp session."""
        if self._session is None or self._session.closed:
            timeout = aiohttp.ClientTimeout(total=self.timeout)
            auth = aiohttp.BasicAuth(self.username, self.password)
            self._session = aiohttp.ClientSession(
                timeout=timeout,
                auth=auth,
                headers={"Content-Type": "application/json"},
            )
        return self._session

    async def close(self) -> None:
        """Close the aiohttp session."""
        if self._session and not self._session.closed:
            await self._session.close()

    async def test_connection(self) -> bool:
        """Test connection to the device."""
        try:
            session = await self._get_session()
            async with session.get(f"{self.base_url}/api/status") as response:
                return response.status == 200
        except Exception as ex:
            _LOGGER.error("Connection test failed: %s", ex)
            return False

    async def get_device_info(self) -> Dict[str, Any]:
        """Get device information."""
        try:
            session = await self._get_session()
            async with session.get(f"{self.base_url}/api/info") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    _LOGGER.error("Failed to get device info: %s", response.status)
                    return {}
        except Exception as ex:
            _LOGGER.error("Error getting device info: %s", ex)
            return {}

    async def get_sensor_data(self) -> Dict[str, Any]:
        """Get current sensor data from the device."""
        try:
            session = await self._get_session()
            async with session.get(f"{self.base_url}/api/sensors") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    _LOGGER.error("Failed to get sensor data: %s", response.status)
                    return {}
        except Exception as ex:
            _LOGGER.error("Error getting sensor data: %s", ex)
            return {}

    async def get_status(self) -> Dict[str, Any]:
        """Get device status."""
        try:
            session = await self._get_session()
            async with session.get(f"{self.base_url}/api/status") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    _LOGGER.error("Failed to get status: %s", response.status)
                    return {}
        except Exception as ex:
            _LOGGER.error("Error getting status: %s", ex)
            return {}

    async def set_power(self, state: bool) -> bool:
        """Set power state."""
        try:
            session = await self._get_session()
            data = {"power": state}
            async with session.post(
                f"{self.base_url}/api/power",
                data=json.dumps(data)
            ) as response:
                return response.status == 200
        except Exception as ex:
            _LOGGER.error("Error setting power: %s", ex)
            return False

    async def set_auto_mode(self, state: bool) -> bool:
        """Set auto mode state."""
        try:
            session = await self._get_session()
            data = {"auto_mode": state}
            async with session.post(
                f"{self.base_url}/api/mode",
                data=json.dumps(data)
            ) as response:
                return response.status == 200
        except Exception as ex:
            _LOGGER.error("Error setting auto mode: %s", ex)
            return False

    async def set_threshold(self, value: float) -> bool:
        """Set threshold value."""
        try:
            session = await self._get_session()
            data = {"threshold": value}
            async with session.post(
                f"{self.base_url}/api/config",
                data=json.dumps(data)
            ) as response:
                return response.status == 200
        except Exception as ex:
            _LOGGER.error("Error setting threshold: %s", ex)
            return False

    async def set_interval(self, value: float) -> bool:
        """Set interval value."""
        try:
            session = await self._get_session()
            data = {"interval": value}
            async with session.post(
                f"{self.base_url}/api/config",
                data=json.dumps(data)
            ) as response:
                return response.status == 200
        except Exception as ex:
            _LOGGER.error("Error setting interval: %s", ex)
            return False

    async def set_mode(self, mode: str) -> bool:
        """Set operation mode."""
        try:
            session = await self._get_session()
            data = {"mode": mode}
            async with session.post(
                f"{self.base_url}/api/mode",
                data=json.dumps(data)
            ) as response:
                return response.status == 200
        except Exception as ex:
            _LOGGER.error("Error setting mode: %s", ex)
            return False

    async def set_profile(self, profile: str) -> bool:
        """Set device profile."""
        try:
            session = await self._get_session()
            data = {"profile": profile}
            async with session.post(
                f"{self.base_url}/api/profile",
                data=json.dumps(data)
            ) as response:
                return response.status == 200
        except Exception as ex:
            _LOGGER.error("Error setting profile: %s", ex)
            return False
