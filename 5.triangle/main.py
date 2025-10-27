try:
    n = int(input().strip())
except Exception:
    # 若沒輸入或格式錯誤，直接結束
    exit(0)

for _ in range(n):
    parts = input().strip().split()
    if len(parts) < 3:
        # 若格式不正確，跳過（簡單處理）
        continue
    L = int(parts[0])
    t1 = parts[1]
    t2 = parts[2]
    for i in range(1, L + 1):
        print(t1 * i + t2 * (L - i))
