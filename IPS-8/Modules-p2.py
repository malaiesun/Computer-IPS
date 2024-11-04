import datetime as dt

yr = int(input())
mn = int(input())
day = int(input())

date = dt.datetime(yr,mn,day)
print(date)
print(date.strftime("%B"))
print(date.strftime("%A"))
