from random import randint
# 題目要求先輸入範圍，再在範圍內隨機猜數字
print("請輸入兩正整數作為範圍")
data = list(map(int, input().split()))
x = 0
if (data[0] != data[1] and (data[0]-data[1] > 1 or data[1]-data[0] > 1)):
    if (data[1] > data[0]):
        # 先決定隨機答案與目前可猜的上下界
        pase = (randint(data[0]+1, data[1]-1))
        end = data[1]
        start = data[0]
    else:
        pase = (randint(data[1]+1, data[0]-1))
        end = data[0]
        start = data[1]
    print("答案", pase)
    print(start, " ~ ", end, "，請輸入數字")
    while 1:
        # 持續接收猜測，直到猜中為止
        ans = int(input())
        if ((data[1] > data[0] and (ans < start or ans > end)) or (data[1] < data[0] and (ans < end or ans > start))):
            print("輸入錯誤，請重新輸入")
            print(start, " ~ ", end, "，請輸入數字")
        elif (ans == pase):
            # 猜中後結束並顯示猜測次數
            x = x+1
            print("正確答案")
            print("猜測次數為 ", x)
        else:
            # 沒猜中就縮小範圍繼續猜
            x = x+1
            if (ans < pase):
                start = ans
            elif (ans > pase):
                end = ans
            print(start, " ~ ", end, "，請輸入數字")


else:
    # 範圍不合法時直接輸出錯誤
    print("錯誤")
