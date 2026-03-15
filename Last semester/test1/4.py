data = input().strip().split()
n=int(data[0])
token1=data[1]
token2=data[2]

n8n=n*n

if(n8n==1):
    print(token1)
else:
    print((token1+' ')*n)
    for _ in range(1, n-1):
        fuck=n-2
        print((token1+' ')+(token2+' ')*fuck+token1)
    print((token1+' ')*n)
