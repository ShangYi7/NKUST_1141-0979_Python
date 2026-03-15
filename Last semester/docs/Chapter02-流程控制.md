# Chapter 02 - 流程控制與迴圈

> 掌握 Python 的控制流程，寫出邏輯清晰的程式

---

## 📋 本章目標

- 理解 Python 的條件判斷語法
- 掌握各種迴圈的使用時機
- 學會使用 break、continue、else
- 實作剪刀石頭布遊戲系統

---

## 2.1 條件判斷

### 2.1.1 if-elif-else 語法

```python
# 基本結構
x = 10

if x > 0:
    print("正數")
elif x < 0:
    print("負數")
else:
    print("零")
```

**與 C/C++ 的差異：**

```python
# Python
if condition:    # 冒號，沒有括號
    statement    # 縮排定義區塊

# C/C++
if (condition) {  // 括號，大括號
    statement;
}
```

### 2.1.2 縮排規則

Python 使用**縮排**（Indentation）定義程式區塊：

```python
# ✅ 正確：一致的縮排（建議 4 空格）
if x > 0:
    print("Line 1")
    print("Line 2")
print("Outside")

# ❌ 錯誤：縮排不一致
if x > 0:
    print("Line 1")
      print("Line 2")  # IndentationError

# ❌ 錯誤：混用 tab 和空格
if x > 0:
    print("Tab")    # 用 tab
    print("Space")  # 用空格
```

**最佳實踐：** 使用 4 個空格，設定編輯器自動將 Tab 轉為空格

### 2.1.3 比較運算進階

```python
# 鏈式比較（Python 特色）
age = 25
if 18 <= age < 65:
    print("工作年齡")

# 相當於
if age >= 18 and age < 65:
    print("工作年齡")

# 多條件判斷
score = 85
passed = True

if score >= 60 and passed:
    print("及格")

# 成員檢查
if x in [1, 2, 3, 4, 5]:
    print("x 在列表中")

# 身份檢查
if x is None:
    print("x 是 None")
```

### 2.1.4 真值檢測（Truthiness）

Python 中很多值可以直接當作布林值使用：

```python
# False 的值：
# - None
# - False
# - 數字 0 (0, 0.0, 0j)
# - 空序列 ('', [], ())
# - 空字典 {}
# - 空集合 set()

# 空字串檢查
text = ""
if not text:  # 等同於 if text == ""
    print("空字串")

# 空列表檢查
items = []
if not items:  # 等同於 if len(items) == 0
    print("沒有項目")

# ✅ Pythonic 寫法
if items:  # 有元素就執行
    print("有項目")

# ❌ 不 Pythonic
if len(items) > 0:
    print("有項目")
```

### 2.1.5 三元運算子

```python
# Python 的條件表達式
age = 20
status = "成年" if age >= 18 else "未成年"

# 相當於
if age >= 18:
    status = "成年"
else:
    status = "未成年"

# 巢狀三元運算（不建議，可讀性差）
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
```

---

## 2.2 for 迴圈

### 2.2.1 基本用法

```python
# range() 函數
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# 指定起始值
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

# 指定步長
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# 倒序
for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i)
```

**range() 詳解：**

```python
# range(stop) - 從 0 到 stop-1
range(5)  # [0, 1, 2, 3, 4]

# range(start, stop) - 從 start 到 stop-1
range(2, 5)  # [2, 3, 4]

# range(start, stop, step) - 從 start 到 stop-1，步長 step
range(0, 10, 2)  # [0, 2, 4, 6, 8]

# 注意：range 回傳的是 range 物件，不是列表
print(type(range(5)))  # <class 'range'>
print(list(range(5)))  # [0, 1, 2, 3, 4]
```

### 2.2.2 遍歷序列

```python
# 遍歷列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍歷字串
for char in "Hello":
    print(char)  # H, e, l, l, o

# 遍歷字典
scores = {"Alice": 90, "Bob": 85}
for name in scores:
    print(name, scores[name])

# 更好的字典遍歷
for name, score in scores.items():
    print(f"{name}: {score}")
```

