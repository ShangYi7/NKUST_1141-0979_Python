# Chapter 01 - 基礎語法與輸入輸出

> 如果你已經會其他程式語言，這章將幫助你快速掌握 Python 的特色與差異

---

## 📋 本章目標

- 理解 Python 與 C/C++/Java 的語法差異
- 掌握 Python 的輸入輸出技巧
- 熟悉型別系統與動態型別特性
- 學會處理常見的輸入格式

---

## 1.1 為什麼選擇 Python？

### Python vs 其他語言

```python
# Python - 簡潔直覺
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
```

```cpp
// C++ - 較繁瑣
vector<int> numbers = {1, 2, 3, 4, 5};
vector<int> squared;
for(int x : numbers) {
    squared.push_back(x * x);
}
```

```java
// Java - 冗長
ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
ArrayList<Integer> squared = new ArrayList<>();
for(Integer x : numbers) {
    squared.add(x * x);
}
```

### Python 的特點

| 特性 | 說明 | 優點 |
|------|------|------|
| **動態型別** | 不需宣告變數型別 | 開發速度快 |
| **自動記憶體管理** | 垃圾回收機制 | 不用擔心記憶體洩漏 |
| **豐富的標準庫** | "Batteries included" | 減少重複造輪子 |
| **簡潔的語法** | 用縮排取代大括號 | 程式碼可讀性高 |

---

## 1.2 基本輸入輸出

### 1.2.1 輸出：print()

Python 的 `print()` 比其他語言更靈活：

```python
# 基本用法
print("Hello, World!")

# 多個參數（自動用空格分隔）
name = "Alice"
age = 20
print("Name:", name, "Age:", age)  # Name: Alice Age: 20

# 自訂分隔符
print("A", "B", "C", sep="-")  # A-B-C

# 自訂結尾（預設是換行 \n）
print("Hello", end="")
print("World")  # HelloWorld

# 不換行輸出（常用於同行輸出）
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()  # 最後換行
```

### 1.2.2 輸入：input()

`input()` 永遠回傳**字串**，這點要特別注意：

```python
# 基本輸入（回傳字串）
name = input()  # 讀取一行
print(type(name))  # <class 'str'>

# 帶提示訊息
age = input("請輸入年齡：")

# ⚠️ 常見錯誤：忘記轉換型別
x = input()  # 假設使用者輸入 "5"
y = x + 3    # ❌ TypeError: can only concatenate str to str

# ✅ 正確做法：轉換型別
x = int(input())  # 將字串轉為整數
y = x + 3         # ✅ 正確

# 浮點數輸入
price = float(input())
```

### 1.2.3 處理多個輸入

#### 方法 1：split() 分割字串

```python
# 輸入：10 20 30
data = input().split()  # ['10', '20', '30'] (字串列表)
print(data[0])  # '10'

# 轉換為整數列表
numbers = list(map(int, input().split()))  # [10, 20, 30]
```

**詳細解析：**

```python
# 假設輸入：10 20 30

# 步驟 1：讀取輸入
line = input()  # "10 20 30"

# 步驟 2：分割字串
parts = line.split()  # ['10', '20', '30']

# 步驟 3：map 函數將每個元素轉為 int
map_object = map(int, parts)  # map object

# 步驟 4：轉為列表
numbers = list(map_object)  # [10, 20, 30]

# 合併寫法（常見）
numbers = list(map(int, input().split()))
```

#### 方法 2：解包賦值

```python
# 輸入：10 20 30
a, b, c = map(int, input().split())
print(a)  # 10
print(b)  # 20
print(c)  # 30

# ⚠️ 注意：數量要對應
x, y = map(int, input().split())  # 若輸入 3 個數字會出錯
```

#### 方法 3：處理不定數量輸入

```python
# 第一個數字是數量
# 輸入：5 10 20 30 40 50
data = list(map(int, input().split()))
n = data[0]      # 5
numbers = data[1:]  # [10, 20, 30, 40, 50]

# 或更 Pythonic 的寫法
line = list(map(int, input().split()))
n, *numbers = line  # n=5, numbers=[10,20,30,40,50]
```

---

## 1.3 資料型別

### 1.3.1 基本型別

```python
# 整數 (int) - 無限精度
x = 100
big_num = 123456789012345678901234567890  # Python 可處理任意大小整數

# 浮點數 (float)
pi = 3.14159
scientific = 1.5e-10  # 科學記號

# 字串 (str)
name = "Alice"
message = 'Hello'
multi_line = """This is
a multi-line
string"""

# 布林值 (bool)
is_valid = True
is_empty = False
```

