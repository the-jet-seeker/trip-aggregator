from datetime import datetime

from trip_aggregator.trips_creator import _trip_duration_nights


def test_trip_duration_nights_0():
    dep_datetime = datetime(2024, 1, 31, 18, 30, 0, tzinfo=None)
    arr_datetime = datetime(2024, 1, 31, 23, 0, 0, tzinfo=None)

    res = _trip_duration_nights(dep_datetime, arr_datetime)

    assert res == 0


def test_trip_duration_nights_1():
    dep_datetime = datetime(2024, 1, 31, 18, 30, 0, tzinfo=None)
    arr_datetime = datetime(2024, 2, 1, 17, 0, 0, tzinfo=None)

    res = _trip_duration_nights(dep_datetime, arr_datetime)

    assert res == 1

def test_trip_duration_nights_2():
    dep_datetime = datetime(2024, 1, 31, 18, 30, 0, tzinfo=None)
    arr_datetime = datetime(2024, 2, 2, 17, 0, 0, tzinfo=None)

    res = _trip_duration_nights(dep_datetime, arr_datetime)

    assert res == 2
