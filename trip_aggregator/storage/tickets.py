import pendulum
from sqlalchemy import or_

from trip_aggregator import models
from trip_aggregator.models import Session
from trip_aggregator.types import Ticket


def get_tickets(weekend_date: pendulum.Interval, home_airport: str) -> tuple[list[Ticket]]:
    """Get tickets from db. Return two lists with inbound tickets and outbound one."""
    # todo impl
    # todo test

    outbound_tickets = []
    inbound_tickets = []

    return outbound_tickets, inbound_tickets


def _fetch_tickets(
    weekend_date: pendulum.Interval,
    home_airport: str,
) -> list[Ticket]:
    """Fetch all tickets from home airport at the selected weekend from db."""
    with Session() as session:
        query = (
            models.Ticket.select().where(
                models.Ticket.dep_datetime >= weekend_date.start,
            ).where(
                models.Ticket.dep_datetime <= weekend_date.end, # todo arrival time
            ).where(
                or_(
                    models.Ticket.from_airport_code == home_airport,
                    models.Ticket.to_airport_code == home_airport,
                )
            )
        )
        return session.scalars(query).all()  # type: ignore