import unittest
from datetime import datetime, timedelta
from gbce.stock import Stock
from gbce.exchange import GBCE


class TestStock(unittest.TestCase):
    def setUp(self):
        """Initialize stock instances for testing."""
        self.stock_common = Stock("POP", "Common", 8, 0, 100)
        self.stock_preferred = Stock("GIN", "Preferred", 8, 0.02, 100)

    def test_dividend_yield_common(self):
        """Test dividend yield calculation for common stock."""
        self.assertEqual(self.stock_common.calculate_dividend_yield(100), 0.08)

    def test_dividend_yield_preferred(self):
        """Test dividend yield calculation for preferred stock."""
        self.assertEqual(self.stock_preferred.calculate_dividend_yield(100), 0.02)

    def test_pe_ratio(self):
        """Test P/E ratio calculation."""
        self.assertEqual(self.stock_common.calculate_pe_ratio(100), 12.5)

    def test_record_trade(self):
        """Test recording of trades."""
        self.stock_common.record_trade(10, "buy", 120)
        self.assertEqual(len(self.stock_common.trades), 1)

    def test_volume_weighted_stock_price(self):
        """Test volume weighted stock price calculation."""
        self.stock_common.record_trade(10, "buy", 120)
        self.stock_common.record_trade(5, "sell", 125)
        self.assertAlmostEqual(self.stock_common.volume_weighted_stock_price(), 121.67, places=2)


class TestGBCE(unittest.TestCase):
    def setUp(self):
        """Initialize GBCE exchange and add stocks."""
        self.exchange = GBCE()
        self.stock1 = Stock("TEA", "Common", 0, 0, 100)
        self.stock2 = Stock("POP", "Common", 8, 0, 100)
        self.exchange.add_stock(self.stock1)
        self.exchange.add_stock(self.stock2)

    def test_all_share_index(self):
        """Test GBCE All Share Index calculation."""
        self.stock1.record_trade(10, "buy", 120)
        self.stock2.record_trade(20, "buy", 110)
        self.assertGreater(self.exchange.calculate_all_share_index(), 0)


if __name__ == "__main__":
    unittest.main()
