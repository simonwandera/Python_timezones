from datetime import datetime
from pytz import timezone, all_timezones

def currentTime():
    timeformat = '%d-%m-%Y, %H:%M:%S'

    now = datetime.now().strftime(timeformat)

    current_time = datetime.now(timezone(zone='Asia/Riyadh')).strftime(timeformat)
    return