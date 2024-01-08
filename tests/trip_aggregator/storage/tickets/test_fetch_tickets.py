from datetime import timedelta

import pendulum

from trip_aggregator.run_task import _weekend_interval
from trip_aggregator.settings import app_settings
from trip_aggregator.storage.tickets import fetch_tickets


def test_fetch_tickets_happy_path(empty_tickets):
    res = fetch_tickets(_weekend_interval(), app_settings.HOME_AIRPORT)

    assert isinstance(res, list)
    assert len(res) == 0


def test_fetch_tickets(empty_tickets, ticket):
    res = fetch_tickets(
        pendulum.Interval(start=ticket.dep_datetime, end=ticket.arr_datetime),
        ticket.from_airport_code,
    )

    assert len(res) == 1
    assert res[0].id == ticket.id


def test_fetch_tickets_filter_dep_date(empty_tickets, ticket):
    res = fetch_tickets(
        pendulum.Interval(start=ticket.dep_datetime + timedelta(seconds=1), end=ticket.arr_datetime),
        ticket.from_airport_code,
    )

    assert len(res) == 0

def test_fetch_tickets_filter_arr_date(empty_tickets, ticket):
    pass


def test_fetch_tickets_filter_airport(empty_tickets, ticket):
    pass
