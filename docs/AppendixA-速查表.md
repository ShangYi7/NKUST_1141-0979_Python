# 附錄 A - Python 速查表

> 快速查詢常用語法與函數

---

## A.1 基本語法

### 變數與型別

```python
# 變數賦值
x = 10
name = "Alice"

# 多重賦值
a, b, c = 1, 2, 3

# 交換變數
a, b = b, a

# 型別檢查
type(x)          # <class 'int'>
isinstance(x, int)  # True
```

### 運算子

| 運算子 | 說明 | 範例 |
|--------|------|------|
| `+` | 加法 | `5 + 3 = 8` |
| `-` | 減法 | `5 - 3 = 2` |
| `*` | 乘法 | `5 * 3 = 15` |
| `/` | 除法（浮點） | `5 / 2 = 2.5` |
| `//` | 整數除法 | `5 // 2 = 2` |
| `%` | 取餘數 | `5 % 2 = 1` |
| `**` | 次方 | `2 ** 3 = 8` |
| `==` | 等於 | `5 == 5` |
| `!=` | 不等於 | `5 != 3` |
| `>`, `<`, `>=`, `<=` | 比較 | `5 > 3` |
| `and`, `or`, `not` | 邏輯 | `True and False` |

---

## A.2 資料結構

### List（列表）

```python
# 建立
lst = [1, 2, 3]
lst = list(range(5))

# 訪問
lst[0]      # 第一個
lst[-1]     # 最後一個
lst[1:3]    # 切片

# 修改
lst.append(4)        # 末尾添加
lst.insert(0, 0)     # 插入
lst.remove(2)        # 刪除值
lst.pop()            # 刪除最後一個
lst[0] = 10          # 修改

# 操作
len(lst)             # 長度
sorted(lst)          # 排序（返回新列表）
lst.sort()           # 原地排序
lst.reverse()        # 反轉
sum(lst)             # 總和
max(lst)             # 最大值
min(lst)             # 最小值
lst.count(1)         # 計數
lst.index(2)         # 找索引
```

### Dictionary（字典）

```python
# 建立
d = {'a': 1, 'b': 2}
d = dict(a=1, b=2)

# 訪問
d['a']               # 取值
d.get('a', 0)        # 安全取值

# 修改
d['c'] = 3           # 添加/修改
del d['a']           # 刪除
d.pop('b')           # 刪除並返回

# 遍歷
d.keys()             # 所有鍵
d.values()           # 所有值
d.items()            # 鍵值對

for key, value in d.items():
    print(key, value)
```

### Set（集合）

```python
# 建立
s = {1, 2, 3}
s = set([1, 2, 2, 3])  # {1, 2, 3}

# 操作
s.add(4)             # 添加
s.remove(2)          # 刪除

# 集合運算
a | b                # 聯集
a & b                # 交集
a - b                # 差集
a ^ b                # 對稱差集
```

---

## A.3 字串方法

```python
s = "Hello World"

# 轉換
s.upper()            # "HELLO WORLD"
s.lower()            # "hello world"
s.capitalize()       # "Hello world"
s.title()            # "Hello World"

# 搜尋
s.find("World")      # 6
s.count("l")         # 3
s.startswith("He")   # True
s.endswith("ld")     # True

# 判斷
s.isalpha()          # False（有空格）
s.isdigit()          # False
s.isalnum()          # False

# 分割合併
s.split()            # ['Hello', 'World']
"-".join(['a','b'])  # "a-b"

# 去除空白
"  hi  ".strip()     # "hi"
"  hi  ".lstrip()    # "hi  "
"  hi  ".rstrip()    # "  hi"

# 替換
s.replace("World", "Python")  # "Hello Python"
```

---

## A.4 格式化字串

### f-string（推薦）

```python
name = "Alice"
age = 20

# 基本
f"Name: {name}, Age: {age}"

# 運算
f"Next year: {age + 1}"

# 格式化
f"{age:02d}"         # 補零：20
f"{3.14159:.2f}"     # 小數：3.14
f"{1000:,}"          # 千分位：1,000
f"{0.856:.1%}"       # 百分比：85.6%

# 對齊
f"{name:<10}"        # 靠左
f"{name:>10}"        # 靠右
f"{name:^10}"        # 置中
```

---

## A.5 控制流程

### 條件判斷

```python
if condition:
    pass
elif condition:
    pass
else:
    pass

# 三元運算
value = a if condition else b

# 多條件
if 0 < x < 100:
    pass
```

