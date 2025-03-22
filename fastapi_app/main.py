from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine, Base
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine, Base
import models, schemas, crud
from trading_strategy import fetch_historical_data, apply_strategy, calculate_performance_metrics, visualize_strategy

import pandas as pd
import numpy as np
# Initialize database
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/", response_model=list[schemas.StockPriceResponse])
def fetch_all_data(db: Session = Depends(get_db)):
    records = crud.get_all_records(db)
    return records


@app.post("/data", response_model=schemas.StockPriceResponse)
def add_stock_price(stock_data: schemas.StockPriceCreate, db: Session = Depends(get_db)):
    if not stock_data:
        raise HTTPException(status_code=400, detail="Invalid input data")
    
    return crud.create_stock_price(db, stock_data)



data = {
    "date": pd.date_range(start="2024-01-01", periods=100, freq="D"),
    "price": np.random.uniform(100, 200, 100)  # Simulating stock prices
}
df = pd.DataFrame(data)

# Moving Average Crossover Strategy
def moving_average_strategy(df, short_window=10, long_window=50):
    """
    Calculate short-term and long-term moving averages.
    Generate buy/sell signals based on crossovers.
    """
    df["short_ma"] = df["price"].rolling(window=short_window).mean()
    df["long_ma"] = df["price"].rolling(window=long_window).mean()
    
    df["signal"] = 0
    df.loc[df["short_ma"] > df["long_ma"], "signal"] = 1  # Buy Signal
    df.loc[df["short_ma"] < df["long_ma"], "signal"] = -1 # Sell Signal
    
    return df

# Apply Strategy
df = moving_average_strategy(df)



@app.get("/strategy/performance")
def get_strategy_performance():
    """
    API endpoint that returns the trading strategy performance as JSON.
    """
    df["id"] = range(1, len(df) + 1)  # Assign unique IDs

    # Replacing NaN and infinite values with a default value (e.g., 0 or "N/A")
    df.replace([np.inf, -np.inf], np.nan, inplace=True)  # Convert inf to NaN
    df.fillna(0, inplace=True)  # Replace NaN with 0 (or choose another default)

    # Convert to JSON-friendly format
    performance_data = df[["id", "date", "price", "short_ma", "long_ma", "signal"]].to_dict(orient="records")

    return {"strategy": "Moving Average Crossover", "performance": performance_data}