for i in range(0, 10):
    dara = input().split()
    # use fixed indices for each input line
    O = int(dara[0])
    d1 = int(dara[1])
    d2 = int(dara[2])

    if (O == 1):  # 小於100的共同因數
        found = False
        for j in range(1, 100):
            if (d1 % j == 0 and d2 % j == 0):
                print(j, end=" ")
                found = True
        if not found:
            print("None", end="")
        print()
    elif (O == 2):  # 小於100的共同倍數
        found = False
        for j in range(1, 100):
            if (j % d1 == 0 and j % d2 == 0):
                print(j, end=" ")
                found = True
        if not found:
            print("None", end="")
        print()
