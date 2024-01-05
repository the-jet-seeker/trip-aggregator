"""Methods for getting tickets from db."""
import pendulum
from sqlalchemy import or_

from trip_aggregator import models


def get_tickets(
    weekend_date: pendulum.Interval,
    home_airport: str,
) -> tuple[list[models.Ticket], list[models.Ticket]]:
    """Get tickets from db. Return two lists with inbound tickets and outbound one."""
    # todo impl  убрать из папки сторадж
    # todo test
    outbound_tickets = []
    inbound_tickets = []
    tickets = _fetch_tickets(weekend_date, home_airport)

    for ticket in tickets:
        if ticket.from_airport_code == home_airport:
            outbound_tickets.append(ticket)
        elif ticket.to_airport_code == home_airport:
            inbound_tickets.append(ticket)

    return outbound_tickets, inbound_tickets


def _fetch_tickets(
    weekend_date: pendulum.Interval,
    home_airport: str,
) -> list[models.Ticket]:
    """Fetch all tickets from home airport at the selected weekend from db."""
    # todo test happy path
    with models.Session() as session:
        query = (
            models.Ticket.select().where(
                models.Ticket.dep_datetime >= weekend_date.start,
            ).where(
                models.Ticket.arr_datetime <= weekend_date.end,
            ).where(
                or_(
                    models.Ticket.from_airport_code == home_airport,
                    models.Ticket.to_airport_code == home_airport,
                ),
            )
        )
        return session.scalars(query).all()  # type: ignore
