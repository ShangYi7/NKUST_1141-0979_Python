# Chapter 06 - 模組與函數

> 掌握模組化程式設計與標準庫應用

---

## 📋 本章目標

- 理解函數定義與呼叫
- 掌握 Lambda 表達式
- 學會使用標準庫模組
- 實作日期計算工具

---

## 6.1 函數基礎

### 6.1.1 定義函數

```python
# 基本函數
def greet():
    print("Hello!")

greet()  # 呼叫函數

# 帶參數的函數
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# 帶預設值的參數
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}")

greet_with_title("Smith")           # Hello, Mr. Smith
greet_with_title("Jones", "Dr.")    # Hello, Dr. Jones
```

### 6.1.2 返回值

```python
# 單一返回值
def add(a, b):
    return a + b

result = add(3, 5)  # 8

# 多重返回值（實際返回元組）
def get_student_info():
    name = "Alice"
    age = 20
    score = 85
    return name, age, score

name, age, score = get_student_info()

# 提早返回
def is_even(n):
    if n % 2 == 0:
        return True
    return False
```

### 6.1.3 參數類型

```python
# 位置參數
def power(base, exponent):
    return base ** exponent

power(2, 3)  # 8

# 關鍵字參數
power(base=2, exponent=3)  # 8
power(exponent=3, base=2)  # 8（順序可調換）

# 任意數量參數 (*args)
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4, 5)  # 15

# 任意關鍵字參數 (**kwargs)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=20, score=85)
```

---

## 6.2 Lambda 表達式

### 6.2.1 基本語法

```python
# 一般函數
def square(x):
    return x ** 2

# Lambda 版本
square = lambda x: x ** 2

print(square(5))  # 25

# 多個參數
add = lambda a, b: a + b
print(add(3, 5))  # 8
```

### 6.2.2 實際應用

```python
# 排序中的應用
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

# 按分數排序
students.sort(key=lambda x: x[1])

# map 中的應用
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

# filter 中的應用
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

---

## 6.3 datetime 模組

### 6.3.1 日期物件

```python
import datetime

# 建立日期
today = datetime.date.today()
print(today)  # 2026-03-07

# 指定日期
birthday = datetime.date(2000, 1, 1)
print(birthday)  # 2000-01-01

# 取得年月日
print(today.year)    # 2026
print(today.month)   # 3
print(today.day)     # 7

# 星期幾（0=Monday, 6=Sunday）
print(today.weekday())     # 5（Saturday）
print(today.isoweekday())  # 6（Saturday）
```

### 6.3.2 時間差運算

```python
import datetime

# timedelta 物件
one_day = datetime.timedelta(days=1)
one_week = datetime.timedelta(weeks=1)

# 日期運算
today = datetime.date.today()
tomorrow = today + one_day
next_week = today + one_week
yesterday = today - one_day

# 計算兩個日期的差距
date1 = datetime.date(2026, 1, 1)
date2 = datetime.date(2026, 3, 7)
diff = date2 - date1
print(diff.days)  # 65 天
```

### 6.3.3 日期時間

```python
import datetime

# 完整的日期時間
now = datetime.datetime.now()
print(now)  # 2026-03-07 10:30:45.123456

# 指定日期時間
dt = datetime.datetime(2026, 3, 7, 10, 30, 45)

# 轉換為字串
print(dt.strftime("%Y-%m-%d"))       # "2026-03-07"
print(dt.strftime("%Y/%m/%d %H:%M"))  # "2026/03/07 10:30"

# 從字串解析
date_str = "2026-03-07"
parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d")
```

---

## 6.4 calendar 模組

### 6.4.1 基本功能

```python
import calendar

# 判斷閏年
print(calendar.isleap(2024))  # True
print(calendar.isleap(2025))  # False

# 取得星期幾
weekday = calendar.weekday(2026, 3, 7)  # 5（Saturday）

# 取得某月有幾天
days = calendar.monthrange(2026, 2)  # (6, 28)
# (6, 28) 表示該月1號是星期日（6），該月有28天
```

### 6.4.2 輸出月曆

```python
import calendar

# 輸出某月的月曆
print(calendar.month(2026, 3))

# 輸出全年月曆
print(calendar.calendar(2026))
```

---

## 6.5 實戰：日期計算工具

### 📝 題目

實作日期查詢與計算工具：

1. 顯示指定日期是星期幾
2. 計算 N 天後/前的日期

**輸入格式：** `YYYY-MM-DD N`
**輸出格式：**

- The day of the week on Month DD, YYYY is Weekday
- The date after/before N days is Month DD, YYYY

### ✅ 解答

```python
import calendar
import datetime

