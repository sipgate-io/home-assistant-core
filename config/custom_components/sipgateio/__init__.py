from homeassistant.components import webhook
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType


DOMAIN = "sipgateio"

DATA_SIPGATEIO_TOKEN = "sipgateio_token_id"
DATA_SIPGATEIO_TOKENID = "sipgateio_token"

CONF_SIPGATEIO_TOKEN = "token_id"
CONF_SIPGATEIO_TOKENID = "token"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """TODO: Write docs"""
    if DOMAIN not in config:
        return True

    conf = config[DOMAIN]
    hass.data[DATA_SIPGATEIO_TOKEN] = conf.get(CONF_SIPGATEIO_TOKEN)
    hass.data[DATA_SIPGATEIO_TOKENID] = conf.get(CONF_SIPGATEIO_TOKENID)
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configure based on config entry."""
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True
