# Chapter 04 - 字串處理

> 精通 Python 的字串操作與格式化

---

## 📋 本章目標

- 掌握字串的各種操作方法
- 精通 f-string 格式化
- 理解字元編碼
- 實作字母頻率分析器

---

## 4.1 字串基礎

### 4.1.1 建立字串

```python
# 單引號或雙引號
s1 = 'Hello'
s2 = "World"

# 多行字串
multi = """This is
a multi-line
string"""

# 原始字串（不轉義）
path = r"C:\Users\name\file.txt"  # 不需要雙反斜線

# 字串連接
greeting = "Hello" + " " + "World"
repeated = "Go! " * 3  # "Go! Go! Go! "
```

### 4.1.2 字串是不可變的

```python
s = "Hello"

# ❌ 不能修改
s[0] = 'h'  # TypeError

# ✅ 建立新字串
s = s.lower()  # "hello"
s = s.replace('h', 'H')  # "Hello"
```

---

## 4.2 字串方法

### 4.2.1 大小寫轉換

```python
text = "Hello World"

text.upper()      # "HELLO WORLD"
text.lower()      # "hello world"
text.capitalize() # "Hello world"（首字母大寫）
text.title()      # "Hello World"（每個單字首字母大寫）
text.swapcase()   # "hELLO wORLD"（大小寫互換）
```

### 4.2.2 搜尋與判斷

```python
s = "Python Programming"

# 搜尋子字串
s.find("Pro")        # 7（返回索引，找不到返回 -1）
s.index("Pro")       # 7（找不到會拋出 ValueError）
s.count("o")         # 2（出現次數）

# 判斷開頭結尾
s.startswith("Py")   # True
s.endswith("ing")    # True

# 判斷內容類型
"123".isdigit()      # True（全是數字）
"abc".isalpha()      # True（全是字母）
"abc123".isalnum()   # True（字母或數字）
"   ".isspace()      # True（全是空白）
```

### 4.2.3 分割與合併

```python
# 分割
sentence = "apple,banana,cherry"
fruits = sentence.split(",")  # ['apple', 'banana', 'cherry']

text = "Hello   World"
words = text.split()  # ['Hello', 'World']（預設按空白分割）

# 合併
items = ["apple", "banana", "cherry"]
result = ", ".join(items)  # "apple, banana, cherry"

# 分割成行
multi_line = "line1\nline2\nline3"
lines = multi_line.splitlines()  # ['line1', 'line2', 'line3']
```

### 4.2.4 去除空白

```python
s = "  Hello  "

s.strip()   # "Hello"（去除兩端空白）
s.lstrip()  # "Hello  "（去除左邊空白）
s.rstrip()  # "  Hello"（去除右邊空白）

# 去除指定字元
"###Hello###".strip('#')  # "Hello"
```

### 4.2.5 替換

```python
s = "Hello World"

s.replace("World", "Python")  # "Hello Python"
s.replace("l", "L")           # "HeLLo WorLd"（替換所有）
s.replace("l", "L", 1)        # "HeLlo World"（只替換1次）
```

---

## 4.3 字串格式化

### 4.3.1 f-string（推薦）

```python
name = "Alice"
age = 20
score = 95.5

# 基本用法
print(f"Name: {name}, Age: {age}")

# 表達式
print(f"Next year: {age + 1}")

# 呼叫函數
print(f"Upper: {name.upper()}")

# 多行 f-string
message = f"""
Student: {name}
Age: {age}
Score: {score}
"""
```

### 4.3.2 數字格式化

```python
num = 1234567
pi = 3.141592653589793

# 千分位
print(f"{num:,}")  # 1,234,567

# 小數位數
print(f"{pi:.2f}")  # 3.14
print(f"{pi:.4f}")  # 3.1416

# 補零
day = 5
print(f"{day:02d}")  # 05

# 百分比
ratio = 0.856
print(f"{ratio:.1%}")  # 85.6%

# 科學記號
large = 1234567890
print(f"{large:e}")  # 1.234568e+09
```

### 4.3.3 對齊與填充

```python
text = "Python"

# 對齊（總寬度 10）
print(f"{text:<10}")  # "Python    "（靠左）
print(f"{text:>10}")  # "    Python"（靠右）
print(f"{text:^10}")  # "  Python  "（置中）

# 填充字元
print(f"{text:*^10}")  # "**Python**"
print(f"{text:0>10}")  # "0000Python"

# 數字補零
num = 42
print(f"{num:05d}")  # "00042"
```

### 4.3.4 除錯模式（Python 3.8+）

```python
x = 10
y = 20

# = 符號會顯示變數名稱
print(f"{x=}")      # x=10
print(f"{y=}")      # y=20
print(f"{x + y=}")  # x + y=30
```

### 4.3.5 format() 方法

```python
# 位置參數
"{} + {} = {}".format(1, 2, 3)  # "1 + 2 = 3"

# 索引
"{0} {1} {0}".format("A", "B")  # "A B A"

# 命名參數
"{name} is {age} years old".format(name="Alice", age=20)

# 格式指定
"{:.2f}".format(3.14159)  # "3.14"
```

### 4.3.6 % 格式化（舊式）

```python
# 不推薦，但可能在舊程式碼中見到
name = "Alice"
age = 20

"%s is %d years old" % (name, age)  # "Alice is 20 years old"
"%.2f" % 3.14159  # "3.14"
```

---

## 4.4 字元與編碼

### 4.4.1 字元與 ASCII

```python
# 字元轉 ASCII 碼
ord('A')  # 65
ord('a')  # 97
ord('0')  # 48

# ASCII 碼轉字元
chr(65)   # 'A'
chr(97)   # 'a'
```

### 4.4.2 遍歷字串

