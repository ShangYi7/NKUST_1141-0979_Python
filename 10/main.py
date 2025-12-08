while True:
    input = list(map(int, input().split()))
    n = input[0]
    if n == 0:
        break
    data = input[1:]
    data.sort()  # 升序排序

    if n % 2 == 1:  # 奇數
        median = data[(n + 1) // 2 - 1]
        output = median
    else:  # 偶數
        median = data[n // 2 - 1]
        output = median