### 2.2.3 enumerate() - 取得索引

```python
# 想要索引和值
fruits = ["apple", "banana", "cherry"]

# ❌ 不好的做法
for i in range(len(fruits)):
    print(i, fruits[i])

# ✅ Pythonic 做法
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry

# 指定起始索引
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry
```

### 2.2.4 巢狀迴圈

```python
# 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} × {j} = {i*j:2d}", end="  ")
    print()  # 換行

# 二維座標
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})", end=" ")
    print()
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)
```

---

## 2.3 while 迴圈

### 2.3.1 基本用法

```python
# 計數器模式
count = 0
while count < 5:
    print(count)
    count += 1  # Python 沒有 count++

# 條件模式
user_input = ""
while user_input != "quit":
    user_input = input("輸入指令（quit 離開）：")
```

### 2.3.2 無限迴圈

```python
# 常見模式：持續讀取直到特定條件
while True:
    n = int(input())
    if n == 0:
        break  # 跳出迴圈
    print(f"你輸入了 {n}")

# 等待正確輸入
while True:
    try:
        age = int(input("請輸入年齡："))
        if 0 < age < 150:
            break
        print("年齡不合理")
    except ValueError:
        print("請輸入數字")
```

### 2.3.3 for vs while 選擇

| 情況 | 選擇 | 原因 |
|------|------|------|
| 已知迴圈次數 | for | 更簡潔 |
| 遍歷序列 | for | 更 Pythonic |
| 未知次數（條件驅動） | while | 更靈活 |
| 需要隨時中斷 | while | 可用 break |

```python
# ✅ 適合用 for
for i in range(10):
    print(i)

# ❌ 不必要的 while
i = 0
while i < 10:
    print(i)
    i += 1

# ✅ 適合用 while
password = ""
while password != "secret":
    password = input("輸入密碼：")
```

---

## 2.4 break、continue、else

### 2.4.1 break - 中斷迴圈

```python
# 找到第一個符合條件的值就停止
for i in range(10):
    if i == 5:
        break  # 跳出迴圈
    print(i)
# 輸出：0 1 2 3 4

# 巢狀迴圈中的 break 只會跳出內層
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # 只跳出內層 for
        print(f"({i}, {j})", end=" ")
    print()
# (0, 0)
# (1, 0)
# (2, 0)
```

### 2.4.2 continue - 跳過本次迭代

```python
# 跳過偶數
for i in range(10):
    if i % 2 == 0:
        continue  # 跳過後面的程式碼，進入下一次迭代
    print(i)
# 輸出：1 3 5 7 9

# 過濾負數
numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        continue
    print(num)
# 輸出：1 3 5
```

### 2.4.3 else - 迴圈正常結束時執行

Python 迴圈有 **else** 子句，這是很多語言沒有的特性：

```python
# 正常結束（沒有 break）
for i in range(5):
    print(i)
else:
    print("迴圈正常結束")
# 輸出：0 1 2 3 4 迴圈正常結束

# 被 break 中斷（不執行 else）
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("這不會執行")
# 輸出：0 1 2
```

**實用案例：搜尋**

```python
# 搜尋列表中的元素
numbers = [1, 3, 5, 7, 9]
target = 6

for num in numbers:
    if num == target:
        print(f"找到 {target}")
        break
else:
    print(f"找不到 {target}")
# 輸出：找不到 6

# while 迴圈也可以使用 else
n = int(input())
while n % 2 == 0:
    n //= 2
else:
    print(f"最後的奇數：{n}")
```

---

## 2.5 實戰：剪刀石頭布遊戲

### 📝 題目 1：基本版（單局）

兩個玩家猜拳，判斷誰贏。

**規則：**

- 1 = 剪刀
- 2 = 石頭
- 3 = 布

