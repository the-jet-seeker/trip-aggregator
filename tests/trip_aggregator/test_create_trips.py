from decimal import Decimal
from unittest.mock import Mock

from pendulum import DateTime

from trip_aggregator import models
from trip_aggregator.trips_creator import create_trips


def test_create_trips_happy_path():

    outbound_tickets = [
        Mock(
            dep_datetime=DateTime(2024, 1, 5, 0, 0, 0, tzinfo=None),
            arr_datetime=DateTime(2024, 1, 5, 1, 10, 0, tzinfo=None),
            from_airport_code='PRG',
            to_airport_code='BCN',
            flight_duration='1:10',
            flight_number='test123',
            airline='TestWings',
            price=Decimal('10'),
            currency='CZK',
        ),
        Mock(
            dep_datetime=DateTime(2024, 1, 6, 0, 0, 0, tzinfo=None),
            arr_datetime=DateTime(2024, 1, 6, 1, 10, 0, tzinfo=None),
            from_airport_code='PRG',
            to_airport_code='BUD',
            flight_duration='1:10',
            flight_number='testFR4092',
            airline='TestRyanair',
            price=Decimal('123456789012345678.12'),
            currency='CZK',
        ),
        Mock(
            dep_datetime=DateTime(2024, 1, 6, 0, 0, 0, tzinfo=None),
            arr_datetime=DateTime(2024, 1, 6, 4, 10, 0, tzinfo=None),
            from_airport_code='PRG',
            to_airport_code='LED',
            flight_duration='4:10',
            flight_number='testFR4092',
            airline='TestRyanair',
            price=Decimal('123456789012345678.12'),
            currency='CZK',
        ),
        Mock(
            dep_datetime=DateTime(2024, 1, 6, 3, 15, 0, tzinfo=None),
            arr_datetime=DateTime(2024, 1, 6, 4, 25, 0, tzinfo=None),
            from_airport_code='PRG',
            to_airport_code='BUD',
            flight_duration='1:10',
            flight_number='testFR4092',
            airline='TestRyanair',
            price=Decimal('30'),
            currency='CZK',
        ),
    ]
    inbound_tickets = [
        Mock(
            dep_datetime=DateTime(2024, 1, 7, 0, 0, 0, tzinfo=None),
            arr_datetime=DateTime(2024, 1, 7, 1, 10, 0, tzinfo=None),
            from_airport_code='BCN',
            to_airport_code='PRG',
            flight_duration='1:10',
            flight_number='test123',
            airline='TestWings',
            price=Decimal('10'),
            currency='CZK',
        ),
        Mock(
            dep_datetime=DateTime(2024, 1, 8, 0, 0, 0, tzinfo=None),
            arr_datetime=DateTime(2024, 1, 8, 1, 10, 0, tzinfo=None),
            from_airport_code='BUD',
            to_airport_code='PRG',
            flight_duration='1:10',
            flight_number='testFR4092',
            airline='TestRyanair',
            price=Decimal('123456789012345678.12'),
            currency='CZK',
        ),
        Mock(
            dep_datetime=DateTime(2024, 1, 8, 2, 10, 0, tzinfo=None),
            arr_datetime=DateTime(2024, 1, 8, 4, 20, 0, tzinfo=None),
            from_airport_code='MAD',
            to_airport_code='PRG',
            flight_duration='2:10',
            flight_number='testFR4092',
            airline='TestRyanair',
            price=Decimal('400'),
            currency='CZK',
        ),
    ]

    res = create_trips(outbound_tickets, inbound_tickets)

    assert len(res) == 3
    assert res[0].start_date == DateTime(2024, 1, 5, 0, 0, 0, tzinfo=None)
    assert res[0].end_date == DateTime(2024, 1, 7, 1, 10, 0, tzinfo=None)
    assert res[0].currency == 'CZK'

    assert res[0].outbound_cost == Decimal('10')
    assert res[0].outbound_airport == 'PRG'
    assert res[0].outbound_airline == 'TestWings'
    assert res[0].outbound_fly_number == 'test123'

    assert res[0].return_cost == Decimal('10')
    assert res[0].return_airport == 'BCN'
    assert res[0].return_airline == 'TestWings'
    assert res[0].return_fly_number == 'test123'

    assert res[1].outbound_airport == 'PRG'
    assert res[1].return_airport == 'BUD'

    assert res[2].outbound_airport == 'PRG'
    assert res[2].return_airport == 'BUD'
