def combination(n, m):
    # 遞迴計算組合數 C(n, m)
    if (n == m or m == 0):
        return 1
    else:
        return combination(n-1, m)+combination(n-1, m-1)


while 1:
    # 讀入一組 n、m，當 n < m 時結束
    data = list(map(int, input().split()))
    if (data[0] < data[1]):
        break
    else:
        # 輸出組合數結果
        print(combination(data[0], data[1]))
