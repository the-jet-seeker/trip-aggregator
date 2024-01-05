from trip_aggregator import models
from trip_aggregator.run_task import _weekend_interval
from trip_aggregator.settings import app_settings
from trip_aggregator.storage.tickets import get_tickets


def test_get_tickets_smoke():
    # todo видимо надо замокировать что то
    weekend_date = _weekend_interval()

    res = get_tickets(weekend_date, app_settings.HOME_AIRPORT)

    assert isinstance(res, tuple)
    assert isinstance(res[0], list)
    assert isinstance(res[0][0], models.Ticket)
