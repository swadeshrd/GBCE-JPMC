from math import prod


class GBCE:
    """
    Represents the Global Beverage Corporation Exchange (GBCE).
    Manages stocks and calculates the All Share Index.
    """

    def __init__(self):
        """
        Initializes the GBCE with an empty dictionary to store stocks.
        """
        self.stocks = {}

    def add_stock(self, stock):
        """
        Adds a stock to the exchange.

        :param stock: Stock object to be added
        """
        self.stocks[stock.symbol] = stock

    def calculate_all_share_index(self):
        """
        Calculates the GBCE All Share Index using the geometric mean of Volume Weighted Stock Prices.

        :return: The GBCE All Share Index value
        """
        vwsp_list = [stock.volume_weighted_stock_price() for stock in self.stocks.values() if
                     stock.volume_weighted_stock_price() > 0]

        if not vwsp_list:
            return 0  # Return 0 if there are no valid stock prices to calculate the index

        return prod(vwsp_list) ** (1 / len(vwsp_list))
