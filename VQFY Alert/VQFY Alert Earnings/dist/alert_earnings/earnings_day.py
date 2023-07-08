from datetime import datetime, timedelta

current_day = datetime.today().date()
yesterday = current_day - timedelta(days=1)
current_day_str = str(current_day)
yesterday_str = str(yesterday)

def earnings_date(ticker_symbol, stock_data):
 
    date_list = stock_data.get_earnings_dates(limit=10)
    date_list = date_list.index.strftime('%Y-%m-%d').to_list()  # Convert Timestamps to strings

    # Was any of the earning dates today or yesterday? If so, filtered_dates = [that date]
    filtered_dates = [date for date in date_list if date[:10] == current_day_str or date[:10] == yesterday_str]
   
    return len(filtered_dates)

