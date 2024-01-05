from trip_aggregator.run_task import _calculate_weekend_interval
from trip_aggregator.settings import app_settings
from trip_aggregator.storage.tickets import _fetch_tickets


def test_fetch_tickets_smoke():
    weekend_date = _calculate_weekend_interval()
    home_airport = app_settings.HOME_AIRPORT

    res = _fetch_tickets(weekend_date, home_airport)

    assert isinstance(res, list)
    #assert isinstance(res[0], models.Ticket)
