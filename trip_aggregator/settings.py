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

    COAST_OF_LEAVING_DATA: dict[str, tuple[int, int]] = {
        'PRG': (2438, 200),
        'BCN': (3615, 504),
        'AMS': (3615, 504),
        'STN': (3615, 504),
        'NAP': (3615, 504),
        'MAN': (3615, 504),
        'DUB': (3615, 504),
        'BUD': (3615, 504),
        'KRK': (3615, 504),
        'KUT': (3615, 504),
        'CPH': (3615, 504),
        'CDG': (3615, 504),
        'EDI': (3615, 504),
        'RIX': (3615, 504),
        'GDN': (3615, 504),
        'CTA': (3615, 504),
        'ALC': (3615, 504),
        'BRI': (3615, 504),
        'LPA': (3615, 504),
        'KSC': (3615, 504),
        'RMI': (3615, 504),
        'OSL': (3615, 504),
        'FCO': (3615, 504),
        'DXB': (3615, 504),
        'PMI': (3615, 504),
        'BVA': (3615, 504),
        'VCE': (3615, 504),
        'HRG': (3615, 504),
        'OTP': (3615, 504),
        'BHX': (3615, 504),
        'TIA': (3615, 504),
        'ATH': (3615, 504),
        'ZAD': (3615, 504),
        'TLV': (3615, 504),
        'MXP': (3615, 504),
        'PSA': (3615, 504),
        'BSL': (3615, 504),
        'OPO': (3615, 504),
        'DUS': (3615, 504),
        'EIN': (3615, 504),
        'MRS': (3615, 504),
        'MAD': (3615, 504),
        'LGW': (3615, 504),
        'RHO': (3615, 504),
        'LYS': (3615, 504),
        'BLQ': (3615, 504),
        'FLR': (3615, 504),
        'FNC': (3615, 504),
        'ORY': (3615, 504),
        'BGY': (3615, 504),
        'TSF': (3615, 504),
        'VLC': (3615, 504),
        'LIS': (3615, 504),
        'LTN': (3615, 504),
        'BRS': (3615, 504),
        'BOD': (3615, 504),
        'VRN': (3615, 504),
        'TFS': (3615, 504),
        'PSR': (3615, 504),
        'GVA': (3615, 504),
        'LCA': (3615, 504),
        'ARN': (3615, 504),
        'RMF': (3615, 504),
        'NTE': (3615, 504),
        'SAW': (3615, 504),
        'CRL': (3615, 504),
        'AGP': (3615, 504),
        'GOT': (3615, 504),
        'SVQ': (3615, 504),
    }


app_settings = AppSettings(
    _env_file=os.path.join(APP_PATH, '.env'),  # type:ignore
)
