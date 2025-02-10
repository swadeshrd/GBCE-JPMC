from gbce.stock import Stock
from gbce.exchange import GBCE

def main():
    """
    Entry point for the GBCE Trading System.
    Demonstrates stock trading operations, calculations, and the All Share Index computation.
    """
    # Initialize the GBCE exchange
    gbce = GBCE()

    # Create and add sample stocks
    stocks = [
        Stock("TEA", "Common", 0, 0, 100),
        Stock("POP", "Common", 8, 0, 100),
        Stock("ALE", "Common", 23, 0, 60),
        Stock("GIN", "Preferred", 8, 0.02, 100),
        Stock("JOE", "Common", 13, 0, 250)
    ]

    for stock in stocks:
        gbce.add_stock(stock)

    # Record sample trades
    stocks[0].record_trade(10, "buy", 120)
    stocks[0].record_trade(5, "sell", 125)
    stocks[1].record_trade(20, "buy", 110)
    stocks[2].record_trade(15, "sell", 95)
    stocks[3].record_trade(25, "buy", 105)
    stocks[4].record_trade(30, "sell", 200)

    # Print stock calculations
    for stock in stocks:
        print(f"\nStock: {stock.symbol}")
        print(f"  Dividend Yield: {stock.calculate_dividend_yield(120):.2f}")
        print(f"  P/E Ratio: {stock.calculate_pe_ratio(120):.2f}")
        print(f"  Volume Weighted Stock Price: {stock.volume_weighted_stock_price():.2f}")

    # Calculate and display GBCE All Share Index
    print(f"\nGBCE All Share Index: {gbce.calculate_all_share_index():.2f}")

if __name__ == "__main__":
    main()
