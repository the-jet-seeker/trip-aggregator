from trip_aggregator.cost_of_leaving import get_cost_of_leaving, CoastOfLeaving


def test_get_cost_of_leaving():
    res = get_cost_of_leaving('PRG')

    assert res == CoastOfLeaving(
        night=2438,
        meal=200,
    )
