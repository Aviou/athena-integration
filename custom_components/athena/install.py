"""Installation and update utilities for Athena Integration."""
from __future__ import annotations

import asyncio
import logging
from pathlib import Path
from typing import Any

_LOGGER = logging.getLogger(__name__)

REQUIRED_FILES = [
    "__init__.py",
    "config_flow.py",
    "const.py",
    "coordinator.py",
    "manifest.json",
    "strings.json",
    "sensor.py",
    "switch.py",
    "binary_sensor.py",
    "number.py",
    "select.py",
]


async def verify_installation() -> bool:
    """Verify that all required files are present."""
    current_dir = Path(__file__).parent
    
    missing_files = []
    for file_name in REQUIRED_FILES:
        file_path = current_dir / file_name
        if not file_path.exists():
            missing_files.append(file_name)
    
    if missing_files:
        _LOGGER.error("Missing required files: %s", missing_files)
        return False
    
    _LOGGER.info("All required files are present")
    return True


async def get_version_info() -> dict[str, Any]:
    """Get version information from manifest.json."""
    import json
    
    current_dir = Path(__file__).parent
    manifest_path = current_dir / "manifest.json"
    
    try:
        with open(manifest_path, "r", encoding="utf-8") as file:
            manifest = json.load(file)
            return {
                "version": manifest.get("version", "unknown"),
                "domain": manifest.get("domain", "athena"),
                "name": manifest.get("name", "Athena"),
                "documentation": manifest.get("documentation", ""),
                "issue_tracker": manifest.get("issue_tracker", ""),
            }
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        _LOGGER.error("Error reading manifest.json: %s", ex)
        return {}


def log_system_info() -> None:
    """Log system information for debugging."""
    import sys
    import platform
    
    _LOGGER.info("Python version: %s", sys.version)
    _LOGGER.info("Platform: %s", platform.platform())
    _LOGGER.info("Architecture: %s", platform.architecture())


if __name__ == "__main__":
    # This can be used for testing the installation
    asyncio.run(verify_installation())
