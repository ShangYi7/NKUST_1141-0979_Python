while True:
    # 輸入 k 與三個整數，k=要找的共同倍數個數
    data = input().split()
    k = int(data[0])
    if k == 0:
        break

    d1 = int(data[1])
    d2 = int(data[2])
    d3 = int(data[3])

    count = 0
    i = 1

    while count < k:
        # 逐一檢查自然數，找出同時可被三個數整除的數
        if (i % d1 == 0 and i % d2 == 0 and i % d3 == 0):
            print(i, end=" ")
            count += 1
        i += 1
    print()
