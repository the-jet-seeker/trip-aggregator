import pendulum
import pytest
from pendulum import DateTime, Timezone

from trip_aggregator.run_task import _weekend_interval
from trip_aggregator.settings import app_settings


@pytest.mark.parametrize('current_day, expected_start_day', [
    (8, 19),
    (9, 19),
    (10, 19),
    (11, 19),
    (12, 19),
    (13, 19),
    (14, 19),
    (15, 26),
])
def test_weekend_interval(mocker, current_day: int, expected_start_day: int):
    mocker.patch(
        'pendulum.now',
        return_value=DateTime(2024, 1, current_day, 12, 2, 28, 765187, tzinfo=Timezone(app_settings.HOME_TIMEZONE)),
    )

    res = _weekend_interval()

    assert isinstance(res, pendulum.Interval)
    assert res.start < res.end
    assert res.start.day == expected_start_day
    assert res.end.day == expected_start_day + 3
    assert res.start.time() == pendulum.Time(0, 0, 0)
    assert res.end.time() == pendulum.Time(23, 59, 59)