### 1.3.2 型別檢查與轉換

```python
# 檢查型別
x = 10
print(type(x))  # <class 'int'>

# 型別轉換 (Type Casting)
s = "123"
n = int(s)      # 123
f = float(s)    # 123.0
b = bool(s)     # True (非空字串為 True)

# 轉回字串
num = 42
text = str(num)  # "42"

# ⚠️ 轉換失敗會拋出例外
int("abc")  # ValueError: invalid literal for int()
```

### 1.3.3 型別檢查函數

```python
# isinstance() - 檢查是否為某型別
x = 10
print(isinstance(x, int))   # True
print(isinstance(x, str))   # False
print(isinstance(x, (int, float)))  # True (其中之一即可)
```

---

## 1.4 運算子

### 1.4.1 算術運算子

```python
a = 10
b = 3

print(a + b)   # 13  加法
print(a - b)   # 7   減法
print(a * b)   # 30  乘法
print(a / b)   # 3.333... 浮點數除法
print(a // b)  # 3   整數除法（無條件捨去）
print(a % b)   # 1   取餘數
print(a ** b)  # 1000 次方（10³）
```

**與 C/C++ 的重要差異：**

```python
# Python
7 / 2    # 3.5  (浮點數除法)
7 // 2   # 3    (整數除法)
-7 // 2  # -4   (向下取整，不是截斷)

# C/C++
7 / 2    // 3    (整數除法，因為兩個都是 int)
7.0 / 2  // 3.5  (浮點數除法)
-7 / 2   // -3   (截斷，不是向下取整)
```

### 1.4.2 比較運算子

```python
# 標準比較
5 == 5   # True  等於
5 != 3   # True  不等於
5 > 3    # True  大於
5 >= 5   # True  大於等於
5 < 10   # True  小於
5 <= 5   # True  小於等於

# Python 特色：連鎖比較
x = 5
1 < x < 10  # True (相當於 1 < x and x < 10)

# 等同於 C/C++ 的寫法
(1 < x) and (x < 10)
```

### 1.4.3 邏輯運算子

```python
# and, or, not (不是 &&, ||, !)
True and False  # False
True or False   # True
not True        # False

# 短路求值 (Short-circuit evaluation)
False and expensive_function()  # expensive_function() 不會執行
True or expensive_function()    # expensive_function() 不會執行
```

---

## 1.5 實戰：輸入處理模式

### 模式 1：單行單個數字

```python
# 輸入：42
n = int(input())
```

### 模式 2：單行多個數字（固定數量）

```python
# 輸入：10 20 30
a, b, c = map(int, input().split())
```

### 模式 3：單行多個數字（不定數量）

```python
# 輸入：5 10 20 30 40 50
numbers = list(map(int, input().split()))
n = numbers[0]      # 第一個是數量
data = numbers[1:]  # 剩下的是資料
```

### 模式 4：多行輸入（固定行數）

```python
# 輸入 3 行資料
for i in range(3):
    x = int(input())
    # 處理 x
```

### 模式 5：多行輸入（直到特定條件）

```python
# 持續讀取直到輸入 0
while True:
    n = int(input())
    if n == 0:
        break
    # 處理 n
```

### 模式 6：讀取整行資料（包含空格）

```python
# 輸入：Hello World
line = input()  # "Hello World" (保留空格)

# 若要分割
words = line.split()  # ['Hello', 'World']
```

---

## 1.6 實戰練習：溫度轉換器

### 📝 題目

撰寫程式將攝氏溫度轉換為華氏溫度。

**公式：** $F = \frac{9C}{5} + 32$

**輸入：** 一個浮點數（攝氏溫度）
**輸出：** 對應的華氏溫度

### 💡 範例

```
輸入：0
輸出：32.0

輸入：100
輸出：212.0

輸入：37
輸出：98.6
```

### ✅ 解答

```python
# 讀取攝氏溫度
celsius = float(input())

# 轉換為華氏
fahrenheit = (celsius * 9) / 5 + 32

# 輸出結果
print(fahrenheit)
```

### 🔍 程式碼解析

```python
celsius = float(input())  # 使用 float() 因為溫度可能是小數

# 運算順序：
# 1. celsius * 9
# 2. 結果 / 5
# 3. 結果 + 32

fahrenheit = (celsius * 9) / 5 + 32

# 或更明確的寫法
fahrenheit = ((celsius * 9) / 5) + 32

# 也可以用一行
print((float(input()) * 9) / 5 + 32)
```

### 🎯 進階挑戰

1. **雙向轉換：** 讓使用者選擇轉換方向
2. **批次處理：** 一次轉換多個溫度
3. **格式化輸出：** 限制小數位數

