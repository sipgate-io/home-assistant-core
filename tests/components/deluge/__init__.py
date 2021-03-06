"""Tests for the Deluge integration."""

from homeassistant.components.deluge.const import (
    CONF_WEB_PORT,
    DEFAULT_RPC_PORT,
    DEFAULT_WEB_PORT,
)
from homeassistant.const import (
    CONF_HOST,
    CONF_MONITORED_VARIABLES,
    CONF_NAME,
    CONF_PASSWORD,
    CONF_PORT,
    CONF_USERNAME,
)

CONF_DATA = {
    CONF_HOST: "1.2.3.4",
    CONF_USERNAME: "user",
    CONF_PASSWORD: "password",
    CONF_PORT: DEFAULT_RPC_PORT,
    CONF_WEB_PORT: DEFAULT_WEB_PORT,
}

IMPORT_DATA = {
    CONF_HOST: "1.2.3.4",
    CONF_NAME: "Deluge Torrent",
    CONF_MONITORED_VARIABLES: ["current_status", "download_speed", "upload_speed"],
    CONF_USERNAME: "user",
    CONF_PASSWORD: "password",
    CONF_PORT: DEFAULT_RPC_PORT,
}
