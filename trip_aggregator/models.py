"""Database models."""
from datetime import datetime
from decimal import Decimal

import sqlalchemy as sa
from sqlalchemy import NUMERIC
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from trip_aggregator.settings import app_settings


class Base(DeclarativeBase):
    """Base class for every database model."""

    @classmethod
    def select(cls) -> sa.Select:
        """Select query shortcut."""
        return sa.select(cls)

    @classmethod
    def delete(cls) -> sa.Delete:
        """Delete query shortcut."""
        return sa.delete(cls)


class Ticket(Base):
    """Ticket database table model."""

    __tablename__ = 'ticket'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    dep_datetime: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=False), index=True)
    arr_datetime: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=False), index=True)
    from_airport_code: Mapped[str] = mapped_column(sa.String(length=3))
    to_airport_code: Mapped[str] = mapped_column(sa.String(length=3))
    flight_duration: Mapped[str] = mapped_column(sa.String)
    flight_number: Mapped[str] = mapped_column(sa.String)
    airline: Mapped[str] = mapped_column(sa.String)
    price: Mapped[Decimal] = mapped_column(NUMERIC(precision=20, scale=2))
    currency: Mapped[str] = mapped_column(sa.String(length=3))
    source: Mapped[str] = mapped_column(sa.String, index=True)


class Trip(Base):
    """Trip database table model."""

    __tablename__ = 'trip'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    start_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=False), index=True)
    end_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=False), index=True)
    currency: Mapped[str] = mapped_column(sa.String(length=3))

    outbound_cost: Mapped[Decimal] = mapped_column(NUMERIC(precision=20, scale=2))
    outbound_airport: Mapped[str] = mapped_column(sa.String(length=3), index=True)
    outbound_airline: Mapped[str] = mapped_column(sa.String)
    outbound_fly_number: Mapped[str] = mapped_column(sa.String(length=16))

    return_cost: Mapped[Decimal] = mapped_column(NUMERIC(precision=20, scale=2))
    return_airport: Mapped[str] = mapped_column(sa.String(length=3))
    return_airline: Mapped[str] = mapped_column(sa.String)
    return_fly_number: Mapped[str] = mapped_column(sa.String(length=16))


engine = sa.create_engine(
    url='postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(
        app_settings.DATABASE_USER,
        app_settings.DATABASE_PASSWORD,
        app_settings.DATABASE_HOST,
        app_settings.DATABASE_PORT,
        app_settings.DATABASE_NAME,
    ),
    echo=app_settings.DEBUG,
)

Session = sessionmaker(engine)
