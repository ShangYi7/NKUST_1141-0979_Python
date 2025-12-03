while True:
    L = int(input())
    if L <= 0:
        break

    t = input().split()     # t[0], t[1], t[2]
    size = 2 * L - 1

    for i in range(size):
        for j in range(size):
            top = i
            left = j
            bottom = size - 1 - i
            right = size - 1 - j

            layer = min(top, left, bottom, right)

            index = (L - 1 - layer) % 3
            token = t[index]

            print(token, end=" ")
        print()
