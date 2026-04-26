data = input()
# 將輸入的攝氏溫度轉成浮點數，方便做公式計算
c = float(data)

# 攝氏轉華氏：F = C * 9 / 5 + 32
F = (c*9)/5+32
print(F)
