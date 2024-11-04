import datetime as dt

yr = int(input())
mn = int(input())
day = int(input())

date = dt.datetime(yr,mn,day)
print(date)
print(date.strftime("%B"))
print(date.strftime("%b"))
print(date.strftime("%m"))
print(date.strftime("%Y"))
print(date.strftime("%y"))
print(date.strftime("%d"))
print(date.strftime("%A"))
print(date.strftime("%a"))
