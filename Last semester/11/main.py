while 1:
    data = list(map(int, input().split()))
    n = data[0]
    b = data[1] # 進位制
    d=0
    if n<0 or b<2 or b>10:
        break

    x = 0
    i = 1
    while (n != 0):
        a = n % b
        x = x + a * i
        i *= 10
        n //= b

    print(x)
