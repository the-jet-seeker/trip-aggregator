"""Updater of trips from the tickets database."""
import logging
from dataclasses import dataclass

from trip_aggregator.settings import app_settings

logger = logging.getLogger(__file__)


@dataclass
class TripsUpdateResult:
    """Trips updater task results representation."""

    is_success: bool
    trips_found: int = 0


def main() -> TripsUpdateResult:
    """Generate new possible trips by tickets from db."""
    # todo impl
    # todo test
    return TripsUpdateResult(
        is_success=True,
        trips_found=1,
    )


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.DEBUG else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )
    main()
