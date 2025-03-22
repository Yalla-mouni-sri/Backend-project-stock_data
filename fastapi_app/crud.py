from sqlalchemy.orm import Session
import models, schemas

def create_stock_price(db: Session, stock_data: schemas.StockPriceCreate):
    """
    Inserts a new stock price record into the database.
    """
    db_stock = models.StockPrice(
        datetime=stock_data.datetime,
        open=stock_data.open,
        high=stock_data.high,
        low=stock_data.low,
        close=stock_data.close,
        volume=stock_data.volume,
        instrument=stock_data.instrument
    )
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock


def get_all_records(db: Session):
    """
    Fetch all stock price records from the database.
    """
    return db.query(models.StockPrice).all()
