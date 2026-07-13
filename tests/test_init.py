"""Tests for integration setup."""

from unittest.mock import patch

import pytest
from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.example.const import DOMAIN


@pytest.mark.asyncio
async def test_setup_and_unload(hass: HomeAssistant, mock_config_entry: MockConfigEntry) -> None:
    """Config entry sets up platforms and unloads cleanly."""
    mock_config_entry.add_to_hass(hass)
    with patch(
        "custom_components.example.coordinator.ExampleCoordinator._async_update_data",
        return_value={"power": {"value": 1.0, "unit": "W", "source": "cloud"}},
    ):
        assert await hass.config_entries.async_setup(mock_config_entry.entry_id)
        await hass.async_block_till_done()
        assert mock_config_entry.domain == DOMAIN
        assert await hass.config_entries.async_unload(mock_config_entry.entry_id)
