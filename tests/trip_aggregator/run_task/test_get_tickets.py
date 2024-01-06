from trip_aggregator import models
from trip_aggregator.run_task import _weekend_interval, _get_tickets
from trip_aggregator.settings import app_settings


def test_get_tickets_smoke():
    # todo видимо надо замокировать что то
    weekend_date = _weekend_interval()

    res = _get_tickets(weekend_date, app_settings.HOME_AIRPORT)

    assert isinstance(res, tuple)
    assert isinstance(res[0], list)
    assert isinstance(res[0][0], models.Ticket)
