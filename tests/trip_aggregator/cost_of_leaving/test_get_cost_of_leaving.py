from trip_aggregator.cost_of_leaving import get_cost_of_leaving, CoastOfLeaving


def test_get_cost_of_leaving_happy_path():
    res = get_cost_of_leaving('PRG')

    assert res == CoastOfLeaving(
        night=2438,
        meal=200,
    )


def test_get_cost_of_leaving_no_data():
    res = get_cost_of_leaving('ABC')

    assert res is None
