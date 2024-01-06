from unittest.mock import Mock

from trip_aggregator import models
from trip_aggregator.trips_creator import _make_trip


def test_make_trip_smoke():
    outbound_ticket = Mock(
        currency='CZK',
    )
    inbound_ticket = Mock(
        currency='CZK',
    )

    res = _make_trip(outbound_ticket, inbound_ticket)

    assert isinstance(res, models.Trip)
