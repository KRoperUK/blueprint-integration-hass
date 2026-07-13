"""Fixtures for the example integration tests."""

import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.example.const import DOMAIN


@pytest.fixture
def mock_config_entry() -> MockConfigEntry:
    """Return a mock config entry."""
    return MockConfigEntry(
        domain=DOMAIN,
        data={"host": "192.0.2.1"},
        unique_id="192.0.2.1",
        title="Example (192.0.2.1)",
    )
