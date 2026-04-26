data1 = int(input())
data2 = int(input())

# 輸出基本四則與平方差運算
print(data1, "-", data2, "=", data1-data2)
print(data1, "x", data2, "=", data1*data2)
print(data1, "%", data2, "=", data1 % data2)
print(data1, "^2-", data2, "^2=", data1*data1-data2*data2)

# 逐一尋找第一個同時可被兩個數整除的正整數，作為最小公倍數
for j in range(1, 1000):
    if (j % data1 == 0 and j % data2 == 0):
        print("最小公倍數：", j)
        break
