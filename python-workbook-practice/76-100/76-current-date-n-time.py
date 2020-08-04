# Print current date and time
import time

#import datetime
#from datetime import *
#print(datetime.strftime(%A))
#print('Today is: ', datetime.date, 'and time is: ', datetime.time, 'and the timezone is :', datetime.timezone)
#print(dir(datetime))

print(time.time()) # O/P: Time in seconds since epoch time (Jan 1 - 1970)

# 1596511973.6690822

print(time.localtime())

# O/P: time.struct_time(tm_year=2020, tm_mon=8, tm_mday=3, tm_hour=23, tm_min=36, tm_sec=50, tm_wday=0, tm_yday=216, tm_i
#sdst=1)

print(type(time.localtime()))

# O/P: <class 'time.struct_time'>

print(time.ctime()) # O/P: Tue Aug  4 01:21:09 2020

print('Today is: ', time.ctime())

# O/P: Today is:  Tue Aug  4 01:21:45 2020










