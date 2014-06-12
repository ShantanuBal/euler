import datetime
count = 0
d1 = datetime.datetime(1901, 1, 1)
while d1.year != 2001:
   if d1.weekday() == 6 and d1.day == 1:
       count += 1
   d1 += datetime.timedelta(days=1)
   print d1
print count
