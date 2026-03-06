# Chapter 05 - 數學運算與演算法

> 用 Python 實作演算法與數學問題

---

## 📋 本章目標

- 掌握數論基礎（因數、倍數、質數）
- 理解排序演算法原理
- 學習統計運算實作
- 精通進位制轉換
- 實作九九乘法表排序系統

---

## 5.1 基礎數論

### 5.1.1 因數與倍數

```python
# 判斷是否為因數
def is_factor(num, divisor):
    return num % divisor == 0

# 找出所有因數
def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

print(find_factors(12))  # [1, 2, 3, 4, 6, 12]

# 優化版本（只檢查到 √n）
def find_factors_fast(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:  # 避免重複（如 √16 = 4）
                factors.append(n // i)
    return sorted(factors)
```

### 5.1.2 最大公因數（GCD）

```python
# 輾轉相除法（歐幾里得演算法）
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # 6

# 使用內建函數
import math
print(math.gcd(48, 18))  # 6
```

**原理解析：**

```python
# GCD(48, 18)
# 48 = 18 × 2 + 12
# 18 = 12 × 1 + 6
# 12 = 6 × 2 + 0
# 答案：6
```

### 5.1.3 最小公倍數（LCM）

```python
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print(lcm(12, 18))  # 36

# Python 3.9+ 有內建 math.lcm()
import math
print(math.lcm(12, 18))  # 36
```

### 5.1.4 質數判斷

```python
# 基本版本
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 優化版本（只檢查到 √n）
def is_prime_fast(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# 找出範圍內的所有質數
def find_primes(n):
    return [x for x in range(2, n+1) if is_prime_fast(x)]

print(find_primes(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

---

## 5.2 實戰：公因數與公倍數

### 📝 題目

給定兩個數字 d1 和 d2，以及操作碼 O：

- O = 1：輸出小於 100 的所有共同因數
- O = 2：輸出小於 100 的所有共同倍數

### ✅ 解答

```python
# 讀取 10 組資料
for _ in range(10):
    data = input().split()
    O = int(data[0])
    d1 = int(data[1])
    d2 = int(data[2])

    if O == 1:  # 共同因數
        found = False
        for j in range(1, 100):
            if d1 % j == 0 and d2 % j == 0:
                print(j, end=" ")
                found = True
        if not found:
            print("None", end="")
        print()

    elif O == 2:  # 共同倍數
        found = False
        for j in range(1, 100):
            if j % d1 == 0 and j % d2 == 0:
                print(j, end=" ")
                found = True
        if not found:
            print("None", end="")
        print()
```

### 🔍 關鍵概念

```python
# 公因數：能同時整除兩個數
if d1 % j == 0 and d2 % j == 0

# 公倍數：能被兩個數同時整除
if j % d1 == 0 and j % d2 == 0

# 最大公因數：就是最大的公因數
gcd(d1, d2)

# 最小公倍數：就是最小的公倍數
lcm(d1, d2)
```

---

## 5.3 排序演算法

### 5.3.1 內建排序

```python
# 列表排序（改變原列表）
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# 排序函數（返回新列表）
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# 降序排序
numbers.sort(reverse=True)
sorted_numbers = sorted(numbers, reverse=True)
```

### 5.3.2 自訂排序鍵

```python
# 按絕對值排序
numbers = [-5, 2, -8, 3, -1]
numbers.sort(key=abs)
print(numbers)  # [-1, 2, 3, -5, -8]

# 按長度排序
words = ["apple", "pie", "zoo", "a"]
words.sort(key=len)
print(words)  # ['a', 'pie', 'zoo', 'apple']

# 多鍵排序（先按第一個元素，再按第二個）
pairs = [(2, 'b'), (1, 'c'), (2, 'a'), (1, 'b')]
pairs.sort()
print(pairs)  # [(1, 'b'), (1, 'c'), (2, 'a'), (2, 'b')]

# Lambda 排序
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 85)
]
students.sort(key=lambda x: (x[1], x[0]))  # 先按分數，再按姓名
```

### 5.3.3 穩定排序

Python 的排序是**穩定的**（相同鍵值保持原順序）：

```python
data = [
    ("Alice", 85),
    ("Bob", 85),
    ("Charlie", 90)
]

# 先按姓名排序
data.sort(key=lambda x: x[0])
# [('Alice', 85), ('Bob', 85), ('Charlie', 90)]

# 再按分數排序（穩定性保證 Alice 還在 Bob 前面）
data.sort(key=lambda x: x[1])
# [('Alice', 85), ('Bob', 85), ('Charlie', 90)]
```

---

## 5.4 實戰：九九乘法表排序

### 📝 題目

將九九乘法表按特殊規則排序：

1. **第一組：** M1 為奇數的公式（按 M1, M2 升序）
2. **第二組：** M1 為偶數且 M2 為奇數的公式
3. **第三組：** M1, M2 都是偶數的公式

輸出時每行顯示 9 個公式。

### 💡 範例

```
第一組（M1 奇數）：
1×1=1  1×2=2  1×3=3  ... 1×9=9
3×1=3  3×2=6  ...

第二組（M1 偶、M2 奇）：
2×1=2  2×3=6  2×5=10 ...

第三組（M1、M2 都偶）：
2×2=4  2×4=8  ...
```

### ✅ 解答

```python
# 生成所有九九乘法表公式
all_formulas = []
for m1 in range(1, 10):
    for m2 in range(1, 10):
        product = m1 * m2
        all_formulas.append((m1, m2, product))

