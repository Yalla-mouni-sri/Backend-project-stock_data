import unittest
import pandas as pd
from trading_strategy import calculate_performance_metrics, apply_strategy, fetch_historical_data

class TestTradingStrategy(unittest.TestCase):

    def test_calculate_performance_metrics(self):
        """Test performance metrics calculation"""
        initial_value = 1000
        final_value = 1500
        returns = pd.Series([0.1, 0.2, -0.1, 0.05])
        metrics = calculate_performance_metrics(initial_value, final_value, returns)
        
        self.assertAlmostEqual(metrics["Total Returns"], 0.5)
        self.assertAlmostEqual(metrics["CAGR"], 0.5)
        self.assertTrue(metrics["Sharpe Ratio"] >= 0)  # Just checking it's non-negative
        self.assertTrue(metrics["Max Drawdown"] >= 0)  # Just checking it's non-negative

    def test_apply_strategy(self):
        """Test if apply_strategy correctly calculates moving averages"""
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
            {"Close": 200},
            {"Close": 201},
            {"Close": 202},
            {"Close": 203},
            {"Close": 204},
            {"Close": 205},
            {"Close": 206},
            {"Close": 207},
            {"Close": 208},
            {"Close": 209},
            {"Close": 210},
            {"Close": 211},
            {"Close": 212},
            {"Close": 213},
            {"Close": 214},
            {"Close": 215},
            {"Close": 216},
            {"Close": 217},
            {"Close": 218},
            {"Close": 219},
            {"Close": 220},
            {"Close": 221},
            {"Close": 222},
            {"Close": 223},
            {"Close": 224},
            {"Close": 225},
            {"Close": 226},
            {"Close": 227},
            {"Close": 228},
            {"Close": 229},
            {"Close": 230}
        ]

        df = pd.DataFrame(stock_data)
        df = apply_strategy(df)
        
        self.assertFalse(df['Short_MA'].isnull().any())  # Ensure no NaN values in Short_MA
        self.assertFalse(df['Long_MA'].isnull().any())   # Ensure no NaN values in Long_MA

if __name__ == "__main__":
    unittest.main()
