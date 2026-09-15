"""Fixtures for the example integration tests."""

from __future__ import annotations

from typing import Any

import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.example.const import DOMAIN

HOST = "192.0.2.1"

# Representative coordinator payload: one point per entity, tagged with the
# transport it came from.
PAYLOAD: dict[str, Any] = {
    "status": {"code": "status", "value": "ok", "source": "cloud"},
    "power": {"code": "power", "value": 1.0, "unit": "W", "source": "cloud"},
}


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations: Any) -> Any:
    """Load the custom integration in every test.

    Without this fixture Home Assistant refuses to set up anything under
    ``custom_components/`` and setup fails with "Integration not found".
    """
    yield


@pytest.fixture
def mock_config_entry() -> MockConfigEntry:
    """Return a mock config entry."""
    return MockConfigEntry(
        domain=DOMAIN,
        data={"host": HOST},
        unique_id=HOST,
        title=f"Example ({HOST})",
    )
