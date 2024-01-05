from decimal import Decimal

import pendulum

from trip_aggregator import models
from trip_aggregator.run_task import _calculate_weekend_interval
from trip_aggregator.storage.trips import replace_trips


def test_replace_trips():
    weekend_date = _calculate_weekend_interval()
    trips = [
        models.Trip(
            start_date=pendulum.now(),
            end_date=pendulum.now().add(days=2),
            currency='CZK',

            outbound_cost=Decimal('10'),
            outbound_airport='PRG',
            outbound_airline='TestAir',
            outbound_fly_number='Test123',

            return_cost=Decimal('123456789012345678.12'),
            return_airport='BCN',
            return_airline='TestAirBack',
            return_fly_number='Test321',
        ),
        models.Trip(
            start_date=weekend_date.start,
            end_date=weekend_date.end,
            currency='CZK',

            outbound_cost=Decimal('100'),
            outbound_airport='PRG',
            outbound_airline='TestAir2',
            outbound_fly_number='Test1234',

            return_cost=Decimal('1'),
            return_airport='MAD',
            return_airline='TestAirBack',
            return_fly_number='Test4321',
        ),
    ]

    res = replace_trips(trips, weekend_date)

    assert res == 2


