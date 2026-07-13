"""Sensor platform for the example integration."""

from __future__ import annotations

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity, SensorStateClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfPower
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import ExampleCoordinator

PARALLEL_UPDATES = 0


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Example sensors."""
    coordinator: ExampleCoordinator = entry.runtime_data
    async_add_entities([ExamplePowerSensor(coordinator, entry)])


class ExamplePowerSensor(CoordinatorEntity[ExampleCoordinator], SensorEntity):
    """Example power sensor."""

    _attr_has_entity_name = True
    _attr_name = "Power"
    _attr_device_class = SensorDeviceClass.POWER
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfPower.WATT

    def __init__(self, coordinator: ExampleCoordinator, entry: ConfigEntry) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.unique_id}_power"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry.unique_id or entry.entry_id)},
            "name": entry.title,
            "manufacturer": "Example",
        }

    @property
    def native_value(self) -> float | None:
        """Return the power reading."""
        point = self.coordinator.data.get("power") if self.coordinator.data else None
        if not point:
            return None
        try:
            return float(point["value"])
        except (TypeError, ValueError, KeyError):
            return None

    @property
    def extra_state_attributes(self) -> dict[str, str] | None:
        """Expose transport provenance when present."""
        point = self.coordinator.data.get("power") if self.coordinator.data else None
        if point and point.get("source"):
            return {"source": str(point["source"])}
        return None
