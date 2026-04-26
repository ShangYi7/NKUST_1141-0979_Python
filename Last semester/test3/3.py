import time  # 匯入名稱為 time 的模組

input('按下 Enter 開始計時')
# time.time() 取得目前時間戳記，可用來計算經過多久
startTime = time.time()  # 模組所提供的一種函式(method)
# 回傳從1970年1月1日到現在所經過秒數的浮點數
input('按下 Enter 停止計時')
endTime = time.time()
# 兩次時間戳記相減就是經過時間
print(endTime - startTime)
print('經過時間(秒)：' + str(endTime - startTime))
