# 附錄 B - 常見問題與陷阱

> 避開新手常見錯誤，提升程式碼品質

---

## B.1 語法相關

### 問題 1：縮排錯誤

```python
# ❌ 錯誤：混用 tab 和空格
def func():
    print("Tab")      # 使用 Tab
    print("Space")  # 使用空格
# IndentationError: unexpected indent

# ✅ 正確：統一使用 4 個空格
def func():
    print("Line 1")
    print("Line 2")
```

**解決方案：**

- 設定編輯器將 Tab 轉為空格
- 使用 4 個空格作為縮排（PEP 8 規範）

### 問題 2：忘記冒號

```python
# ❌ 錯誤
if x > 0
    print("Positive")
# SyntaxError: invalid syntax

# ✅ 正確
if x > 0:
    print("Positive")
```

Python 的流程控制關鍵字後需要冒號：`if`、`for`、`while`、`def`、`class` 等。

### 問題 3：括號不匹配

```python
# ❌ 錯誤
result = ((1 + 2) * 3
print(result)
# SyntaxError: unexpected EOF

# ✅ 正確
result = ((1 + 2) * 3)
print(result)
```

**技巧：** 使用支援括號匹配的編輯器（如 VS Code、PyCharm）

---

## B.2 型別相關

### 問題 4：字串與數字相加

```python
# ❌ 錯誤
age = input()  # 輸入 "20"
next_year = age + 1
# TypeError: can only concatenate str (not "int") to str

# ✅ 正確
age = int(input())
next_year = age + 1
```

**記住：** `input()` 永遠回傳字串！

### 問題 5：除法類型混淆

```python
# Python 2 風格（錯誤）
result = 7 / 2  # 期望得到 3，但在 Python 3 會得到 3.5

# Python 3
7 / 2   # 3.5（總是浮點除法）
7 // 2  # 3（整數除法）

# 負數除法的差異
-7 // 2  # -4（向下取整）
# C/C++: -7 / 2 = -3（向零截斷）
```

### 問題 6：== vs is

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# == 比較值
a == b  # True（內容相同）

# is 比較身份（記憶體位址）
a is b  # False（不同物件）
a is c  # True（同一物件）

# 特例：小整數和字串會被快取
x = 256
y = 256
x is y  # True（Python 快取 -5 到 256）

x = 257
y = 257
x is y  # False（超出快取範圍）
```

**最佳實踐：**

- 比較值用 `==`
- `is` 只用於比較 `None`、`True`、`False`

```python
# ✅ 正確
if x is None:
    pass

# ❌ 不推薦
if x == None:
    pass
```

---

## B.3 資料結構陷阱

### 問題 7：列表複製陷阱

```python
# ❌ 危險：只複製引用
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4]（list1 也改變了！）

# ✅ 正確：真正複製
list2 = list1.copy()
list2 = list1[:]
list2 = list(list1)

# 深層複製（包含嵌套結構）
import copy
list2 = copy.deepcopy(list1)
```

### 問題 8：可變預設參數

```python
# ❌ 危險
def add_to_list(item, lst=[]):
    lst.append(item)
    return lst

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [1, 2]（預期 [2]，但得到 [1, 2]）

# ✅ 正確
def add_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

**原因：** 預設參數在函數定義時只計算一次，之後都使用同一個物件。

### 問題 9：字典遍歷時修改

```python
# ❌ 錯誤：遍歷時修改字典大小
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    if d[key] == 2:
        del d[key]
# RuntimeError: dictionary changed size during iteration

# ✅ 正確：使用列表副本
for key in list(d.keys()):
    if d[key] == 2:
        del d[key]

# 或使用字典推導式
d = {k: v for k, v in d.items() if v != 2}
```

---

## B.4 迴圈相關

### 問題 10：迴圈變數洩漏

```python
# 迴圈變數在迴圈結束後仍然存在
for i in range(5):
    pass

print(i)  # 4（i 仍然存在）

# 如果要避免，使用函數封裝
def loop():
    for i in range(5):
        pass
    # i 在這裡失效

loop()
# print(i)  # NameError
```

### 問題 11：無限迴圈

```python
# ❌ 忘記更新條件
i = 0
while i < 10:
    print(i)
    # 忘記 i += 1
    # 無限迴圈！

# ✅ 記得更新
i = 0
while i < 10:
    print(i)
    i += 1

# 或使用 for 迴圈（更安全）
for i in range(10):
    print(i)
```

### 問題 12：修改正在遍歷的列表

```python
# ❌ 危險
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # 會跳過元素！
print(numbers)  # [1, 3, 5]（預期正確，但僅是巧合）

# 測試會出問題的例子
numbers = [1, 2, 2, 3]
for num in numbers:
    if num == 2:
        numbers.remove(num)
print(numbers)  # [1, 2, 3]（應該是 [1, 3]）

# ✅ 正確：遍歷副本或使用列表推導式
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
```

---

## B.5 函數相關

### 問題 13：忘記 return

