data = input().strip().split()
n = int(data[0])
token1 = data[1]
token2 = data[2]

# n*n 代表整個圖形的面積，這裡用來判斷是否為 1x1 的特例
n8n = n*n

if (n8n == 1):
    print(token1)
else:
    # 上下邊全由 token1 組成
    print((token1+' ')*n)
    for _ in range(1, n-1):
        # 中間每列左、右邊是 token1，中間是 token2
        fuck = n-2
        print((token1+' ')+(token2+' ')*fuck+token1)
    # 底邊與頂邊相同
    print((token1+' ')*n)
