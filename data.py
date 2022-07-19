from datetime import datetime
from pytz import timezone, all_timezones

timeformat = '%d-%m-%Y, %H:%M:%S'

now = datetime.now().strftime(timeformat)

timeInArabia = datetime.now(timezone(zone='Asia/Riyadh')).strftime(timeformat)

print(timeInArabia)


print(now)