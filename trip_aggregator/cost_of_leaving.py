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
    cost_data = app_settings.COAST_OF_LEAVING_DATA.get(airport)
    if cost_data is None:
        return None

    return CoastOfLeaving(
        cost_data[0],
        cost_data[1],
    )
