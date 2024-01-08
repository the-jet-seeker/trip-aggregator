from unittest.mock import Mock

from trip_aggregator import models
from trip_aggregator.run_task import _weekend_interval, _get_tickets
from trip_aggregator.settings import app_settings


def test_get_tickets_smoke(mocker):
    tickets = [
        Mock(
            from_airport_code=app_settings.HOME_AIRPORT,
            flight_number='test_ticket_from_home'
        ),
        Mock(
            to_airport_code=app_settings.HOME_AIRPORT,
            flight_number='test_ticket_to_home'

        ),
    ]
    mocker.patch('trip_aggregator.run_task.fetch_tickets', return_value=tickets)
    weekend_date = _weekend_interval()

    outbound, inbound = _get_tickets(weekend_date, app_settings.HOME_AIRPORT)

    assert isinstance(outbound, list)
    assert isinstance(inbound, list)
    assert len(outbound) == 1
    assert len(inbound) == 1
    assert outbound[0].from_airport_code == app_settings.HOME_AIRPORT
    assert inbound[0].to_airport_code == app_settings.HOME_AIRPORT
