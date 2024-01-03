"""Updater of trips from the tickets database."""
import logging
from dataclasses import dataclass

import pendulum

from trip_aggregator.settings import app_settings
from trip_aggregator.storage.tickets import get_tickets
from trip_aggregator.storage.trips import replace_trips
from trip_aggregator.trips_creator import create_trips

logger = logging.getLogger(__file__)


@dataclass
class TripsUpdateResult:
    """Trips updater task results representation."""

    is_success: bool
    weekend_date: pendulum.Interval
    trips_found: int = 0


def main() -> TripsUpdateResult:
    """Generate new possible trips by tickets from db."""
    # todo test
    weekend_date = _calculate_weekend_interval()
    outbound_tickets, inbound_tickets = get_tickets(weekend_date, app_settings.HOME_AIRPORT)

    trips = create_trips(outbound_tickets, inbound_tickets)

    if trips:
        saved_trips = replace_trips(trips, weekend_date)

        logger.info(f'{saved_trips} trips saved.')
    else:
        logger.warning('Trips not found.')

    return TripsUpdateResult(
        is_success=True,
        weekend_date=weekend_date,
        trips_found=len(trips),
    )


def _calculate_weekend_interval() -> pendulum.Interval:
    """Calculate date interval for the weekend trips."""
    # todo test
    # todo imp
    current_date = pendulum.now(app_settings.HOME_TIMEZONE)

    outbound_date = current_date.add(days=7).next(pendulum.FRIDAY).naive()
    inbound_date = outbound_date.next(pendulum.SUNDAY).naive()
    #todo перепиасать тут не то должен выбирать понедельник до полуночи

    return pendulum.Interval(outbound_date, inbound_date)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.DEBUG else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )
    main()
