"""Methods for getting tickets from db."""
import pendulum
from sqlalchemy import or_

from trip_aggregator import models


def fetch_tickets(
    weekend_date: pendulum.Interval,
    home_airport: str,
) -> list[models.Ticket]:
    """Fetch all tickets from home airport at the selected weekend from db."""
    with models.Session() as session:
        query = (
            models.Ticket.select().where(
                models.Ticket.dep_datetime >= weekend_date.start.naive(),  # type: ignore
            ).where(
                models.Ticket.arr_datetime <= weekend_date.end.naive(),  # type: ignore
            ).where(
                or_(
                    models.Ticket.from_airport_code == home_airport,
                    models.Ticket.to_airport_code == home_airport,
                ),
            )
        )
        return session.scalars(query).all()  # type: ignore