# 分組並排序
# 第一組：M1 為奇數
group1 = [(m1, m2, p) for m1, m2, p in all_formulas if m1 % 2 == 1]
group1.sort(key=lambda x: (x[0], x[1]))

# 第二組：M1 為偶數且 M2 為奇數
group2 = [(m1, m2, p) for m1, m2, p in all_formulas if m1 % 2 == 0 and m2 % 2 == 1]
group2.sort(key=lambda x: (x[0], x[1]))

# 第三組：M1、M2 都是偶數
group3 = [(m1, m2, p) for m1, m2, p in all_formulas if m1 % 2 == 0 and m2 % 2 == 0]
group3.sort(key=lambda x: (x[0], x[1]))

# 合併所有公式
all_sorted = group1 + group2 + group3

# 輸出（每行 9 個）
formulas_per_row = 9
for i in range(0, len(all_sorted), formulas_per_row):
    row = all_sorted[i:i+formulas_per_row]
    formatted = [f"{m1} X {m2} = {p}" for m1, m2, p in row]
    print("\t".join(formatted))
```

### 🔍 關鍵技巧

```python
# 1. List Comprehension 過濾
group1 = [item for item in all_formulas if condition]

# 2. Lambda 多鍵排序
data.sort(key=lambda x: (x[0], x[1]))
# 先按 x[0]，相同時再按 x[1]

# 3. 列表切片
row = all_sorted[i:i+9]  # 取 9 個元素

# 4. 列表連接
all_sorted = list1 + list2 + list3
```

---

## 5.5 統計運算

### 5.5.1 基本統計量

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 平均值
mean = sum(numbers) / len(numbers)  # 5.5

# 中位數（需先排序）
sorted_nums = sorted(numbers)
n = len(sorted_nums)
if n % 2 == 1:  # 奇數個
    median = sorted_nums[n // 2]
else:  # 偶數個
    median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2

# 眾數（最常出現的數）
from collections import Counter
counter = Counter(numbers)
mode = counter.most_common(1)[0][0]

# 變異數
mean = sum(numbers) / len(numbers)
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

# 標準差
import math
std_dev = math.sqrt(variance)
```

### 5.5.2 實戰：中位數與變異數

```python
while True:
    data = list(map(int, input().split()))
    n = data[0]

    if n == 0:
        break

    numbers = data[1:]
    numbers.sort()  # 排序

    # 中位數（題目要求的是特定算法）
    if n % 2 == 1:  # 奇數
        median = numbers[(n + 1) // 2 - 1]
    else:  # 偶數
        median = numbers[n // 2 - 1]

    print(median, end=" ")

    # 變異數
    mean = sum(numbers) // n  # 整數平均
    variance = sum((x - mean) ** 2 for x in numbers) // n

    print(f"{variance}")
```

---

## 5.6 進位制轉換

### 5.6.1 十進位轉 N 進位

```python
def dec_to_base(num, base):
    """將十進位轉為 base 進位"""
    if num == 0:
        return "0"

    digits = []
    while num:
        digits.append(str(num % base))
        num //= base

    return ''.join(reversed(digits))

print(dec_to_base(10, 2))   # "1010"
print(dec_to_base(255, 16)) # "FF" (需處理 A-F)
```

### 5.6.2 N 進位轉十進位

```python
def base_to_dec(num_str, base):
    """將 base 進位轉為十進位"""
    result = 0
    for digit in num_str:
        result = result * base + int(digit)
    return result

print(base_to_dec("1010", 2))  # 10
print(base_to_dec("377", 8))   # 255
```

### 5.6.3 實戰：進位制表示

```python
while True:
    data = list(map(int, input().split()))
    n = data[0]
    b = data[1]

    # 驗證輸入
    if n < 0 or b < 2 or b > 10:
        break

    # 轉換
    if n == 0:
        print(0)
        continue

    result = 0
    multiplier = 1

    while n != 0:
        digit = n % b
        result = result + digit * multiplier
        multiplier *= 10
        n //= b

    print(result)
```

---

## 5.7 常見演算法模式

### 模式 1：計數器

```python
# 統計出現次數
from collections import Counter
counts = Counter([1, 2, 2, 3, 3, 3])
print(counts)  # Counter({3: 3, 2: 2, 1: 1})
```

### 模式 2：雙指標

```python
# 判斷回文
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

### 模式 3：滑動窗口

```python
# 找出所有長度為 k 的子陣列的最大值
def max_sliding_window(nums, k):
    result = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        result.append(max(window))
    return result
```

---

## 📝 本章總結

### 核心概念

1. **因數** - 能整除的數
2. **倍數** - 被整除的數
3. **GCD** - 最大公因數，用輾轉相除法
4. **LCM** - 最小公倍數，LCM = (a×b) / GCD
5. **Lambda 排序** - `key=lambda x: (x[0], x[1])`
6. **進位制轉換** - 不斷除法取餘數

### 必記演算法

| 演算法 | 時間複雜度 | 用途 |
|--------|-----------|------|
| 找因數（優化） | O(√n) | 數論 |
| GCD（輾轉相除） | O(log n) | 最大公因數 |
| 質數判斷 | O(√n) | 數論 |
| 排序（內建） | O(n log n) | 資料整理 |

---

## 🎯 練習題

1. 實作埃拉托斯特尼篩法（Sieve of Eratosthenes）
2. 找出 N 的所有質因數
3. 計算組合數 C(n, r)
4. 實作快速冪（Fast Exponentiation）
5. 找出陣列中的第 K 大元素

---

**上一章：** [Chapter 04 - 字串處理](./Chapter04-字串處理.md)
**下一章：** [Chapter 06 - 模組與函數](./Chapter06-模組與函數.md)
