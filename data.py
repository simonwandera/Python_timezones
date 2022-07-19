from datetime import datetime
from pytz import timezone, all_timezones

timeformat = '%d-%m-%Y, %H:%M:%S'

now = datetime.now().strftime(timeformat)


print(now)