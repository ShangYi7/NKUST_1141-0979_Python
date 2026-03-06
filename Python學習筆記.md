# Python 學習筆記 - NKUST 1141-0979

> 課程作業整理與知識點總結
>
> 最後更新：2026年3月7日

---

## 📑 目錄

1. [基礎概念](#1-基礎概念)
2. [迴圈與邏輯控制](#2-迴圈與邏輯控制)
3. [數學運算與算法](#3-數學運算與算法)
4. [字串處理](#4-字串處理)
5. [日期時間處理](#5-日期時間處理)
6. [進階數據處理](#6-進階數據處理)
7. [檔案操作](#7-檔案操作)
8. [考試題目](#8-考試題目)

---

## 1. 基礎概念

### 1.1 輸入與輸出

```python
# 基本輸入
data = input()  # 讀取一行字串

# 分割輸入為列表
data = input().split()  # 按空格分割
numbers = list(map(int, input().split()))  # 轉換為整數列表

# 格式化輸出
print("Hello")
print(value, end=" ")  # 不換行，以空格結尾
print(f"變數值: {variable}")  # f-string 格式化
```

### 1.2 資料類型轉換

```python
# 字串轉數字
x = int("123")      # 轉整數
y = float("3.14")   # 轉浮點數

# 列表轉換
numbers = list(map(int, ["1", "2", "3"]))  # ['1','2','3'] → [1,2,3]
```

---

## 2. 迴圈與邏輯控制

### 2.1 for 迴圈

```python
# 基本 for 迴圈
for i in range(10):  # 0 到 9
    print(i)

for i in range(1, 10):  # 1 到 9
    print(i)

# 巢狀迴圈
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
```

### 2.2 while 迴圈

```python
# 條件迴圈
while True:
    data = input()
    if data == "exit":
        break
```

### 2.3 條件判斷

```python
# if-elif-else
if condition1:
    # 執行程式碼
elif condition2:
    # 執行程式碼
else:
    # 執行程式碼

# 判斷奇偶數
if n % 2 == 0:
    print("偶數")
else:
    print("奇數")
```

---

## 3. 數學運算與算法

### 3.1 基本運算

```python
# 四則運算
a + b    # 加法
a - b    # 減法
a * b    # 乘法
a / b    # 除法 (浮點數)
a // b   # 整數除法
a % b    # 取餘數
a ** b   # 次方
```

### 3.2 最大公因數與最小公倍數

**題目：找出小於 100 的共同因數或共同倍數**

```python
# 共同因數 (Common Factor)
for j in range(1, 100):
    if d1 % j == 0 and d2 % j == 0:
        print(j, end=" ")

# 共同倍數 (Common Multiple)
for j in range(1, 100):
    if j % d1 == 0 and j % d2 == 0:
        print(j, end=" ")
```

**學習重點：**

- 因數：能整除該數的數字
- 倍數：該數的倍數
- 使用 `%` 運算子檢查整除性

### 3.3 統計計算

**題目：計算中位數與變異數**

```python
# 中位數 (Median)
data.sort()  # 先排序
if n % 2 == 1:  # 奇數個
    median = data[(n + 1) // 2 - 1]
else:  # 偶數個
    median = data[n // 2 - 1]

# 變異數 (Variance)
mean = sum(data) // n  # 平均值
variance = 0
for x in data:
    variance += (x - mean) * (x - mean)
variance //= n
```

**學習重點：**

- `sum()` 函數計算總和
- 變異數公式：每個數與平均值差的平方和除以總數
- 列表排序：`list.sort()`

### 3.4 進位制轉換

**題目：將 N 轉換為 B 進位制**

```python
n = data[0]  # 十進位數字
b = data[1]  # 目標進位制

x = 0
i = 1
while n != 0:
    a = n % b      # 取餘數
    x = x + a * i  # 建立新數字
    i *= 10        # 位數進位
    n //= b        # 整數除法
```

**學習重點：**

- 進位制轉換原理：不斷除以基數取餘數
- 由低位到高位建立結果

---

## 4. 字串處理

### 4.1 字串基本操作

```python
# 字串方法
text = "hello"
text.upper()    # 轉大寫: "HELLO"
text.lower()    # 轉小寫: "hello"
text.split()    # 分割為列表
len(text)       # 字串長度

# 字元判斷
'a' <= ch <= 'z'    # 小寫字母
'A' <= ch <= 'Z'    # 大寫字母
```

### 4.2 字元統計

**題目：統計字母出現次數並用星號顯示**

```python
# 使用字典計數
counts = {}
for ch in text:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        counts[ch] = counts.get(ch, 0) + 1

# 按固定順序輸出 (a-z, A-Z)
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
parts = []
for ch in letters:
    n = counts.get(ch, 0)
    if n:
        parts.append(ch + ' ' + ('*' * n))

print(' '.join(parts))
```

**學習重點：**

- 字典 (Dictionary) 用於計數
- `dict.get(key, default)` 方法
- 字串重複：`'*' * 5 = '*****'`

### 4.3 字串重複模式

**題目：生成指定長度的字串組合**

```python
L = int(parts[0])
t1 = parts[1]
t2 = parts[2]

for i in range(1, L + 1):
    print(t1 * i + t2 * (L - i))
```

**範例輸出：**

```
輸入: 5 A B
輸出:
ABBBB
AABBB
AAABB
AAAAB
AAAAA
```

---

## 5. 日期時間處理

### 5.1 calendar 模組

```python
import calendar

# 判斷閏年
calendar.isleap(year)  # True/False

# 取得星期幾 (0=Monday, 6=Sunday)
week = calendar.weekday(year, month, day)
```

### 5.2 datetime 模組

```python
import datetime

# 建立日期物件
current_date = datetime.date(year, month, day)

# 日期運算
new_date = current_date + datetime.timedelta(days=n)

# 取得年月日
new_date.year
new_date.month
new_date.day
```

### 5.3 實作範例

**題目：顯示日期對應的星期與計算前後日期**

```python
import calendar
import datetime

# 英文月份與星期列表
monthlist = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
weeklist = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]

# 取得星期
week = calendar.weekday(year, month, day)

# 格式化輸出
print(f"The day of the week on {monthlist[month-1]} {day:02d}, {year} is {weeklist[week]}")

# 計算 n 天後/前的日期
current_date = datetime.date(year, month, day)
new_day = current_date + datetime.timedelta(days=n)

if n < 0:
    n = abs(n)
    print(f"The date before {n} days is {monthlist[new_day.month-1]} {new_day.day:02d}, {new_day.year}")
else:
    print(f"The date after {n} days is {monthlist[new_day.month-1]} {new_day.day:02d}, {new_day.year}")
```

**學習重點：**

- `{day:02d}`: 補零至兩位數，例如 5 → 05
- `timedelta(days=n)`: 日期增減
- `abs()`: 取絕對值

---

## 6. 進階數據處理

### 6.1 列表排序與操作

```python
# 排序
data.sort()              # 升序排序（會修改原列表）
data.sort(reverse=True)  # 降序排序

# Lambda 排序
# 按第一個元素排序，相同時按第二個元素
data.sort(key=lambda x: (x[0], x[1]))

# 列表切片
data[0:5]   # 取前 5 個元素
data[-1]    # 最後一個元素
```

### 6.2 九九乘法表排序

**題目：特殊規則排序九九乘法表**

規則：

1. M1 為奇數的公式（先列出）
2. M1 為偶數但 M2 為奇數的公式
3. 剩餘公式（M1、M2 都是偶數）

```python
# 生成所有公式
all_formulas = []
for m1 in range(1, 10):
    for m2 in range(1, 10):
        p = m1 * m2
        all_formulas.append((m1, m2, p))

# 第一組：M1 為奇數
group1 = [(m1, m2, p) for m1, m2, p in all_formulas if m1 % 2 == 1]
group1.sort(key=lambda x: (x[0], x[1]))

# 第二組：M1 為偶數且 M2 為奇數
group2 = [(m1, m2, p) for m1, m2, p in all_formulas if m1 % 2 == 0 and m2 % 2 == 1]
group2.sort(key=lambda x: (x[0], x[1]))

# 第三組：M1、M2 都是偶數
group3 = [(m1, m2, p) for m1, m2, p in all_formulas if m1 % 2 == 0 and m2 % 2 == 0]
group3.sort(key=lambda x: (x[0], x[1]))

# 合併
all_sorted_formulas = group1 + group2 + group3
```

**學習重點：**

- Tuple (元組)：`(m1, m2, p)`
- List comprehension：`[x for x in list if condition]`
- Lambda 函數用於排序

### 6.3 二維圖案生成

**題目：生成同心方框圖案**

```python
L = int(input())
t = input().split()  # [t[0], t[1], t[2]] 三種符號
size = 2 * L - 1

for i in range(size):
    for j in range(size):
        # 計算到四個邊的距離
        top = i
        left = j
        bottom = size - 1 - i
        right = size - 1 - j

        # 層數 = 到最近邊的距離
        layer = min(top, left, bottom, right)

        # 選擇符號（循環使用）
        index = (L - 1 - layer) % 3
        token = t[index]

        print(token, end=" ")
    print()
```

**範例：** `L=3, t=['A', 'B', 'C']`

```
A A A A A
A B B B A
A B C B A
A B B B A
A A A A A
```

**學習重點：**

- 二維迴圈繪圖
- `min()` 函數找最小值
- 索引循環：使用 `%` 運算子

---

## 7. 檔案操作

### 7.1 基本檔案讀寫

```python
# 讀取檔案
f = open('input.txt', 'r')
lines = f.readlines()  # 讀取所有行
f.close()

# 寫入檔案
f = open('output.txt', 'w')
f.write("Hello World\n")
f.close()

# 使用 with 語句（推薦）
with open('file.txt', 'r') as f:
    content = f.read()
```

### 7.2 顧客資料管理系統

**題目：實作簡單的資料庫系統**

指令格式：

- `@` ID NAME PHONE ADDRESS：新增
- `#` ID：刪除
- `!` ID FIELD VALUE：更新
- `$` ID FIELD：查詢
- `*`：結束

```python
# 讀取檔案資料
customers = {}
try:
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        parts = line.split()
        if len(parts) >= 4:
            customers[parts[0]] = [parts[1], parts[2], parts[3]]
except:
    pass

# 新增顧客
if parts[0] == '@' and len(parts) >= 5:
    if parts[1] in customers:
        print('Exist')
    else:
        customers[parts[1]] = [parts[2], parts[3], parts[4]]
        # 寫入檔案
        f = open('input.txt', 'w')
        for id in customers:
            f.write(id + ' ' + customers[id][0] + ' ' +
                   customers[id][1] + ' ' + customers[id][2] + '\n')
        f.close()

# 刪除顧客
elif parts[0] == '#' and len(parts) >= 2:
    if parts[1] in customers:
        del customers[parts[1]]
        # 更新檔案...
    else:
        print('None')

# 更新顧客資料
elif parts[0] == '!' and len(parts) >= 4:
    if parts[1] in customers:
        field_index = int(parts[2])
        customers[parts[1]][field_index] = parts[3]
        # 更新檔案...
    else:
        print('None')

# 查詢顧客資料
elif parts[0] == '$' and len(parts) >= 3:
    if parts[1] in customers:
        field_index = int(parts[2])
        print(customers[parts[1]][field_index])
    else:
        print('None')
```

**學習重點：**

- 字典 (Dictionary) 作為資料庫
- 檔案讀寫同步
- `del` 刪除字典元素
- 例外處理：`try-except`

---

## 8. 考試題目

### 8.1 考試一 (test1)

#### 題目 1：溫度轉換

```python
# 攝氏轉華氏：F = (C * 9) / 5 + 32
c = float(input())
F = (c * 9) / 5 + 32
print(F)
```

### 8.2 考試三 (test3)

#### 題目 1：數字轉中文（未完成）

```python
chin = ["零","一","二","三","四","五","六","七","八","九"]
f = open("input.text", "r")  # 語法錯誤：應為 'r'
```

**注意：** 此題目未完成，open() 第二參數應為字串 `'r'`

### 8.3 剪刀石頭布遊戲

**版本 1：10 局猜拳**

```python
# 1=剪刀, 2=石頭, 3=布
# 讀取 10 組輸入
for _ in range(10):
    a = list(map(int, input().split()))
    player1, player2 = a[0], a[1]

    if player1 == player2:
        print("A tie")
    elif (player1 == 1 and player2 == 3) or \
         (player1 == 2 and player2 == 1) or \
         (player1 == 3 and player2 == 2):
        print("The first man wins the game")
    else:
        print("The second man wins the game")
```

**版本 2：N 戰 (N+1)/2 勝**

```python
# Y=剪刀, M=石頭, O=布
while True:
    n = int(input())
    if n % 2 == 0 or n <= 0:  # 必須是正奇數
        break

    win1 = 0
    win2 = 0
    win_threshold = (n + 1) / 2

    while True:
        data = input().split()
        player1, player2 = data[0], data[1]

        # 判斷勝負
        if (player1 == "Y" and player2 == "O") or \
           (player1 == "M" and player2 == "Y") or \
           (player1 == "O" and player2 == "M"):
            win1 += 1
        elif (player2 == "Y" and player1 == "O") or \
             (player2 == "M" and player1 == "Y") or \
             (player2 == "O" and player1 == "M"):
            win2 += 1

        # 檢查是否有人獲勝
        if win1 >= win_threshold:
            print("The first person wins the game")
            break
        elif win2 >= win_threshold:
            print("The second person wins the game")
            break
```

**學習重點：**

- 邏輯判斷的簡化
- 勝負規則的程式化
- 計數器的使用

---

## 9. F-String 格式化（重要！）

f-string 是 Python 3.6+ 的字串格式化方式，**可讀性高**、**速度快**。

### 9.1 基本用法

```python
name = "Alice"
age = 20

print(f"Hello, {name}!")  # Hello, Alice!
print(f"I am {age} years old")  # I am 20 years old
```

### 9.2 數字格式化

```python
number = 5
pi = 3.1415926

# 補零
print(f"{number:02d}")  # 05 (補零至2位)
print(f"{number:05d}")  # 00005 (補零至5位)

# 千分位
large_num = 1000000
print(f"{large_num:,}")  # 1,000,000

# 小數位數
print(f"{pi:.2f}")  # 3.14 (保留2位小數)

# 百分比
percent = 0.856
print(f"{percent:.1%}")  # 85.6%
```

### 9.3 表達式與函數

```python
a = 10
b = 20
text = "hello"

print(f"Total: {a + b}")  # Total: 30
print(f"Upper: {text.upper()}")  # Upper: HELLO
```

### 9.4 文字對齊

```python
text = "Hi"

# < 靠左, > 靠右, ^ 置中
print(f"|{text:>10}|")   # |        Hi|
print(f"|{text:<10}|")   # |Hi        |
print(f"|{text:^10}|")   # |    Hi    |
print(f"|{text:-^10}|")  # |----Hi----|
```

### 9.5 除錯模式 (Python 3.8+)

```python
user = "Alice"
score = 95

print(f"{user=}")   # user='Alice'
print(f"{score=}")  # score=95
print(f"{1+1=}")    # 1+1=2
```

---

## 10. 實用技巧總結

### 10.1 常見錯誤

```python
# ❌ 錯誤：忘記轉換類型
data = input().split()
result = data[0] + data[1]  # 字串相加，不是數字

# ✅ 正確：轉換為數字
data = list(map(int, input().split()))
result = data[0] + data[1]  # 數字相加
```

```python
# ❌ 錯誤：整數除法使用 /
median = data[n / 2]  # 可能產生浮點數索引

# ✅ 正確：使用 //
median = data[n // 2]  # 整數除法
```

### 10.2 輸入處理模板

```python
# 單行輸入
n = int(input())

# 多個數字
a, b, c = map(int, input().split())

# 列表輸入
data = list(map(int, input().split()))

# 持續輸入直到條件
while True:
    n = int(input())
    if n == 0:
        break
    # 處理...
```

### 10.3 效能優化

```python
# 使用 list comprehension（較快）
squares = [x*x for x in range(10)]

# 而非傳統迴圈
squares = []
for x in range(10):
    squares.append(x*x)
```

---

## 11. 重要概念速查

| 概念 | 說明 | 範例 |
|------|------|------|
| 整數除法 | `//` | `7 // 2 = 3` |
| 取餘數 | `%` | `7 % 2 = 1` |
| 次方 | `**` | `2 ** 3 = 8` |
| 字串重複 | `*` | `'A' * 3 = 'AAA'` |
| 列表排序 | `.sort()` | `data.sort()` |
| 字典計數 | `dict.get(key, 0)` | `count.get('a', 0)` |
| 列表總和 | `sum()` | `sum([1,2,3]) = 6` |
| 絕對值 | `abs()` | `abs(-5) = 5` |
| 最小/最大值 | `min()` / `max()` | `min([1,2,3]) = 1` |

---

## 12. 學習建議

1. **多練習輸入處理**：很多題目的關鍵在於正確解析輸入格式
2. **熟悉 f-string**：現代 Python 的標準格式化方式
3. **理解迴圈邏輯**：巢狀迴圈是很多算法的基礎
4. **掌握列表操作**：排序、切片、comprehension
5. **練習除錯**：使用 `print()` 或 f-string 的 `{var=}` 模式
6. **閱讀題目**：仔細理解題目要求的輸出格式

---

## 📚 參考資源

- [Python 官方文件](https://docs.python.org/zh-tw/3/)
- [f-string 詳細說明](09/f-string.md)
- 各作業資料夾：01-12
- 測試題目：test1, test3, test4

---

## 🎯 作業完成度檢查表

- [x] 01 - 九九乘法表排序
- [x] 02 - 剪刀石頭布
- [x] 03 - 公因數與公倍數
- [x] 04 - 字母統計（星號顯示）
- [x] 05 - 字串重複模式
- [x] 06 - 剪刀石頭布進階版
- [x] 07 - 共同倍數查詢
- [x] 08 - 二維圖案生成
- [x] 09 - 日期時間處理
- [x] 10 - 中位數與變異數
- [x] 11 - 進位制轉換
- [x] 12 - 檔案資料管理系統

---

**筆記製作日期：** 2026年3月7日
**課程代碼：** NKUST 1141-0979
**程式語言：** Python 3.13.7
