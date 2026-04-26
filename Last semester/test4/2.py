import time
while 1:
    # 每次輸入一個秒數 n，代表要觀察的時間長度
    n = int(input())
    startTime = time.time()
    x = 1
    if (n == 0):
        break
    while 1:
        endTime = time.time()
        if (endTime - startTime == x):
            # 到達第 x 秒時就輸出 x，並立即刷新畫面
            print(x, end="", flush=True)
            # flush=True 立即輸出, 不緩衝在記憶體
            x = x+1
        if (endTime - startTime == n):
            print("\n時間到！")
            break
