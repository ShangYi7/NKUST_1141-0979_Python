import time
from random import randint
sun = []
n = 1
while n != 4:
    # 共有 3 次測試，分別記錄每次等待使用者反應的時間
    print("第 ", n, " 次：")
    n = n+1
    # 隨機決定這次要等待幾秒後才顯示「時間到」
    ans = (randint(1, 3))
    # print(ans)
    startTime = time.time()
    endTime = time.time()
    while 1:
        x_time = endTime - startTime
        if (x_time >= ans):
            break
        else:
            endTime = time.time()
    print("時間到！", end="")
    # 計算使用者按下 Enter 的反應時間
    startTime = time.time()
    input('')
    endTime = time.time()
    sun.append(endTime - startTime)
    if (n != 3):
        # 兩次測試之間固定等待 3 秒，讓流程更一致
        startTime = time.time()
        endTime = time.time()
        while 1:
            x_time = endTime - startTime
            if (x_time >= 3):
                break
            else:
                endTime = time.time()

# 將三次反應時間格式化輸出
print(f"結果統計： {sun[0]:.3f} {sun[1]:.3f} {sun[2]:.3f}")
