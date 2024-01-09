"""Methods to create trips from tickets."""
import logging

from trip_aggregator import models
from trip_aggregator.settings import app_settings

logger = logging.getLogger(__file__)


def create_trips(outbound_tickets: list[models.Ticket], inbound_tickets: list[models.Ticket]) -> list[models.Trip]:
    """Create list of trips from lists of outbound and inbound tickets."""
    all_trips = []

    for outbound_ticket in outbound_tickets:
        for inbound_ticket in inbound_tickets:

            if outbound_ticket.to_airport_code != inbound_ticket.from_airport_code:
                continue

            all_trips.append(_make_trip(outbound_ticket, inbound_ticket))

    return [
        trip
        for trip in all_trips
        if int((trip.end_date - trip.start_date).total_seconds()) >= app_settings.MINIMAL_TRIP_DURATION
    ]


def _make_trip(outbound_ticket: models.Ticket, inbound_ticket: models.Ticket) -> models.Trip:
    """Create a trip from two tickets."""
    if outbound_ticket.currency != inbound_ticket.currency:
        raise RuntimeError(
            f'Different currencies.\noutbound - {outbound_ticket.currency}\ninbound - {inbound_ticket.currency}',
        )

    return models.Trip(
        start_date=outbound_ticket.dep_datetime,
        end_date=inbound_ticket.arr_datetime,
        currency=outbound_ticket.currency,

        outbound_cost=outbound_ticket.price,
        outbound_airport=outbound_ticket.from_airport_code,
        outbound_airline=outbound_ticket.airline,
        outbound_fly_number=outbound_ticket.flight_number,

        return_cost=inbound_ticket.price,
        return_airport=inbound_ticket.from_airport_code,
        return_airline=inbound_ticket.airline,
        return_fly_number=inbound_ticket.flight_number,
    )
