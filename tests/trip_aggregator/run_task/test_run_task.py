from unittest.mock import Mock

from trip_aggregator.run_task import main


async def test_main_happy_path(mocker):
    trips = [
        Mock(),
        Mock(),
    ]
    mocker.patch('trip_aggregator.run_task.create_trips', return_value=trips)
    spy = mocker.patch('trip_aggregator.run_task.replace_trips', return_value=2)

    response = main()

    assert response.is_success is True
    assert response.trips_found > 0
    assert spy.call_count == 1


async def test_main_no_tickets(mocker):
    trips = []
    mocker.patch('trip_aggregator.run_task.replace_trips', return_value=trips)

    response = main()

    assert response.is_success is True
    assert response.trips_found == 0
