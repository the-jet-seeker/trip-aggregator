from datetime import datetime
from decimal import Decimal

import pytest

from trip_aggregator import models


@pytest.fixture()
def empty_tickets() -> None:
    with models.Session() as session:
        session.execute(
            models.Ticket.delete()
        )
        session.commit()

    yield


@pytest.fixture()
def ticket() -> models.Ticket:
    ticket = models.Ticket(
        dep_datetime=datetime(2024, 1, 6, 0, 0, 0, tzinfo=None),
        arr_datetime=datetime(2024, 1, 6, 1, 10, 0, tzinfo=None),
        from_airport_code='PRG',
        to_airport_code='BCN',
        flight_duration='1:10',
        flight_number='test123',
        airline='TestWings',
        price=Decimal('10'),
        currency='czk',
        source='azair',
    )

    with models.Session() as session:
        session.add(ticket)
        session.commit()

    yield ticket

    with models.Session() as session:
        session.execute(
            models.Ticket.delete().where(
                models.Ticket.id == ticket.id
            )
        )
        session.commit()
