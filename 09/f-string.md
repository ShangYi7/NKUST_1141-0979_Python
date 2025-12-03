# Python f-string 語法速查表

**f-string** (Formatted String Literals) 是 Python 3.6+ 引入的字串格式化方式，它**可讀性高**、**速度快**且**功能強大**。

## 1. 基礎用法

只要在字串引號前加上 `f` 或 `F`，即可在 `{}` 中直接填入變數。

```python
name = "Gemini"
age = 1

# 輸出: Hello, my name is Gemini.
print(f"Hello, my name is {name}.")

# 輸出: I am 1 year old.
print(f"I am {age} year old.")
```

## 2. 數字格式化 (常用)

透過冒號 `:` 後接格式代碼，可以控制數字的顯示方式（補零、小數位數等）。

### 整數補零與千分位
```python
number = 5
large_num = 1000000

# :02d => 補零至 2 位數 (常用於日期: 01, 05, 12)
print(f"Date: {number:02d}")  # 輸出: Date: 05

# :05d => 補零至 5 位數
print(f"ID: {number:05d}")    # 輸出: ID: 00005

# :, => 加入千分位逗號
print(f"Cost: {large_num:,}") # 輸出: Cost: 1,000,000
```

### 浮點數 (小數)
```python
pi = 3.1415926
percent = 0.856

# :.2f => 保留兩位小數 (四捨五入)
print(f"Pi: {pi:.2f}")        # 輸出: Pi: 3.14

# :.1% => 轉為百分比並保留一位小數
print(f"Rate: {percent:.1%}") # 輸出: Rate: 85.6%
```

## 3. 表達式與函數呼叫

大括號 `{}` 內不只能放變數，還可以直接寫程式碼。

```python
a = 10
b = 20
text = "hello"

# 數學運算
print(f"Total: {a + b}")      # 輸出: Total: 30

# 呼叫方法
print(f"Title: {text.upper()}") # 輸出: Title: HELLO
```

## 4. 文字對齊

可用於製作整齊的表格輸出。格式為 `:{填滿字元}{對齊方向}{寬度}`。
* `<` : 靠左
* `>` : 靠右
* `^` : 置中

```python
text = "Hi"

# 靠右對齊，寬度 10
print(f"|{text:>10}|")  # 輸出: |        Hi|

# 靠左對齊，寬度 10
print(f"|{text:<10}|")  # 輸出: |Hi        |

# 置中對齊，寬度 10，空白處用 - 填滿
print(f"|{text:-^10}|") # 輸出: |----Hi----|
```

## 5. 除錯模式 (Python 3.8+)

在變數後加上 `=`，可以同時印出「變數名稱」與「數值」，Debug 神器。

```python
user = "Alice"
score = 95

print(f"{user=}")   # 輸出: user='Alice'
print(f"{score=}")  # 輸出: score=95
print(f"{1+1=}")    # 輸出: 1+1=2
```

## 6. 綜合範例 (日期處理)

結合您的需求，這是將日期變數格式化輸出的最佳寫法：

```python
year = 2025
month = 12
date = 4
day_name = "Thursday"

# 使用 f-string 一行解決，包含 date 補零
print(f"The date is {month}-{date:02d}-{year}, which is a {day_name}.")
# 輸出: The date is 12-04-2025, which is a Thursday.
```