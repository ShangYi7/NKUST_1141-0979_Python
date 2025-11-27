data1=int(input())
data2=int(input())

print(data1,"-",data2,"=",data1-data2)
print(data1,"x",data2,"=",data1*data2)
print(data1,"%",data2,"=",data1%data2)
print(data1,"^2-",data2,"^2=",data1*data1-data2*data2)

for j in range(1, 1000):
    if (j % data1 == 0 and j % data2 == 0):
        print("最小公倍數：",j)
        break