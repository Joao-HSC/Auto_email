import pandas as pd
import yfinance as yf


def price_delta():
    print('Processing...')
    csv_file = 'VQFY_CONSTITUENTS.csv'
    message = 'Hey!\n\nHere\'s a list of today\'s winners/losers:\n\n'
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Extract tickers from the first column and convert to strings
    ticker_symbols = df.iloc[:, 0].astype(str).str.strip().tolist()

    # Print each ticker symbol and its latest change in percentage
    for ticker_symbol in ticker_symbols:
        stock_data = yf.Ticker(ticker_symbol)
        history = stock_data.history(period="5d")
        latest_close = history["Close"].iloc[-1] #last row
        previous_close = history["Close"].iloc[-2] #second to last row
        
        latest_change = (latest_close - previous_close) / previous_close * 100
        latest_change_rounded = round(latest_change, 2)

        if latest_change_rounded <= -7 or latest_change_rounded >= 7:
            message += '\t' + str(ticker_symbol) + " has changed by: " + str(latest_change_rounded) + '%\n'
   
    return message
