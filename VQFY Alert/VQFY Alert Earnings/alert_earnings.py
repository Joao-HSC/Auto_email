import stock_change
import auto_email
from pandas_market_calendars import get_calendar
from earnings_day import current_day

# Is the market open today? 
def is_trading_day(current_day):
    
    market_calendar = get_calendar('NYSE')
    return market_calendar.valid_days(start_date=current_day, end_date=current_day).size

# If so, execute the program
if is_trading_day(current_day):
    message = stock_change.price_delta()
    if message != 'Hey!\n\nHere\'s a list of today\'s winners/losers:\n\n':
        auto_email.email(message)
