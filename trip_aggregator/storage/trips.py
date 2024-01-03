"""Methods of interaction with the long-term trips storage subsystem."""
import dataclasses

import pendulum

from trip_aggregator import types, models


def replace_trips(trips: list[types.Trip], weekend_date: pendulum.Interval) -> int:
    """Save list of trips to the database."""
    with models.Session() as session:
        session.execute(
            models.Trip.delete().where(
                models.Trip.start_date >= weekend_date.start,
            ),
        )

        for trip in trips:
            trip_model = models.Trip(
                **dataclasses.asdict(trip),
            )

            session.add(trip_model)
        session.commit()

    return len(trips)
