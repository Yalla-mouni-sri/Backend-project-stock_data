from sqlalchemy import Column, Integer, Float, DateTime, String

from database import Base
import datetime


class StockPrice(Base):
    __tablename__ = "stock_prices"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    datetime = Column(DateTime, nullable=False)
    close = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    open = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)
    instrument = Column(String, nullable=False)