```python
# ❌ 沒有返回值
def add(a, b):
    result = a + b
    # 忘記 return

answer = add(3, 5)
print(answer)  # None

# ✅ 記得 return
def add(a, b):
    return a + b
```

### 問題 14：全域變數修改

```python
# ❌ 不會修改全域變數
count = 0

def increment():
    count = count + 1  # UnboundLocalError

increment()

# ✅ 使用 global（不推薦）
count = 0

def increment():
    global count
    count = count + 1

# ✅ 更好：返回新值
count = 0

def increment(n):
    return n + 1

count = increment(count)
```

---

## B.6 字串相關

### 問題 15：字串是不可變的

```python
# ❌ 不能修改字串
s = "Hello"
s[0] = 'h'  # TypeError

# ✅ 建立新字串
s = 'h' + s[1:]  # "hello"
s = s.replace('H', 'h')
```

### 問題 16：字串連接效率

```python
# ❌ 低效率
result = ""
for i in range(10000):
    result += str(i)

# ✅ 高效率
result = ''.join(str(i) for i in range(10000))

# 效能差異：O(n²) vs O(n)
```

---

## B.7 檔案操作

### 問題 17：忘記關閉檔案

```python
# ❌ 可能忘記關閉
f = open('file.txt', 'r')
content = f.read()
# 如果這裡發生錯誤，f.close() 不會執行
f.close()

# ✅ 使用 with（自動關閉）
with open('file.txt', 'r') as f:
    content = f.read()
# 自動關閉，即使發生錯誤
```

### 問題 18：編碼問題

```python
# ❌ 可能出現編碼錯誤
with open('file.txt', 'r') as f:
    content = f.read()
# UnicodeDecodeError（如果檔案不是 UTF-8）

# ✅ 明確指定編碼
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

---

## B.8 效能陷阱

### 問題 19：重複計算

```python
# ❌ 重複計算 len()
for i in range(len(items)):
    if i < len(items) - 1:  # 每次都計算 len()
        pass

# ✅ 預先計算
n = len(items)
for i in range(n):
    if i < n - 1:
        pass
```

### 問題 20：用 in 檢查列表

```python
# ❌ 慢（O(n)）
numbers = [1, 2, 3, 4, 5, ..., 10000]
if 5000 in numbers:  # 需要遍歷
    pass

# ✅ 快（O(1)）
numbers_set = set(numbers)
if 5000 in numbers_set:  # 直接查找
    pass
```

---

## B.9 邏輯錯誤

### 問題 21：浮點數比較

```python
# ❌ 直接比較浮點數
a = 0.1 + 0.2
if a == 0.3:  # False！（因為浮點精度）
    print("Equal")

print(a)  # 0.30000000000000004

# ✅ 使用容差比較
epsilon = 1e-10
if abs(a - 0.3) < epsilon:
    print("Equal")

# 或使用 math.isclose()
import math
if math.isclose(a, 0.3):
    print("Equal")
```

### 問題 22：邏輯運算優先順序

```python
# ❌ 可能不是你想要的
if x > 0 and x < 10 or x > 20:
    # x > 0 and x < 10 會先計算

# ✅ 使用括號明確化
if (x > 0 and x < 10) or x > 20:
    pass

# ✅ 或使用 Python 的鏈式比較
if 0 < x < 10 or x > 20:
    pass
```

---

## B.10 記憶體相關

### 問題 23：大型列表推導式

```python
# ❌ 占用大量記憶體
result = [x**2 for x in range(10000000)]  # 一次建立所有元素

# ✅ 使用生成器（惰性計算）
result = (x**2 for x in range(10000000))  # 需要時才計算
```

---

## B.11 偵錯技巧

### 技巧 1：使用 print 偵錯

```python
# f-string 的 = 功能
x = 10
y = 20
print(f"{x=}, {y=}, {x+y=}")
# 輸出：x=10, y=20, x+y=30
```

### 技巧 2：使用 assert

```python
def divide(a, b):
    assert b != 0, "除數不能為零"
    return a / b
```

### 技巧 3：使用 pdb 偵錯器

```python
import pdb

def buggy_function():
    x = 10
    pdb.set_trace()  # 暫停在這裡
    y = x * 2
    return y
```

---

## B.12 最佳實踐總結

### ✅ 該做的事

1. 使用 4 空格縮排
2. 使用 with 處理檔案
3. 使用 f-string 格式化
4. 使用列表推導式（適度）
5. 明確處理例外
6. 寫有意義的變數名
7. 添加適當註解
8. 使用 `if x is None:` 檢查 None

### ❌ 不該做的事

1. 混用 tab 和空格
2. 使用可變預設參數
3. 在遍歷時修改容器
4. 用 `==` 比較 None
5. 忘記關閉檔案
6. 忽略例外
7. 過度使用全域變數
8. 寫過長的函數（超過 50 行）

---

**返回：** [主目錄](./README.md)
**上一頁：** [附錄 A - 速查表](./AppendixA-速查表.md)
**下一頁：** [附錄 C - 學習資源](./AppendixC-學習資源.md)
