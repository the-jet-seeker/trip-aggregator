"""Methods to create trips from tickets."""
import logging

from trip_aggregator import models

logger = logging.getLogger(__file__)


def create_trips(outbound_tickets: list[models.Ticket], inbound_tickets: list[models.Ticket]) -> list[models.Trip]:
    """Create list of trips from lists of outbound and inbound tickets."""
    trips = []

    for outbound_ticket in outbound_tickets:
        for inbound_ticket in inbound_tickets:

            if outbound_ticket.to_airport_code == inbound_ticket.from_airport_code:

                if outbound_ticket.currency != inbound_ticket.currency:
                    logger.warning(
                        f'Different currencies.\nOutbound - {outbound_ticket.currency}\ninbound - {inbound_ticket.currency}',
                    )

                trips.append(
                    models.Trip(
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
                    ),
                )

    return trips
