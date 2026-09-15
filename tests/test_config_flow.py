"""Tests for the example config flow."""

from __future__ import annotations

from homeassistant import config_entries
from homeassistant.const import CONF_HOST
from homeassistant.data_entry_flow import FlowResultType

from custom_components.example.const import DOMAIN

from .conftest import HOST


async def _start(hass):
    return await hass.config_entries.flow.async_init(DOMAIN, context={"source": config_entries.SOURCE_USER})


async def test_form_is_shown(hass) -> None:
    """The user step renders an empty form."""
    result = await _start(hass)

    assert result["type"] == FlowResultType.FORM
    assert result["step_id"] == "user"
    assert result["errors"] == {}


async def test_submitting_a_host_creates_the_entry(hass) -> None:
    """A host creates a config entry titled after it."""
    result = await _start(hass)

    result = await hass.config_entries.flow.async_configure(result["flow_id"], user_input={CONF_HOST: HOST})

    assert result["type"] == FlowResultType.CREATE_ENTRY
    assert result["title"] == f"Example ({HOST})"
    assert result["data"] == {CONF_HOST: HOST}


async def test_duplicate_host_aborts(hass, mock_config_entry) -> None:
    """A second entry for the same host aborts."""
    mock_config_entry.add_to_hass(hass)
    result = await _start(hass)

    result = await hass.config_entries.flow.async_configure(result["flow_id"], user_input={CONF_HOST: HOST})

    assert result["type"] == FlowResultType.ABORT
    assert result["reason"] == "already_configured"
