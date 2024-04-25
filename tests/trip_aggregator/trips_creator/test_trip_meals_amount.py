from datetime import datetime

from trip_aggregator.trips_creator import _trip_meals_amount


def test_trip_meals_amount():
    dep_datetime = datetime(2024, 1, 31, 0, 0, 0, tzinfo=None)
    arr_datetime = datetime(2024, 2, 1, 0, 30, 0, tzinfo=None)

    res = _trip_meals_amount(dep_datetime, arr_datetime)

    assert res == 4
