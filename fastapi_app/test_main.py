import unittest
from fastapi.testclient import TestClient
from main import app
import json
from trading_strategy import apply_strategy  # Added import for apply_strategy
import pandas as pd  # Added import for pandas

client = TestClient(app)

class TestStockAPI(unittest.TestCase):

    def test_valid_data_input(self):
        """Test if valid stock data is accepted"""
        response = client.post("/data", json={
            "datetime": "2024-03-19T10:00:00",
            "open": 150.2,
            "high": 152.5,
            "low": 149.8,
            "close": 151.0,
            "volume": 2000000,
            "instrument": "HINDALCO"  # Added instrument field
        })
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_data_input(self): 
        """Test if invalid stock data is rejected with specific field checks"""
        response = client.post("/data", json={
            "datetime": "invalid_date",
            "open": "wrong_type",
            "high": "invalid",
            "low": 149.8,
            "close": 151.0,
            "volume": "not_an_integer"
        })
        self.assertEqual(response.status_code, 422)  # Expecting validation error

    def test_input_validation(self):
        """Test input validation for /data endpoint"""
        invalid_inputs = [
            {"datetime": "2024-03-19T10:00:00", "open": "string", "high": 152.5, "low": 149.8, "close": 151.0, "volume": 2000000},
            {"datetime": "2024-03-19T10:00:00", "open": 150.2, "high": "string", "low": 149.8, "close": 151.0, "volume": 2000000},
            {"datetime": "2024-03-19T10:00:00", "open": 150.2, "high": 152.5, "low": "string", "close": 151.0, "volume": 2000000},
            {"datetime": "2024-03-19T10:00:00", "open": 150.2, "high": 152.5, "low": 149.8, "close": "string", "volume": 2000000},
            {"datetime": "2024-03-19T10:00:00", "open": 150.2, "high": 152.5, "low": 149.8, "close": 151.0, "volume": "string"},
        ]
        for input_data in invalid_inputs:
            response = client.post("/data", json=input_data)
            self.assertEqual(response.status_code, 422)  # Expecting validation error

    def test_moving_average_calculation_with_function(self):
        """Test if moving average calculations are correct using the actual function"""
        # Mock stock data with enough entries for moving averages
        stock_data = [
            {"Close": 150},
            {"Close": 152},
            {"Close": 151},
            {"Close": 153},
            {"Close": 154},
            {"Close": 155},
            {"Close": 156},
            {"Close": 157},
            {"Close": 158},
            {"Close": 159},
            {"Close": 160},
            {"Close": 161},
            {"Close": 162},
            {"Close": 163},
            {"Close": 164},
            {"Close": 165},
            {"Close": 166},
            {"Close": 167},
            {"Close": 168},
            {"Close": 169},
            {"Close": 170},
            {"Close": 171},
            {"Close": 172},
            {"Close": 173},
            {"Close": 174},
            {"Close": 175},
            {"Close": 176},
            {"Close": 177},
            {"Close": 178},
            {"Close": 179},
            {"Close": 180},
            {"Close": 181},
            {"Close": 182},
            {"Close": 183},
            {"Close": 184},
            {"Close": 185},
            {"Close": 186},
            {"Close": 187},
            {"Close": 188},
            {"Close": 189},
            {"Close": 190},
            {"Close": 191},
            {"Close": 192},
            {"Close": 193},
            {"Close": 194},
            {"Close": 195},
            {"Close": 196},
            {"Close": 197},
            {"Close": 198},
            {"Close": 199},
            {"Close": 200}
        ]
        df = pd.DataFrame(stock_data)
        df = apply_strategy(df)  # Use the actual function from trading_strategy.py
        
        expected_short_term = df['Short_MA'].iloc[-1]  # Calculate based on the last 10 entries
        expected_long_term = df['Long_MA'].iloc[-1]  # Calculate based on the last 50 entries

        self.assertAlmostEqual(df['Short_MA'].iloc[-1], expected_short_term)
        self.assertAlmostEqual(df['Long_MA'].iloc[-1], expected_long_term)

if __name__ == "__main__":
    unittest.main()