**輸入：** 兩個數字（玩家 1 和玩家 2 的出拳）
**輸出：**

- `The first man wins the game` - 玩家 1 贏
- `The second man wins the game` - 玩家 2 贏
- `A tie` - 平手

### 💡 思路分析

```python
# 勝負規則：
# 剪刀(1) 贏 布(3)
# 石頭(2) 贏 剪刀(1)
# 布(3) 贏 石頭(2)

# 方法 1：窮舉所有情況
if p1 == p2:
    # 平手
elif (p1 == 1 and p2 == 3) or \
     (p1 == 2 and p2 == 1) or \
     (p1 == 3 and p2 == 2):
    # 玩家 1 贏
else:
    # 玩家 2 贏
```

### ✅ 解答 1：窮舉法

```python
# 讀取輸入
p1, p2 = map(int, input().split())

# 判斷勝負
if p1 == p2:
    print("A tie")
elif p1 == 1 and p2 == 2:  # 剪刀 vs 石頭
    print("The second man wins the game")
elif p1 == 1 and p2 == 3:  # 剪刀 vs 布
    print("The first man wins the game")
elif p1 == 2 and p2 == 1:  # 石頭 vs 剪刀
    print("The first man wins the game")
elif p1 == 2 and p2 == 3:  # 石頭 vs 布
    print("The second man wins the game")
elif p1 == 3 and p2 == 1:  # 布 vs 剪刀
    print("The second man wins the game")
elif p1 == 3 and p2 == 2:  # 布 vs 石頭
    print("The first man wins the game")
```

### ✅ 解答 2：簡化版

```python
p1, p2 = map(int, input().split())

if p1 == p2:
    print("A tie")
elif (p1 == 1 and p2 == 3) or \
     (p1 == 2 and p2 == 1) or \
     (p1 == 3 and p2 == 2):
    print("The first man wins the game")
else:
    print("The second man wins the game")
```

### ✅ 解答 3：數學技巧（最優雅）

```python
p1, p2 = map(int, input().split())

if p1 == p2:
    print("A tie")
elif (p1 - p2) % 3 == 1:
    # 利用模運算判斷：(1-3)%3=1, (2-1)%3=1, (3-2)%3=1
    print("The first man wins the game")
else:
    print("The second man wins the game")
```

**數學原理：**

```
p1 贏的情況：
1 - 3 = -2 ≡ 1 (mod 3)
2 - 1 =  1 ≡ 1 (mod 3)
3 - 2 =  1 ≡ 1 (mod 3)
```

---

### 📝 題目 2：進階版（N 戰 M 勝制）

進行 N 局猜拳（N 為奇數），先贏 (N+1)/2 局者獲勝。

**符號：**

- `Y` = 剪刀
- `M` = 石頭
- `O` = 布

**輸入：**

- 第一行：N（正奇數）
- 接下來每行：兩個玩家的出拳

**輸出：**

- `The first person wins the game`
- `The second person wins the game`

### 💡 範例

```
輸入：
3
Y M
O Y
M O

過程：
第1局：Y vs M → 玩家2贏（石頭贏剪刀）
第2局：O vs Y → 玩家2贏（剪刀贏布）
玩家2贏了2局 ≥ (3+1)/2 = 2 → 遊戲結束

輸出：
The second person wins the game
```

### ✅ 解答

```python
# 主迴圈：持續讀取遊戲
while True:
    n = int(input())

    # 檢查是否為正奇數
    if n % 2 == 0 or n <= 0:
        break

    # 初始化計數器
    win1 = 0  # 玩家1贏的次數
    win2 = 0  # 玩家2贏的次數
    win_threshold = (n + 1) / 2  # 獲勝所需局數

    # 進行遊戲
    while True:
        p1, p2 = input().split()

        # 判斷勝負
        if p1 == p2:
            # 平手，不計分
            pass
        elif (p1 == "Y" and p2 == "O") or \
             (p1 == "M" and p2 == "Y") or \
             (p1 == "O" and p2 == "M"):
            win1 += 1
        else:
            win2 += 1

        # 檢查是否有人獲勝
        if win1 >= win_threshold:
            print("The first person wins the game")
            break
        elif win2 >= win_threshold:
            print("The second person wins the game")
            break
```

