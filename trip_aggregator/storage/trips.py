"""Methods of interaction with the long-term trips storage subsystem."""
import pendulum

from trip_aggregator import types
from trip_aggregator.types import Ticket


def replace_trips(trips: list[types.Trip], weekend_date: pendulum.Interval) -> int:
    """Save list of trips to the database."""
    #todo impl
    #todo  test
    ...

