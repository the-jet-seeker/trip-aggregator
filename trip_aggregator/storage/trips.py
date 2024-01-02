"""Methods of interaction with the long-term trips storage subsystem."""
import pendulum

from trip_aggregator import types
from trip_aggregator.types import Ticket


def replace_trips(trips: list[types.Trip], weekend_date: pendulum.Interval) -> int:
    """Save list of trips to the database."""
    #todo impl
    #todo  test
    ...


def get_tickets(weekend_date: pendulum.Interval, home_airport: str) -> list[Ticket]:
    """Get tickets from db. Return two lists with inbound tickets and outbound one."""
    # todo impl
    # todo test

