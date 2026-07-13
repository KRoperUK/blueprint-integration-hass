"""Data update coordinator for the example integration."""

from __future__ import annotations

import logging
from datetime import timedelta
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DEFAULT_SCAN_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)


class ExampleCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Fetch data for one Example hub."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            config_entry=entry,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.entry = entry

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from the API / device.

        Replace with a call into your PyPI client library. Tag provenance when
        multiple transports exist (e.g. source=cloud|local|derived).
        """
        try:
            # Placeholder demo payload.
            return {
                "status": {"code": "status", "value": "ok", "source": "cloud"},
                "power": {"code": "power", "value": 0.0, "unit": "W", "source": "cloud"},
            }
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}") from err