### 迴圈

```python
# for 迴圈
for i in range(10):
    pass

for item in items:
    pass

for i, item in enumerate(items):
    pass

# while 迴圈
while condition:
    pass

while True:
    if stop:
        break
    if skip:
        continue

# 迴圈 else
for item in items:
    if found(item):
        break
else:
    print("沒找到")
```

---

## A.6 函數

```python
# 基本定義
def func(arg):
    return result

# 預設參數
def func(arg, opt=default):
    pass

# 任意參數
def func(*args, **kwargs):
    pass

# Lambda
square = lambda x: x**2
```

---

## A.7 檔案操作

```python
# 讀取
with open('file.txt', 'r') as f:
    content = f.read()
    lines = f.readlines()
    for line in f:
        pass

# 寫入
with open('file.txt', 'w') as f:
    f.write("text")
    f.writelines(lines)

# 追加
with open('file.txt', 'a') as f:
    f.write("new line\n")
```

---

## A.8 常用內建函數

| 函數 | 說明 | 範例 |
|------|------|------|
| `len()` | 長度 | `len([1,2,3])` = 3 |
| `sum()` | 總和 | `sum([1,2,3])` = 6 |
| `max()` | 最大值 | `max([1,2,3])` = 3 |
| `min()` | 最小值 | `min([1,2,3])` = 1 |
| `abs()` | 絕對值 | `abs(-5)` = 5 |
| `round()` | 四捨五入 | `round(3.14, 1)` = 3.1 |
| `sorted()` | 排序 | `sorted([3,1,2])` |
| `reversed()` | 反轉 | `list(reversed([1,2,3]))` |
| `enumerate()` | 帶索引遍歷 | `enumerate(['a','b'])` |
| `zip()` | 配對 | `zip([1,2], ['a','b'])` |
| `map()` | 映射 | `map(str, [1,2,3])` |
| `filter()` | 過濾 | `filter(lambda x: x>0, lst)` |
| `range()` | 範圍 | `range(10)` |

---

## A.9 List Comprehension

```python
# 基本
[x for x in range(10)]

# 條件過濾
[x for x in range(10) if x % 2 == 0]

# 轉換
[x**2 for x in range(10)]

# 嵌套
[(x, y) for x in range(3) for y in range(3)]

# Dict comprehension
{x: x**2 for x in range(5)}

# Set comprehension
{x for x in [1, 2, 2, 3]}
```

---

## A.10 常用模組

### datetime

```python
import datetime

# 日期
today = datetime.date.today()
d = datetime.date(2026, 3, 7)

# 時間差
delta = datetime.timedelta(days=7)
new_date = today + delta

# 格式化
d.strftime("%Y-%m-%d")
```

### calendar

```python
import calendar

calendar.isleap(2024)        # 判斷閏年
calendar.weekday(2026, 3, 7) # 星期幾
```

### math

```python
import math

math.sqrt(16)      # 平方根
math.ceil(3.2)     # 無條件進位
math.floor(3.8)    # 無條件捨去
math.pi            # 圓周率
```

### random

```python
import random

random.randint(1, 10)        # 隨機整數
random.choice([1,2,3])       # 隨機選擇
random.shuffle(lst)          # 打亂列表
```

---

## A.11 例外處理

```python
try:
    risky_operation()
except ValueError as e:
    handle_value_error(e)
except Exception as e:
    handle_general_error(e)
else:
    success()
finally:
    cleanup()
```

---

## A.12 常見陷阱

### 可變預設參數

```python
# ❌ 錯誤
def append_to(element, lst=[]):
    lst.append(element)
    return lst

# ✅ 正確
def append_to(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst
```

### 列表複製

```python
# 淺複製（只複製引用）
lst2 = lst1
lst2[0] = 999  # lst1 也會改變

# 正確複製
lst2 = lst1.copy()
lst2 = lst1[:]
lst2 = list(lst1)
```

---

## A.13 效能技巧

```python
# ❌ 慢
result = ""
for x in items:
    result += str(x)

# ✅ 快
result = ''.join(str(x) for x in items)

# ❌ 慢
if x == 1 or x == 2 or x == 3:
    pass

# ✅ 快
if x in (1, 2, 3):
    pass
```

---

**返回：** [主目錄](./README.md)
**下一頁：** [附錄 B - 常見問題](./AppendixB-常見問題.md)
