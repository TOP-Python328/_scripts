from datetime import datetime as dt, date, time, timedelta as td


two_days_ago = dt(2023, 9, 5, 3, 42)
now = dt.now()

# >>> two_days_ago
# datetime.datetime(2023, 9, 5, 3, 42)
# >>>
# >>> print(two_days_ago)
# 2023-09-05 03:42:00
# >>>
# >>> two_days_ago.strftime('%d.%m.%y %H:%M:%S')
# '05.09.23 03:42:00'
# >>>
# >>> two_days_ago.strftime('%d.%m.%y %H:%M')
# '05.09.23 03:42'
# >>>
# >>> f'{two_days_ago:%d.%m - %H:%M}'
# '05.09 - 03:42'


# >>> td1 = now - two_days_ago
# >>> td1
# datetime.timedelta(days=1, seconds=64243, microseconds=952610)
# >>>
# >>> print(td1)
# 1 day, 17:50:43.952610
# >>>
# >>> td1.days
# 1
# >>> td1.seconds
# 64243
# >>>
# >>> td1.hours
# ...
# AttributeError: 'datetime.timedelta' object has no attribute 'hours'


# >>> long_ago = dt.strptime('4:27 01.05.1963', '%H:%M %d.%m.%Y')
# >>> long_ago
# datetime.datetime(1963, 5, 1, 4, 27)
# >>>
# >>> long_ago.date()
# datetime.date(1963, 5, 1)
# >>>
# >>> long_ago.time()
# datetime.time(4, 27)

