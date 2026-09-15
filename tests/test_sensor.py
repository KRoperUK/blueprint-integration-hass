"""Tests for the example sensor platform."""

from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock

import pytest

from custom_components.example.sensor import ExamplePowerSensor

from .conftest import PAYLOAD


def _coordinator(data: Any) -> MagicMock:
    coordinator = MagicMock()
    coordinator.data = data
    return coordinator


def _build(entry: Any, data: Any) -> ExamplePowerSensor:
    return ExamplePowerSensor(_coordinator(data), entry)


def test_native_value(mock_config_entry) -> None:
    """The power reading is coerced to a float."""
    assert _build(mock_config_entry, PAYLOAD).native_value == 1.0


@pytest.mark.parametrize("data", [None, {}, {"power": None}])
def test_native_value_without_a_power_point(mock_config_entry, data) -> None:
    """A missing power point yields None."""
    assert _build(mock_config_entry, data).native_value is None


@pytest.mark.parametrize("value", ["not-a-number", None, object()])
def test_native_value_with_an_unusable_value(mock_config_entry, value) -> None:
    """A malformed value degrades to None instead of raising."""
    assert _build(mock_config_entry, {"power": {"value": value}}).native_value is None


def test_extra_state_attributes_expose_transport(mock_config_entry) -> None:
    """Provenance is surfaced when the payload carries a source."""
    assert _build(mock_config_entry, PAYLOAD).extra_state_attributes == {"source": "cloud"}


@pytest.mark.parametrize("data", [None, {}, {"power": {"value": 1.0}}])
def test_extra_state_attributes_without_a_source(mock_config_entry, data) -> None:
    """No source means no attributes."""
    assert _build(mock_config_entry, data).extra_state_attributes is None


def test_unique_id_and_device_info(mock_config_entry) -> None:
    """The entity is namespaced by the entry unique id and exposes device info."""
    sensor = _build(mock_config_entry, PAYLOAD)

    assert sensor.unique_id == f"{mock_config_entry.unique_id}_power"
    assert sensor.device_info is not None
    assert sensor.device_info["manufacturer"] == "Example"
