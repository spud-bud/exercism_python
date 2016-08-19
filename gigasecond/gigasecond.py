from datetime import datetime, timedelta
def add_gigasecond(date_time):
    gigasecond = timedelta(seconds = 10**9)
    result = date_time + gigasecond
    return result
