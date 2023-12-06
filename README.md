# The Jet Seeker [aggregator]

[![tests](https://github.com/the-jet-seeker/trip-aggregator/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/the-jet-seeker/trip-aggregator/actions/workflows/tests.yml)
[![linters](https://github.com/the-jet-seeker/trip-aggregator/actions/workflows/linters.yml/badge.svg?branch=master)](https://github.com/the-jet-seeker/trip-aggregator/actions/workflows/linters.yml)


### Pre-requirements
- [Python 3.12+](https://www.python.org/downloads/)
- [PostgreSQL server](https://www.postgresql.org/download/)


### Local setup
```shell
$ git clone git@github.com:the-jet-seeker/trip-aggregator.git
$ cd trip-aggregator
$ python3.12 -m venv venv
$ source venv/bin/activate
$ pip install -U poetry pip setuptools
$ poetry config virtualenvs.create false --local
$ poetry install
```


### Host setup
```shell
$ add-apt-repository ppa:deadsnakes/ppa
$ apt-get update
$ apt install -y software-properties-common python3.12 python3.12-dev python3.12-venv python3-psycopg2 libpq-dev gcc postgresql-client-14
$ apt-get upgrade

$ curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
$ curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12

$ python3.10 -m pip install --upgrade setuptools
$ python3.12 -m pip install --upgrade setuptools

$ adduser tjs-stage-aggregator
$ adduser tjs-production-aggregator
```


### Local run tests
```shell
$ pytest --cov=trip_aggregator
```


### Local run linters
```shell
$ poetry run flake8 trip_aggregator/
$ poetry run mypy trip_aggregator/
```

### Run scrapper
```shell
$ python -m trip_aggregator.run_task
```


### Setting up periodically jobs
```shell
$ crontab etc/crontab.txt
```