### 🔍 程式碼解析

```python
# 1. 外層 while True：可以進行多場遊戲
while True:
    n = int(input())
    if n % 2 == 0 or n <= 0:  # 驗證輸入
        break

# 2. 獲勝條件
win_threshold = (n + 1) / 2
# N=3 → 需贏2局
# N=5 → 需贏3局
# N=7 → 需贏4局

# 3. 內層 while True：進行單場遊戲
while True:
    # 讀取並判斷
    # ...

    # 檢查是否有人獲勝
    if win1 >= win_threshold:
        print("...")
        break  # 跳出內層迴圈，進入下一場
```

---

## 2.6 常見模式總結

### 模式 1：計數迴圈

```python
# 執行 N 次
for i in range(N):
    # 做某事
```

### 模式 2：遍歷序列

```python
# 遍歷所有元素
for item in items:
    # 處理 item
```

### 模式 3：條件累加

```python
# 累計總和
total = 0
for num in numbers:
    total += num

# 計數符合條件的數量
count = 0
for num in numbers:
    if num > 0:
        count += 1
```

### 模式 4：搜尋

```python
# 找到第一個符合條件的
for item in items:
    if condition(item):
        result = item
        break
else:
    result = None  # 沒找到
```

### 模式 5：雙層迴圈生成組合

```python
# 生成所有配對
for i in range(n):
    for j in range(m):
        process(i, j)
```

### 模式 6：持續輸入直到條件

```python
while True:
    data = input()
    if stop_condition(data):
        break
    process(data)
```

---

## 2.7 效能考量

### 避免不必要的計算

```python
# ❌ 每次都計算 len()
for i in range(len(items)):
    if i < len(items) - 1:  # 重複計算
        pass

# ✅ 預先計算
n = len(items)
for i in range(n):
    if i < n - 1:
        pass
```

### 使用 break 提早結束

```python
# ❌ 找到後還繼續迴圈
found = False
for item in items:
    if item == target:
        found = True
# 繼續跑完整個迴圈

# ✅ 找到就停止
found = False
for item in items:
    if item == target:
        found = True
        break  # 立即停止
```

---

## 📝 本章總結

### 核心概念

1. **Python 使用縮排定義區塊**，必須一致
2. **for 迴圈**適合已知次數或遍歷序列
3. **while 迴圈**適合條件驅動的情況
4. **break** 跳出迴圈，**continue** 跳過本次迭代
5. **else** 子句在迴圈正常結束時執行

### 必記語法

```python
# 條件判斷
if condition:
    pass
elif condition:
    pass
else:
    pass

# for 迴圈
for i in range(n):
    pass

for item in items:
    pass

for i, item in enumerate(items):
    pass

# while 迴圈
while condition:
    pass

while True:
    if stop_condition:
        break
```

---

## 🎯 練習題

### 基礎題

1. 輸出 1 到 100 的所有偶數
2. 計算 1 到 N 的總和
3. 判斷一個數字是否為質數

### 進階題

1. 找出兩個數字的最大公因數（GCD）
2. 印出所有的完全數（小於 1000）
3. 實作 FizzBuzz（1-100，3的倍數印Fizz，5的倍數印Buzz，15的倍數印FizzBuzz）

### 挑戰題

1. 實作五子棋的勝負判斷
2. 生成帕斯卡三角形（Pascal's Triangle）
3. 實作石頭剪刀布蜥蜴史波克（多人版本）

---

**上一章：** [Chapter 01 - 基礎語法](./Chapter01-基礎語法.md)
**下一章：** [Chapter 03 - 資料結構](./Chapter03-資料結構.md)
