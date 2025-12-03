while True:
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
        if (i % d1 == 0 and i % d2 == 0 and i % d3 == 0):
            print(i, end=" ")
            count += 1
        i += 1
    print()
