import stock_change
import auto_email
import datetime
from pandas_market_calendars import get_calendar

def is_trading_day():
    
    current_date = datetime.date.today()
    market_calendar = get_calendar('NYSE') 
    
    return market_calendar.valid_days(start_date=current_date, end_date=current_date).size


if is_trading_day():
    message = stock_change.price_delta()
    if message != 'Hey!\n\nHere\'s a list of today\'s winners/losers:\n\n':
        auto_email.email(message)