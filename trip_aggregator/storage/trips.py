"""Methods of interaction with the long-term trips storage subsystem."""
import pendulum

from trip_aggregator import models


def replace_trips(trips: list[models.Trip], weekend_date: pendulum.Interval) -> int:
    """Save list of trips to the database."""
    with models.Session() as session:
        session.execute(
            models.Trip.delete().where(
                models.Trip.start_date >= weekend_date.start,
            ),
        )

        for trip in trips:
            session.add(trip)
        session.commit()

    return len(trips)
