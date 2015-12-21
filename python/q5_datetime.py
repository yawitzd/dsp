# Hint:  use Google to find python function
monthDict={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
monthDictInv={'Feb': 2, 'Jan': 1, 'Sep': 9, 'Oct': 10, 'Dec': 12, 'Jun': 6, 'Jul': 7, 'May': 5, 'Mar': 3, 'Nov': 11, 'Aug': 8, 'Apr': 4}
monthExtraDict={1:1, 2:-2, 3:1, 4:0, 5:1, 6:0, 7:1, 8:1, 9:0, 10:1, 11:0, 12:1}

def get_extradays(start, stop):
  extra = 0
  diff = abs(stop - start)
  for i in range(diff):
    key = start + i
    extra = extra + monthExtraDict[key]
  return extra

def get_timediff(y1, y2, m1, m2, d1, d2):
  year_diff = y2 - y1
  #leap_days = do something
  year_days = year_diff * 365 # + leap days
  

  month_diff = abs(m2 - m1)
  extra = get_extradays(m1, m2)
  month_days = month_diff * 30 + extra

  day_days = abs(day_stop - day_start)

  total = year_days + month_days + day_days
  return total

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

year_start = int(date_start[6:])
year_stop = int(date_stop[6:])

month_start = int(date_start[3:4])
month_stop = int(date_stop[3:4])

day_start = int(date_start[0:1])
day_stop = int(date_stop[0:1])

TIME_A = get_timediff(year_start, year_stop, month_start, month_stop, day_start, day_stop)
print("There are ", TIME_A, " days between", date_start, " and ", date_stop)

####b)
date_start = '12312013'
date_stop = '05282015'

year_start = int(date_start[4:])
year_stop = int(date_stop[4:])

month_start = int(date_start[2:3])
month_stop = int(date_stop[2:3])

day_start = int(date_start[0:1])
day_stop = int(date_stop[0:1])

TIME_B = get_timediff(year_start, year_stop, month_start, month_stop, day_start, day_stop)
print("There are ", TIME_B, " days between", date_start, " and ", date_stop)

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

year_start = int(date_start[7:])
year_stop = int(date_stop[7:])

month_start = int(monthDictInv[date_start[3:6]])
month_stop = int((monthDictInv[date_stop[3:6]]))

day_start = int(date_start[0:1])
day_stop = int(date_stop[0:1])

TIME_C = get_timediff(year_start, year_stop, month_start, month_stop, day_start, day_stop)
print("There are ", TIME_C, " days between", date_start, " and ", date_stop)
