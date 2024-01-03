import pendulum

from trip_aggregator.types import Ticket


def get_tickets(weekend_date: pendulum.Interval, home_airport: str) -> tuple[list[Ticket]]:
    """Get tickets from db. Return two lists with inbound tickets and outbound one."""
    # todo impl
    # todo test

    outbound_tickets = []
    inbound_tickets = []

    return outbound_tickets, inbound_tickets


