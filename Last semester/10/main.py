while True:
    # 第一個數字是資料筆數，後面是對應資料
    nums = list(map(int, input().split()))
    n = nums[0]
    if n == 0:
        break
    data = nums[1:]
    data.sort()  # 升序排序

    # 中位數：依資料筆數奇偶決定取哪個位置
    if n % 2 == 1:  # 奇數
        median = data[(n + 1) // 2 - 1]
        output = median
    else:  # 偶數
        median = data[n // 2 - 1]
        output = median
    print(output, end=" ")
    # 變異數：先算平均，再累加平方差
    ans = 0
    mean = sum(data) // n  # 平均值 # sum == 全部加起來
    for x in data:
        ans += (x - mean) * (x - mean)
    ans //= n
    print(f"{ans:0.0f}")
