from trip_aggregator.run_task import main


async def test_main_happy_path():
    response = main()

    assert response.is_success is True
    assert response.trips_found > 0