```python
# 遍歷每個字元
for char in "Hello":
    print(char)

# 帶索引遍歷
for i, char in enumerate("Hello"):
    print(f"{i}: {char}")
```

### 4.4.3 字串與列表轉換

```python
# 字串轉列表
s = "Hello"
chars = list(s)  # ['H', 'e', 'l', 'l', 'o']

# 列表轉字串
chars = ['H', 'e', 'l', 'l', 'o']
s = ''.join(chars)  # "Hello"
```

---

## 4.5 實戰：字母統計與顯示

### 📝 題目

讀取 3 行文字，統計每個字母（區分大小寫）出現的次數，並用星號顯示。

**輸出格式：** 按 a-z, A-Z 順序，格式為 `字母 星號`

**範例：**

```
輸入：
Hello World
Python
AAA

輸出：
d * e * l *** o ** r * H * P * W * A ***
```

### ✅ 解答

```python
# 讀取 3 行輸入
for _ in range(3):
    text = input()

    # 統計字母出現次數
    counts = {}
    for ch in text:
        if ch.isalpha():  # 只統計字母
            counts[ch] = counts.get(ch, 0) + 1

    # 固定順序輸出：a-z, A-Z
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []

    for ch in letters:
        if ch in counts:
            stars = '*' * counts[ch]
            result.append(f"{ch} {stars}")

    print(' '.join(result))
```

### 🔍 程式碼解析

```python
# 1. 字典計數模式
counts = {}
for ch in text:
    if ch.isalpha():
        counts[ch] = counts.get(ch, 0) + 1

# counts.get(ch, 0) 的作用：
# - 如果 ch 在字典中，返回其值
# - 如果 ch 不在字典中，返回 0
# 然後 +1

# 2. 字串重複運算
'*' * 3  # '***'
'A' * 5  # 'AAAAA'

# 3. 按固定順序輸出
# 不使用 for ch in counts（順序不固定）
# 而是遍歷預定義的字母順序
```

---

## 4.6 實戰：字串模式生成

### 📝 題目

給定長度 L 和兩個字串 t1、t2，生成 L 行輸出：

- 第 1 行：t1 × 1 + t2 × (L-1)
- 第 2 行：t1 × 2 + t2 × (L-2)
- ...
- 第 L 行：t1 × L

**範例：**

```
輸入：5 A B

輸出：
ABBBB
AABBB
AAABB
AAAAB
AAAAA
```

### ✅ 解答

```python
# 讀取 N 組資料
n = int(input())

for _ in range(n):
    parts = input().split()
    L = int(parts[0])
    t1 = parts[1]
    t2 = parts[2]

    # 生成 L 行
    for i in range(1, L + 1):
        line = t1 * i + t2 * (L - i)
        print(line)
```

---

## 4.7 常見模式總結

### 模式 1：統計字元出現次數

```python
text = "hello"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1

# 或使用 Counter
from collections import Counter
counts = Counter(text)
```

### 模式 2：過濾字串

```python
# 保留字母
text = "Hello123World"
letters = ''.join(ch for ch in text if ch.isalpha())  # "HelloWorld"

# 保留數字
numbers = ''.join(ch for ch in text if ch.isdigit())  # "123"
```

### 模式 3：字串反轉

```python
s = "Hello"

# 方法 1：切片
reversed_s = s[::-1]  # "olleH"

# 方法 2：reversed
reversed_s = ''.join(reversed(s))  # "olleH"
```

### 模式 4：檢查回文

```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
```

---

## 4.8 效能考量

### 字串連接

```python
# ❌ 效率低（每次都創建新字串）
result = ""
for i in range(1000):
    result += str(i)

# ✅ 效率高（使用列表累積，最後合併）
parts = []
for i in range(1000):
    parts.append(str(i))
result = ''.join(parts)
```

### 字串格式化效能

```python
# 效能排序（快到慢）：
# 1. f-string（最快）
f"{x} {y}"

# 2. % 格式化
"%s %s" % (x, y)

# 3. format()
"{} {}".format(x, y)

# 4. + 連接（最慢）
str(x) + " " + str(y)
```

---

## 📝 本章總結

### 核心概念

1. **字串是不可變的** - 所有操作都返回新字串
2. **f-string 是最推薦的格式化方式** - 簡潔、高效、可讀
3. **字典計數** 是統計的常用模式
4. **join() 連接列表** 比 + 連接字串更高效

### 必記方法

| 方法 | 用途 | 範例 |
|------|------|------|
| `split()` | 分割字串 | `"a,b".split(',')` |
| `join()` | 合併列表 | `','.join(['a','b'])` |
| `strip()` | 去除空白 | `" hi ".strip()` |
| `replace()` | 替換 | `"hi".replace('i','o')` |
| `lower()`/`upper()` | 大小寫 | `"Hi".lower()` |
| `isalpha()`/`isdigit()` | 類型檢查 | `'a'.isalpha()` |

### f-string 速查

```python
f"{var}"           # 基本
f"{var:.2f}"       # 2位小數
f"{var:10}"        # 寬度10
f"{var:<10}"       # 靠左
f"{var:>10}"       # 靠右
f"{var:^10}"       # 置中
f"{var:02d}"       # 補零
f"{var:,}"         # 千分位
f"{var:.1%}"       # 百分比
```

---

## 🎯 練習題

1. 反轉字串（不使用切片）
2. 計算字串中母音字母的數量
3. 判斷兩個字串是否為變位詞（anagram）
4. 實作簡單的字串壓縮（aaabbc → a3b2c1）
5. 將駝峰命名轉為蛇形命名（camelCase → camel_case）

---

**上一章：** [Chapter 03 - 資料結構](./Chapter03-資料結構.md)
**下一章：** [Chapter 05 - 數學與演算法](./Chapter05-數學與演算法.md)
