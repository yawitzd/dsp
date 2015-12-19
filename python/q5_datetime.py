# Hint:  use Google to find python function
monthDict={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
monthExtraDict={1:1, 2:-2, 3:1, 4:0, 5:1, 6:0, 7:1, 8:1, 9:0, 10:1, 11:0, 12:1} 

def get_extradays(start, stop):
  extra = 0
  diff = abs(stop - start)
  for i in range(diff):
    key = start + i
    extra = extra + monthExtraDict[key]
  return extra
  

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'  

year_start = int(date_start[6:])
year_stop = int(date_stop[6:])
year_dif = year_stop - year start
year_days = year_dif * 365

month_start = int(date_start[3:4])
month_stop = int(date_stop[3:4])
month_dif = month_stop - month_start

extra = get_extradays(month_start, month_stop)
month_days = month_days * 30 + extra

day_start = int(date_start[0:1])
day_stop = int(day_stop[0:1])
day_days = abs(day_stop - day_start)

total = year_days + month_days + day_days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
