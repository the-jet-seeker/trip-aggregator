from datetime import datetime
from unittest.mock import Mock

import pytest

from trip_aggregator import models
from trip_aggregator.trips_creator import _make_trip


def test_make_trip_smoke():
    outbound_ticket = Mock(
        currency='CZK',
        dep_datetime = datetime(2024, 1, 31, 18, 30, 0, tzinfo=None),
    )
    inbound_ticket = Mock(
        currency='CZK',
        arr_datetime=datetime(2024, 1, 31, 23, 0, 0, tzinfo=None),
        from_airport_code='PRG',
    )

    res = _make_trip(outbound_ticket, inbound_ticket)

    assert isinstance(res, models.Trip)


def test_make_trip_different_currencies():
    outbound_ticket = Mock(
        currency='CZK',
    )
    inbound_ticket = Mock(
        currency='EUR',
    )

    with pytest.raises(RuntimeError):
        _make_trip(outbound_ticket, inbound_ticket)
