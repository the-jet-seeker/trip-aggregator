"""Updater of trips from the tickets database."""
import logging
from dataclasses import dataclass

import pendulum

from trip_aggregator import models
from trip_aggregator.settings import app_settings
from trip_aggregator.storage.tickets import fetch_tickets
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
    weekend_date = _weekend_interval()
    outbound_tickets, inbound_tickets = _get_tickets(weekend_date, app_settings.HOME_AIRPORT)

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


def _weekend_interval() -> pendulum.Interval:
    """Calculate date interval for the weekend trips."""
    current_date = pendulum.now(app_settings.HOME_TIMEZONE)

    outbound_date = current_date.next(
        pendulum.MONDAY,
    ).next(
        pendulum.FRIDAY,
    ).naive()
    inbound_date = outbound_date.next(
        pendulum.MONDAY,
    ).add(
        hours=23,
        minutes=59,
        seconds=59,
    ).naive()

    return pendulum.Interval(outbound_date, inbound_date)


def _get_tickets(
    weekend_date: pendulum.Interval,
    home_airport: str,
) -> tuple[list[models.Ticket], list[models.Ticket]]:
    """Get tickets from db. Return two lists with inbound tickets and outbound one."""
    # todo test
    outbound_tickets = []
    inbound_tickets = []
    tickets = fetch_tickets(weekend_date, home_airport)

    for ticket in tickets:
        if ticket.from_airport_code == home_airport:
            outbound_tickets.append(ticket)
        elif ticket.to_airport_code == home_airport:
            inbound_tickets.append(ticket)

    return outbound_tickets, inbound_tickets


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.DEBUG else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )
    main()
