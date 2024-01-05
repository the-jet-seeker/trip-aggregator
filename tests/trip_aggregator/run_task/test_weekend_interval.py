import pendulum
from pendulum import DateTime, Timezone

from trip_aggregator.run_task import _weekend_interval
from trip_aggregator.settings import app_settings


def test_weekend_interval(mocker):
    mocker.patch(
        'pendulum.now',
        return_value=DateTime(2023, 11, 1, 12, 2, 28, 765187, tzinfo=Timezone(app_settings.HOME_TIMEZONE)),
    )

    res = _weekend_interval()

    assert res == pendulum.Interval(
        DateTime(2023, 11, 10, 0, 0, 0, tzinfo=None),
        DateTime(2023, 11, 13, 23, 59, 59, tzinfo=None),
    )
