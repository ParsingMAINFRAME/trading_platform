import yfinance as yf
import pandas as pd

# Function to download stock data and save to CSV
def download_stock_data(ticker, start_date, end_date):
    stock = yf.download(ticker, start=start_date, end=end_date)
    csv_filename = f"{ticker}_data_{start_date}_to_{end_date}.csv"
    stock.to_csv(csv_filename)
    return stock

# Get inputs from the user
if __name__ == "__main__":
    ticker = input("Enter stock ticker symbol (e.g., AAPL): ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    data = download_stock_data(ticker, start_date, end_date)
    print(f"Data saved to {ticker}_data_{start_date}_to_{end_date}.csv")