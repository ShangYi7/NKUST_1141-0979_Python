def combination(n,m):
    if(n==m or m ==0):
        return 1
    else:
        return combination(n-1,m)+combination(n-1,m-1)

while 1:
    data = list(map(int, input().split()))
    if(data[0]<data[1]):
        break
    else:
        print(combination(data[0],data[1]))
