# https://steam.oxxostudio.tw/category/python/library/calendar.html#a6
import calendar # 日曆函數

while 1:
    data=input().split()
    day=data[0]
    n=int(data[1])
    year=int(day[0:4])
    month=int(day[5:7])
    date=int(day[8:10])
    # calendar.weekday 可以回傳某年某月的某一天是星期幾 ( 星期一從 0 開始 )。
    week=calendar.weekday(year,month,date)
    print(week) # 星期幾
    # if()
