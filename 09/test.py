from datetime import datetime, timedelta

# 獲取當前日期和時間
now = datetime.now()
print("現在時間:", now)

# 計算未來的日期（例如，加上 10 天）
future_date = now + timedelta(days=10)
print("10 天後的日期:", future_date)

# 計算過去的日期（例如，減去 5 天）
past_date = now - timedelta(days=5)
print("5 天前的日期:", past_date)