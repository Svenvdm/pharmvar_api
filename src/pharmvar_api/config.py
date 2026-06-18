from typing import Final
from dataclasses import dataclass

@dataclass(frozen=True)
class APIConfig:
    """API Configuration settings"""
    DEFAULT_HOST: Final[str] = "www.pharmvar.org/api-service"
    DEFAULT_VERSION: Final[str] = "0.2"
    DEFAULT_SSL_VERIFY: Final[bool] = True
    DEFAULT_LOGGER = None
    DEFAULT_API_KEY: Final[str] = ""
    DEFAULT_HEADER_ACCEPT: Final[str] = "*/*"

@dataclass(frozen=True)
class LogConfig:
    """Logging Configuration settings"""
    DEFAULT_LOG_LEVEL: Final[str] = "INFO"
    DEFAULT_LOG_FORMAT: Final[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

@dataclass(frozen=True)
class CacheSettings:
    "Cache configuration settings"
    DEFAULT_CACHE_NAME: Final[str] = "pharmvar_api_cache"
    DEFAULT_CACHE_BACKEND: Final[str] = "sqlite"
    DEFAULT_EXPIRY_TIME: Final[int] = 3600  # seconds
    DEFAULT_ALLOWABLE_METHODS: Final[list] = ("GET")
    DEFAULT_ALLOWABLE_CODES: Final[list] = (200,)

# Rate limiting
RATE_LIMIT: Final[int] = 120 # requests per minute
