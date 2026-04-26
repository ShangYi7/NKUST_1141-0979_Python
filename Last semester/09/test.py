from datetime import datetime, timedelta

# 取出現在時間，作為日期運算的基準
now = datetime.now()
print("現在時間:", now)

# 計算 10 天後的時間
future_date = now + timedelta(days=10)
print("10 天後的日期:", future_date)

# 計算 5 天前的時間
past_date = now - timedelta(days=5)
print("5 天前的日期:", past_date)
