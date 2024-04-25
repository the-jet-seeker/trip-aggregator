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
    BETWEEN_MEAL_INTERVAL: int = Field(
        default=6,
        description='time between one food and the next one during the trip.',
    )

    COAST_OF_LEAVING_DATA: dict[str, tuple[int, int]] = {
        'PRG': (2438, 200),
        'BCN': (3135, 380),
        'AMS': (4731, 506),
        'STN': (6555, 585),
        'NAP': (1797, 380),
        'MAN': (3428, 440),
        'DUB': (5131, 506),
        'BUD': (1480, 257),
        'KRK': (2224, 234),
        'KUT': (790, 199),
        'CPH': (4096, 508),
        'CDG': (3569, 455),
        'EDI': (3723, 440),
        'RIX': (1235, 253),
        'GDN': (2262, 234),
        'CTA': (1155, 304),
        'ALC': (2172, 329),
        'BRI': (1898, 380),
        'LPA': (1708, 259),
        'KSC': (1536, 177),
        'RMI': (1630, 418),
        'OSL': (3310, 496),
        'FCO': (2702, 380),
        'DXB': (5186, 258),
        'PMI': (2578, 329),
        'BVA': (3569, 455),
        'VCE': (2488, 430),
        'HRG': (348, 99),
        'OTP': (1313, 254),
        'BHX': (2850, 440),
        'TIA': (1308, 250),
        'ATH': (1463, 380),
        'ZAD': (1334, 268),
        'TLV': (4116, 472),
        'MXP': (3623, 506),
        'PSA': (1602, 354),
        'BSL': (4395, 650),
        'OPO': (2413, 228),
        'DUS': (2274, 380),
        'EIN': (3560, 380),
        'MRS': (1952, 354),
        'MAD': (3026, 354),
        'LGW': (6555, 586),
        'RHO': (1265, 253),
        'LYS': (2267, 380),
        'BLQ': (2486, 506),
        'FLR': (2485, 378),
        'FNC': (3125, 176),
        'ORY': (3569, 455),
        'BGY': (1603, 380),
        'TSF': (2614, 380),
        'VLC': (2484, 322),
        'LIS': (3373, 342),
        'LTN': (2966, 352),
        'BRS': (4013, 440),
        'BOD': (1990, 405),
        'VRN': (2150, 380),
        'TFS': (2277, 304),
        'PSR': (1488, 380),
        'GVA': (5435, 650),
        'LCA': (2475, 380),
        'ARN': (3620, 327),
        'NTE': (1680, 366),
        'SAW': (1753, 219),
        'CRL': (2683, 455),
        'AGP': (2356, 304),
        'GOT': (2490, 278),
        'SVQ': (2030, 304),
    }


app_settings = AppSettings(
    _env_file=os.path.join(APP_PATH, '.env'),  # type:ignore
)
