"""Constants for the Tesla Powerwall integration."""
from typing import Final

DOMAIN = "powerwall"

POWERWALL_BASE_INFO: Final = "base_info"
POWERWALL_COORDINATOR: Final = "coordinator"
POWERWALL_API_CHANGED: Final = "api_changed"
POWERWALL_HTTP_SESSION: Final = "http_session"
POWERWALL_LOGIN_FAILED_COUNT: Final = "login_failed_count"

UPDATE_INTERVAL = 30

ATTR_FREQUENCY = "frequency"
ATTR_INSTANT_AVERAGE_VOLTAGE = "instant_average_voltage"
ATTR_INSTANT_TOTAL_CURRENT = "instant_total_current"
ATTR_IS_ACTIVE = "is_active"

MODEL = "PowerWall 2"
MANUFACTURER = "Tesla"
