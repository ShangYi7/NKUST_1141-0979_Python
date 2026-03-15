import time #匯入名稱為 time 的模組

input('按下 Enter 開始計時')
startTime = time.time() #模組所提供的一種函式(method)
#回傳從1970年1月1日到現在所經過秒數的浮點數
input('按下 Enter 停止計時')
endTime = time.time()
print(endTime - startTime)
print('經過時間(秒)：' + str(endTime - startTime))