from decimal import Decimal

from pendulum import DateTime

from trip_aggregator import types
from trip_aggregator.trips_creator import create_trips
from trip_aggregator.types import Trip


def test_create_trips_happy_path():
    outbound_tickets = [
        types.Ticket(
            dep_datetime=DateTime(2024, 1, 5, 0, 0, 0, tzinfo=None),
            from_airport_code='PRG',
            to_airport_code='BCN',
            flight_duration='1:10',
            flight_number='test123',
            airline='TestWings',
            price=Decimal('10'),
            currency='CZK',
        ),
        types.Ticket(
            dep_datetime=DateTime(2024, 1, 6, 0, 0, 0, tzinfo=None),
            from_airport_code='PRG',
            to_airport_code='BUD',
            flight_duration='1:10',
            flight_number='testFR4092',
            airline='TestRyanair',
            price=Decimal('123456789012345678.12'),
            currency='CZK',
        ),
        types.Ticket(
            dep_datetime=DateTime(2024, 1, 6, 0, 0, 0, tzinfo=None),
            from_airport_code='PRG',
            to_airport_code='LED',
            flight_duration='4:10',
            flight_number='testFR4092',
            airline='TestRyanair',
            price=Decimal('123456789012345678.12'),
            currency='CZK',
        ),
        types.Ticket(
            dep_datetime=DateTime(2024, 1, 6, 3, 15, 0, tzinfo=None),
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
        types.Ticket(
            dep_datetime=DateTime(2024, 1, 7, 0, 0, 0, tzinfo=None),
            from_airport_code='BCN',
            to_airport_code='PRG',
            flight_duration='1:10',
            flight_number='test123',
            airline='TestWings',
            price=Decimal('10'),
            currency='CZK',
        ),
        types.Ticket(
            dep_datetime=DateTime(2024, 1, 8, 0, 0, 0, tzinfo=None),
            from_airport_code='BUD',
            to_airport_code='PRG',
            flight_duration='1:10',
            flight_number='testFR4092',
            airline='TestRyanair',
            price=Decimal('123456789012345678.12'),
            currency='CZK',
        ),
        types.Ticket(
            dep_datetime=DateTime(2024, 1, 8, 0, 0, 0, tzinfo=None),
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

    assert res == [
        Trip(
            start_date=DateTime(2024, 1, 5, 0, 0, 0),
            end_date=DateTime(2024, 1, 7, 0, 0, 0),
            currency='CZK',
            outbound_cost=Decimal('10'),
            outbound_airport='PRG',
            outbound_airline='TestWings',
            outbound_fly_number='test123',
            return_cost=Decimal('10'),
            return_airport='BCN',
            return_airline='TestWings',
            return_fly_number='test123'),
        Trip(
            start_date=DateTime(2024, 1, 6, 0, 0, 0),
            end_date=DateTime(2024, 1, 8, 0, 0, 0),
            currency='CZK',
            outbound_cost=Decimal('123456789012345678.12'),
            outbound_airport='PRG',
            outbound_airline='TestRyanair',
            outbound_fly_number='testFR4092',
            return_cost=Decimal('123456789012345678.12'),
            return_airport='BUD',
            return_airline='TestRyanair',
            return_fly_number='testFR4092'),
        Trip(
            start_date=DateTime(2024, 1, 6, 3, 15, 0),
            end_date=DateTime(2024, 1, 8, 0, 0, 0),
            currency='CZK',
            outbound_cost=Decimal('30'),
            outbound_airport='PRG',
            outbound_airline='TestRyanair',
            outbound_fly_number='testFR4092',
            return_cost=Decimal('123456789012345678.12'),
            return_airport='BUD',
            return_airline='TestRyanair',
            return_fly_number='testFR4092')
    ]
