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
    start_date: pendulum.DateTime
    end_date: pendulum.DateTime
    currency: str

    outbound_cost: Decimal
    outbound_airport: str
    outbound_airline: str
    outbound_fly_number: str

    return_cost: Decimal
    return_airport: str
    return_airline: str
    return_fly_number: str

