from datetime import datetime, timedelta

class Stock:
    """
    Represents a stock in the Global Beverage Corporation Exchange (GBCE).
    Supports common and preferred stock types and allows trading operations.
    """

    def __init__(self, symbol, stock_type, last_dividend, fixed_dividend, par_value):
        """
        Initialize a stock with given parameters.
        :param symbol: Stock symbol
        :param stock_type: Type of stock ('Common' or 'Preferred')
        :param last_dividend: Last dividend value
        :param fixed_dividend: Fixed dividend percentage (for preferred stock)
        :param par_value: Par value of the stock
        """
        self.symbol = symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.trades = []  # Stores trades as a list of tuples (timestamp, quantity, buy/sell, price)

    def calculate_dividend_yield(self, price):
        """
        Calculate the dividend yield based on stock type.
        :param price: Market price of the stock
        :return: Dividend yield value
        """
        if price <= 0:
            raise ValueError("Price must be greater than zero")

        if self.stock_type == "Common":
            return self.last_dividend / price
        elif self.stock_type == "Preferred":
            return (self.fixed_dividend * self.par_value) / price

    def calculate_pe_ratio(self, price):
        """
        Calculate the Price-to-Earnings (P/E) ratio.
        :param price: Market price of the stock
        :return: P/E ratio value
        """
        dividend = self.last_dividend if self.stock_type == "Common" else (self.fixed_dividend * self.par_value)
        if dividend == 0:
            return float('inf')  # P/E ratio is undefined when dividend is 0
        return price / dividend

    def record_trade(self, quantity, indicator, price):
        """
        Record a trade for the stock.
        :param quantity: Number of shares traded
        :param indicator: 'buy' or 'sell'
        :param price: Trade price per share
        """
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be greater than zero")
        if indicator not in ("buy", "sell"):
            raise ValueError("Indicator must be 'buy' or 'sell'")

        trade = (datetime.now(), quantity, indicator, price)
        self.trades.append(trade)

    def volume_weighted_stock_price(self):
        """
        Calculate the Volume Weighted Stock Price based on trades in the past 5 minutes.
        :return: Volume Weighted Stock Price
        """
        cutoff_time = datetime.now() - timedelta(minutes=5)
        recent_trades = [(q, p) for t, q, _, p in self.trades if t >= cutoff_time]

        total_trade_price_quantity = sum(q * p for q, p in recent_trades)
        total_quantity = sum(q for q, _ in recent_trades)

        return total_trade_price_quantity / total_quantity if total_quantity > 0 else 0

