import time
while 1:
    n = int(input())
    startTime = time.time()
    x = 1
    if (n == 0):
        break
    while 1:
        endTime = time.time()
        if (endTime - startTime == x):
            print(x, end="", flush=True)
            # flush=True 立即輸出, 不緩衝在記憶體
            x = x+1
        if (endTime - startTime == n):
            print("\n時間到！")
            break
