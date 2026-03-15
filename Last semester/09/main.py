# 輸出格式 1:The day of the week on "月份(英文字)" "日期(數字)", 年分(數字) is "星期幾(英文字)"
# 輸出格式 2:The date (n=正=after,n=負=before) (n的值) days is 月份(英文字) 日期(數字), 年分(數字)

# https://steam.oxxostudio.tw/category/python/library/calendar.html#a6
import calendar  # 日曆函數

# https://ithelp.ithome.com.tw/articles/10369051
# https://steam.oxxostudio.tw/category/python/library/datetime.html
import datetime  # 計算日期和時間之間的差異

while 1:
    data = input().split()
    day = data[0]
    n = int(data[1])
    year = int(day[0:4])
    month = int(day[5:7])
    day = int(day[8:10])
    if (
        calendar.isleap(year) == False and month == 2 and day == 29
    ):  # 判斷是否為閏年, 若不是閏年且日期為29，則跳出迴圈
        break
    # calendar.weekday 可以回傳某年某月的某一天是星期幾 ( 星期一從 0 開始 )。
    week = calendar.weekday(year, month, day)
    weeklist = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    monthlist = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    # f-string 格式化輸出
    print(
        f"The day of the week on {monthlist[month-1]} {day:02d}, {year} is {weeklist[week]}"
    )

    # datetime.date 用於表示日期 ( 年、月、日 )
    current_date = datetime.date(year, month, day)  # 建立日期物件
    # datetime.timedelta 用於表示兩個日期或時間之間的差異
    new_day = current_date + datetime.timedelta(days=n)  # 計算新的日期
    week = calendar.weekday(new_day.year, new_day.month, new_day.day)
    if n < 0:
        n = n + -n * 2
        print(
            f"The date before {n} days is {monthlist[new_day.month-1]} {new_day.day:02d}, {new_day.year}"
        )
    else:
        print(
            f"The date after {n} days is {monthlist[new_day.month-1]} {new_day.day:02d}, {new_day.year}"
        )
