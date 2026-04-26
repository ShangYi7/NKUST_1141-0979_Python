while True:
    # 讀入邊長 L，若 L <= 0 代表輸入結束
    L = int(input())
    if L <= 0:
        break

    # 三個圖案字元，會依層數由外而內輪流使用
    t = input().split()     # t[0], t[1], t[2]
    size = 2 * L - 1

    for i in range(size):
        for j in range(size):
            # 依位置算出目前位於第幾層，離邊界越近層數越外側
            top = i
            left = j
            bottom = size - 1 - i
            right = size - 1 - j

            layer = min(top, left, bottom, right)

            # 以層數決定目前要印出的字元
            index = (L - 1 - layer) % 3
            token = t[index]

            print(token, end=" ")
        print()