```python
# 挑戰 3：格式化輸出
celsius = float(input())
fahrenheit = (celsius * 9) / 5 + 32
print(f"{fahrenheit:.1f}")  # 保留 1 位小數
```

---

## 1.7 常見陷阱與最佳實踐

### ⚠️ 陷阱 1：忘記型別轉換

```python
# ❌ 錯誤
x = input()  # "5"
y = x + 3    # TypeError

# ✅ 正確
x = int(input())
y = x + 3
```

### ⚠️ 陷阱 2：整數除法與浮點除法混淆

```python
# Python 3
7 / 2    # 3.5 (總是浮點數)
7 // 2   # 3   (整數除法)

# 計算平均值
total = 10
count = 3
avg = total / count      # 3.333... (正確)
avg_wrong = total // count  # 3 (錯誤：會遺失小數)
```

### ⚠️ 陷阱 3：input() 會包含換行符嗎？

```python
# input() 會自動去除結尾的換行符
line = input()  # 使用者輸入 "hello\n"
print(repr(line))  # 'hello' (沒有 \n)

# 若需要讀取包含換行的原始輸入，使用 sys.stdin
import sys
line = sys.stdin.readline()  # 保留換行符
```

### ✅ 最佳實踐 1：使用有意義的變數名

```python
# ❌ 不好
a = int(input())
b = int(input())
c = a + b

# ✅ 好
width = int(input())
height = int(input())
area = width * height
```

### ✅ 最佳實踐 2：適當的註解

```python
# 計算圓形面積
radius = float(input())  # 半徑
PI = 3.14159
area = PI * radius ** 2  # A = πr²
print(area)
```

### ✅ 最佳實踐 3：錯誤處理

```python
# 基本版本（會直接崩潰）
n = int(input())

# 安全版本（處理錯誤輸入）
try:
    n = int(input())
except ValueError:
    print("請輸入有效的數字")
    n = 0
```

---

## 1.8 Python 獨有特性速覽

這些特性在後續章節會詳細介紹，這裡先有個印象：

### 多重賦值

```python
# 同時賦值多個變數
a, b, c = 1, 2, 3

# 交換變數（不需要暫存變數！）
a, b = b, a
```

### 串接比較

```python
# Python 可以這樣寫
if 0 < x < 100:
    print("x 在 0 到 100 之間")

# 其他語言要寫
if (x > 0) and (x < 100):
    pass
```

### 萬用字元 _

```python
# 忽略不需要的值
a, _, c = 1, 2, 3  # 不關心第二個值

# 迴圈中表示"我不在乎這個變數"
for _ in range(5):
    print("Hello")
```

---

## 📝 本章總結

### 核心概念

1. **Python 使用縮排**取代大括號定義程式區塊
2. **input() 永遠回傳字串**，需要自行轉換型別
3. **`/` 是浮點除法，`//` 是整數除法**
4. **動態型別**：變數不需宣告型別，但要注意隱式轉換

### 必記函數

| 函數 | 用途 | 範例 |
|------|------|------|
| `input()` | 讀取輸入 | `input()` |
| `print()` | 輸出 | `print("Hello")` |
| `int()` | 轉整數 | `int("123")` |
| `float()` | 轉浮點數 | `float("3.14")` |
| `str()` | 轉字串 | `str(42)` |
| `type()` | 取得型別 | `type(x)` |
| `map()` | 映射函數 | `map(int, ["1","2"])` |

### 輸入處理速查

```python
# 單個數字
n = int(input())

# 多個數字（固定）
a, b, c = map(int, input().split())

# 多個數字（列表）
numbers = list(map(int, input().split()))

# 字串（不分割）
text = input()
```

---

## 🎯 練習題

### 基礎題

1. 讀取兩個整數，輸出它們的和
2. 讀取一個數字，判斷是否為偶數
3. 讀取姓名與年齡，輸出 "姓名 今年 年齡 歲"

### 進階題

1. 讀取三個數字，輸出最大值（不使用 max 函數）
2. 讀取一行數字，計算平均值
3. 讀取 N，輸出 1 到 N 的總和

### 挑戰題

1. 設計一個通用的單位轉換器（長度、重量、溫度）
2. 實作簡單的計算機（支援 +、-、*、/）

---

## 📚 延伸閱讀

- [Python 官方教學](https://docs.python.org/zh-tw/3/tutorial/index.html)
- [PEP 20 - The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)

---

**下一章：** [Chapter 02 - 流程控制與迴圈](./Chapter02-流程控制.md)
