while True:
    nums = list(map(int, input().split()))
    n = nums[0]
    if n == 0:
        break
    data = nums[1:]
    data.sort()  # 升序排序

    #中位數
    if n % 2 == 1:  # 奇數
        median = data[(n + 1) // 2 - 1]
        output = median
    else:  # 偶數
        median = data[n // 2 - 1]
        output = median
    print(output,end=" ")
    #變異數
    ans = 0
    mean = sum(data) // n #平均值 # sum == 全部加起來
    for x in data:
        ans += (x - mean) * (x - mean)
    ans//=n
    print(f"{ans:0.0f}")
