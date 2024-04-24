"""Calculate data connected with coast of leaving."""

from dataclasses import dataclass

from trip_aggregator.settings import app_settings


@dataclass
class CoastOfLeaving:
    """Type with the prices for one city."""

    night: int
    meal: int


def get_cost_of_leaving(airport: str) -> CoastOfLeaving | None:
    """Return the price of one night in destination place."""
    if airport in app_settings.COAST_OF_LEAVING_DATA:
        return CoastOfLeaving(
            app_settings.COAST_OF_LEAVING_DATA[airport][0],
            app_settings.COAST_OF_LEAVING_DATA[airport][1],
        )

    return None
