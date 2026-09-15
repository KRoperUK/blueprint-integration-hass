"""Tests for the example coordinator."""

from __future__ import annotations

from custom_components.example.const import DEFAULT_SCAN_INTERVAL
from custom_components.example.coordinator import ExampleCoordinator


async def test_update_data_returns_the_demo_payload(hass, mock_config_entry) -> None:
    """The placeholder payload is shaped the way the sensor platform expects."""
    coordinator = ExampleCoordinator(hass, mock_config_entry)

    data = await coordinator._async_update_data()

    assert data["status"] == {"code": "status", "value": "ok", "source": "cloud"}
    assert data["power"]["value"] == 0.0
    assert data["power"]["unit"] == "W"
    assert data["power"]["source"] == "cloud"


def test_scan_interval_comes_from_constants(hass, mock_config_entry) -> None:
    """The poll interval is driven by DEFAULT_SCAN_INTERVAL."""
    coordinator = ExampleCoordinator(hass, mock_config_entry)

    assert coordinator.update_interval is not None
    assert coordinator.update_interval.total_seconds() == DEFAULT_SCAN_INTERVAL
    assert coordinator.entry is mock_config_entry
