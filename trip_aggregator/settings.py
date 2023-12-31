"""Application settings."""
import os
from decimal import getcontext

from pydantic import Field
from pydantic_settings import BaseSettings

getcontext().prec = 2

APP_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
    ),
)


class AppSettings(BaseSettings, extra='ignore'):
    """Application settings class."""

    DEBUG: bool = Field(default=False)
    DATABASE_USER: str = Field(default='root')
    DATABASE_PASSWORD: str = Field(default='root')
    DATABASE_NAME: str = Field(default='the-jet-seeker')
    DATABASE_HOST: str = Field(default='localhost')
    DATABASE_PORT: int = Field(default=5432)

    HOME_AIRPORT: str = Field(default='PRG', description='department airport code')
    HOME_TIMEZONE: str = Field(default='Europe/Prague', description='local timezone')

    MINIMAL_TRIP_DURATION: int = Field(
        default=18 * 60 * 60,
        description='time between department and arrival time in seconds',
    )


app_settings = AppSettings(
    _env_file=os.path.join(APP_PATH, '.env'),  # type:ignore
)
