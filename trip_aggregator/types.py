"""Whole project types."""
from dataclasses import dataclass
from decimal import Decimal

import pendulum


@dataclass
class Ticket:
    """Type of the one ticket."""

    dep_datetime: pendulum.DateTime
    from_airport_code: str
    to_airport_code: str
    flight_duration: str
    flight_number: str
    airline: str
    price: Decimal
    currency: str


@dataclass
class Trip:
    """Type of the one trip."""
    # todo