# 英文月份與星期列表
monthlist = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
weeklist = [
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
]

while True:
    data = input().split()
    date_str = data[0]
    n = int(data[1])

    # 解析日期
    year = int(date_str[0:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])

    # 檢查閏年（2月29日）
    if not calendar.isleap(year) and month == 2 and day == 29:
        break

    # 取得星期
    week = calendar.weekday(year, month, day)

    # 格式化輸出第一行
    print(f"The day of the week on {monthlist[month-1]} {day:02d}, {year} is {weeklist[week]}")

    # 計算 N 天後/前的日期
    current_date = datetime.date(year, month, day)
    new_date = current_date + datetime.timedelta(days=n)

    # 格式化輸出第二行
    if n < 0:
        n_abs = abs(n)
        print(f"The date before {n_abs} days is {monthlist[new_date.month-1]} {new_date.day:02d}, {new_date.year}")
    else:
        print(f"The date after {n} days is {monthlist[new_date.month-1]} {new_date.day:02d}, {new_date.year}")
```

### 🔍 關鍵技巧

```python
# 1. 字串切片解析日期
date_str = "2026-03-07"
year = int(date_str[0:4])   # 2026
month = int(date_str[5:7])  # 3
day = int(date_str[8:10])   # 7

# 2. f-string 補零
print(f"{day:02d}")  # 07

# 3. timedelta 日期運算
new_date = current_date + datetime.timedelta(days=n)

# 4. 取絕對值
n_abs = abs(n)
```

---

## 6.6 其他常用標準庫

### 6.6.1 math 模組

```python
import math

# 數學常數
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045

# 常用函數
math.sqrt(16)      # 4.0（平方根）
math.pow(2, 3)     # 8.0（次方）
math.ceil(3.2)     # 4（無條件進位）
math.floor(3.8)    # 3（無條件捨去）
math.factorial(5)  # 120（階乘）

# 三角函數
math.sin(math.pi/2)  # 1.0
math.cos(0)          # 1.0
```

### 6.6.2 random 模組

```python
import random

# 隨機整數
random.randint(1, 10)  # 1-10 的隨機整數

# 隨機浮點數
random.random()        # 0-1 的隨機浮點數
random.uniform(1, 10)  # 1-10 的隨機浮點數

# 隨機選擇
random.choice(['a', 'b', 'c'])  # 隨機選一個

# 洗牌
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)  # 原地打亂
```

### 6.6.3 collections 模組

```python
from collections import Counter, defaultdict, deque

# Counter：計數器
counts = Counter("hello world")
print(counts)  # Counter({'l': 3, 'o': 2, ...})
print(counts.most_common(2))  # [('l', 3), ('o', 2)]

# defaultdict：有預設值的字典
dd = defaultdict(int)  # 預設值為 0
dd['a'] += 1  # 不需要先初始化

# deque：雙端佇列
dq = deque([1, 2, 3])
dq.append(4)      # [1, 2, 3, 4]
dq.appendleft(0)  # [0, 1, 2, 3, 4]
dq.popleft()      # 0，剩餘 [1, 2, 3, 4]
```

---

## 6.7 自訂模組

### 6.7.1 建立模組

```python
# mymath.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159
```

### 6.7.2 匯入模組

```python
# 方法 1：匯入整個模組
import mymath
result = mymath.add(3, 5)
print(mymath.PI)

# 方法 2：匯入特定函數
from mymath import add, PI
result = add(3, 5)
print(PI)

# 方法 3：匯入所有（不推薦）
from mymath import *
```

---

## 📝 本章總結

### 核心概念

1. **函數**封裝可重用的程式碼
2. **Lambda**適合簡單的單行函數
3. **datetime**處理日期時間
4. **calendar**提供日曆相關功能
5. **標準庫**提供豐富的工具

### 常用模組速查

| 模組 | 用途 | 常用功能 |
|------|------|----------|
| `datetime` | 日期時間 | date, timedelta, strftime |
| `calendar` | 日曆 | isleap, weekday, month |
| `math` | 數學 | sqrt, ceil, floor, pi |
| `random` | 隨機 | randint, choice, shuffle |
| `collections` | 容器 | Counter, defaultdict, deque |

---

## 🎯 練習題

1. 實作計算兩個日期之間相差幾天的函數
2. 實作判斷某年某月有幾個星期幾（如：幾個星期日）
3. 實作自動生成月曆的函數
4. 實作計算某人出生至今有幾天的工具

---

**上一章：** [Chapter 05 - 數學與演算法](./Chapter05-數學與演算法.md)
**下一章：** [Chapter 07 - 檔案與例外處理](./Chapter07-檔案操作.md)
