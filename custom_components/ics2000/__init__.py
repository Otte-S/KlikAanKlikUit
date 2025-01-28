from homeassistant.core import HomeAssistant
DOMAIN = "ics2000"

async def async_setup(hass: HomeAssistant, config: dict):
    """Setup van de integratie."""
    hass.states.async_set(f"{DOMAIN}.status", "Actief")
    return True
