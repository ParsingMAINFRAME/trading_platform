# import yfinance as yf
# import pandas as pd

# # Function to download stock data and save to CSV
# def download_stock_data(ticker, start_date, end_date):
#     stock = yf.download(ticker, start=start_date, end=end_date)
#     csv_filename = f"{ticker}_data_{start_date}_to_{end_date}.csv"
#     stock.to_csv(csv_filename)
#     return stock

# # Get inputs from the user
# if __name__ == "__main__":
#     ticker = input("Enter stock ticker symbol (e.g., AAPL): ")
#     start_date = input("Enter start date (YYYY-MM-DD): ")
#     end_date = input("Enter end date (YYYY-MM-DD): ")
#     data = download_stock_data(ticker, start_date, end_date)
#     print(f"Data saved to {ticker}_data_{start_date}_to_{end_date}.csv")

#Explanation
#•	The code now includes functionality to calculate moving averages and store them in the CSV file.
#•	You can dynamically input the short-term and long-term moving average
# windows when prompted.
    #
# import yfinance as yf
# import pandas as pd

# # Function to download stock data, calculate moving averages, and save to CSV
# def download_stock_data(ticker, start_date, end_date, short_window=40, long_window=100):
#     # Download the stock data
#     stock = yf.download(ticker, start=start_date, end=end_date)

#     # Calculate moving averages
#     stock['Short_MA'] = stock['Close'].rolling(window=short_window).mean()
#     stock['Long_MA'] = stock['Close'].rolling(window=long_window).mean()

#     # Save the data to CSV
#     csv_filename = f"{ticker}_data_{start_date}_to_{end_date}.csv"
#     stock.to_csv(csv_filename)

#     return stock

# # Get inputs from the user
# if __name__ == "__main__":
#     ticker = input("Enter stock ticker symbol (e.g., AAPL): ")
#     start_date = input("Enter start date (YYYY-MM-DD): ")
#     end_date = input("Enter end date (YYYY-MM-DD): ")
#     short_window = int(input("Enter short moving average window (e.g., 40): "))
#     long_window = int(input("Enter long moving average window (e.g., 100): "))

#     # Call the function
#     data = download_stock_data(ticker, start_date, end_date, short_window, long_window)
#     print(f"Data saved to {ticker}_data_{start_date}_to_{end_date}.csv")
#     print(data.tail())  # Display the last few rows of data
#Explanation
# 1.	os.makedirs(output_dir):
# This command checks if the output folder exists. If not, it creates the folder to store the CSV files.
# 	2.	csv_filename = os.path.join(output_dir, ...):
# The os.path.join function ensures that the file path is constructed correctly, regardless of the operating system (Windows, macOS, Linux).
import os
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Function to download stock data, calculate moving averages, and save to CSV
def download_stock_data(ticker, start_date, end_date, short_window=40, long_window=100):
    # Download the stock data
    stock = yf.download(ticker, start=start_date, end=end_date)

    # Calculate moving averages
    stock['Short_MA'] = stock['Close'].rolling(window=short_window).mean()
    stock['Long_MA'] = stock['Close'].rolling(window=long_window).mean()

    # Define the output directory path (since it exists now)
    output_dir = 'output'

    # Save the data to CSV in the manually created output folder
    csv_filename = os.path.join(output_dir, f"{ticker}_data_{start_date}_to_{end_date}.csv")
    stock.to_csv(csv_filename)

    # Optionally, plot the data (if you have plotting enabled)
    plt.figure(figsize=(12,6))
    plt.plot(stock['Close'], label='Close Price')
    plt.plot(stock['Short_MA'], label=f'{short_window}-Day Moving Average')
    plt.plot(stock['Long_MA'], label=f'{long_window}-Day Moving Average')
    plt.title(f'{ticker} Close Price and Moving Averages')
    plt.legend()
    plt.show()

    return stock

# Get inputs from the user
if __name__ == "__main__":
    ticker = input("Enter stock ticker symbol (e.g., AAPL): ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    short_window = int(input("Enter short moving average window (e.g., 40): "))
    long_window = int(input("Enter long moving average window (e.g., 100): "))

    # Call the function
    data = download_stock_data(ticker, start_date, end_date, short_window, long_window)
    print(f"Data saved to output/{ticker}_data_{start_date}_to_{end_date}.csv")
    print(data.tail())  # Display the last few rows of data