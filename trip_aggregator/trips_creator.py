"""Methods to create trips from tickets."""
from trip_aggregator import types


def create_trips(outbound_tickets: list[types.Ticket], inbound_tickets: list[types.Ticket]) -> list[types.Trip]:
    """Create list of trips from lists of outbound and inbound tickets."""
    trips = []

    for outbound_ticket in outbound_tickets:
        for inbound_ticket in inbound_tickets:
            if outbound_ticket.to_airport_code == inbound_ticket.from_airport_code:
                trips.append(
                    types.Trip(
                        start_date=outbound_ticket.dep_datetime,
                        end_date=inbound_ticket.dep_datetime,
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
