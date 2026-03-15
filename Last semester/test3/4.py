import time 
from random import randint 
sun=[]
n=1
while n!=4:
    print("第 ",n ," 次：")
    n=n+1
    ans=(randint(1,3))
    # print(ans)
    startTime=time.time()
    endTime=time.time()
    while 1:
        x_time=endTime - startTime
        if(x_time>=ans):
            break
        else:
            endTime=time.time()
    print("時間到！",end="")
    startTime=time.time()
    input('')
    endTime=time.time()
    sun.append(endTime - startTime)
    if(n!=3):
        startTime=time.time()
        endTime=time.time()
        while 1:
            x_time=endTime - startTime
            if(x_time>=3):
                break
            else:
                endTime=time.time()

print(f"結果統計： {sun[0]:.3f} {sun[1]:.3f} {sun[2]:.3f}")

