# Chapter 03 - 資料結構

> 深入理解 Python 的核心資料結構

---

## 📋 本章目標

- 掌握 List（列表）的各種操作
- 理解 Tuple（元組）與不可變性
- 精通 Dictionary（字典）的應用
- 認識 Set（集合）與數學運算
- 實作資料管理系統

---

## 3.1 List（列表）

### 3.1.1 建立列表

```python
# 空列表
empty = []
also_empty = list()

# 有初始值的列表
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # 可以混合類型

# 使用 range 建立
nums = list(range(10))  # [0, 1, 2, ..., 9]

# List Comprehension（列表推導式）
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, ...]
evens = [x for x in range(20) if x % 2 == 0]  # [0, 2, 4, ...]
```

### 3.1.2 訪問元素

```python
fruits = ["apple", "banana", "cherry", "date"]

# 索引（從 0 開始）
print(fruits[0])   # apple
print(fruits[2])   # cherry

# 負索引（從後面數）
print(fruits[-1])  # date（最後一個）
print(fruits[-2])  # cherry（倒數第二個）

# 切片 [start:end:step]
print(fruits[1:3])  # ['banana', 'cherry']（不包含索引3）
print(fruits[:2])   # ['apple', 'banana']（從開頭到索引2）
print(fruits[2:])   # ['cherry', 'date']（從索引2到結尾）
print(fruits[::2])  # ['apple', 'cherry']（每隔一個）
print(fruits[::-1]) # ['date', 'cherry', 'banana', 'apple']（反轉）
```

### 3.1.3 修改列表

```python
numbers = [1, 2, 3, 4, 5]

# 修改單個元素
numbers[0] = 10  # [10, 2, 3, 4, 5]

# 添加元素
numbers.append(6)      # [10, 2, 3, 4, 5, 6]
numbers.insert(1, 15)  # [10, 15, 2, 3, 4, 5, 6]

# 擴展列表
numbers.extend([7, 8, 9])  # [10, 15, 2, 3, 4, 5, 6, 7, 8, 9]
# 或使用 +
numbers = numbers + [11, 12]

# 刪除元素
numbers.remove(15)  # 刪除第一個 15
del numbers[0]      # 刪除索引 0 的元素
popped = numbers.pop()  # 刪除並返回最後一個元素
```

### 3.1.4 列表排序

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort()：原地排序（修改原列表）
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)  # 降序
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted()：返回新列表（不修改原列表）
original = [3, 1, 4]
sorted_list = sorted(original)
print(original)     # [3, 1, 4]
print(sorted_list)  # [1, 3, 4]

# 自訂排序鍵
words = ["apple", "pie", "zoo", "a"]
words.sort(key=len)  # 按長度排序
print(words)  # ['a', 'pie', 'zoo', 'apple']
```

### 3.1.5 列表方法速查

```python
lst = [1, 2, 3, 2, 4]

lst.append(5)      # 末尾添加元素
lst.insert(1, 10)  # 在索引 1 插入 10
lst.remove(2)      # 刪除第一個 2
lst.pop()          # 刪除並返回最後一個
lst.pop(0)         # 刪除並返回索引 0
lst.clear()        # 清空列表
lst.count(2)       # 計算 2 出現的次數
lst.index(3)       # 返回 3 的索引
lst.reverse()      # 反轉列表
lst.copy()         # 淺複製
```

---

## 3.2 Tuple（元組）

### 3.2.1 不可變序列

```python
# 建立元組
point = (3, 4)
single = (5,)  # 單元素元組需要逗號
empty = ()

# 也可以省略括號
coords = 10, 20, 30

# 訪問元素（與列表相同）
print(point[0])  # 3
print(point[-1])  # 4

# ❌ 不能修改
point[0] = 5  # TypeError: 'tuple' object does not support item assignment
```

### 3.2.2 元組的用途

```python
# 1. 多重返回值
def get_student():
    return "Alice", 20, 85  # 返回元組

name, age, score = get_student()  # 解包

# 2. 當作字典的鍵（列表不行）
locations = {
    (0, 0): "起點",
    (10, 20): "終點"
}

# 3. 保護資料不被修改
DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
```

### 3.2.3 元組 vs 列表

| 特性 | Tuple | List |
|------|-------|------|
| 可變性 | 不可變 | 可變 |
| 語法 | `(1, 2, 3)` | `[1, 2, 3]` |
| 效能 | 較快 | 較慢 |
| 用途 | 固定資料、返回值 | 動態資料集合 |

---

## 3.3 Dictionary（字典）

### 3.3.1 建立字典

```python
# 空字典
empty = {}
also_empty = dict()

# 有初始值
student = {
    "name": "Alice",
    "age": 20,
    "score": 85
}

# 使用 dict()
person = dict(name="Bob", age=25)

# 從鍵值對列表
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)  # {'a': 1, 'b': 2}
```

### 3.3.2 訪問與修改

```python
student = {"name": "Alice", "age": 20}

# 訪問值
print(student["name"])  # Alice

# 安全訪問（不存在時返回 None 或預設值）
print(student.get("name"))      # Alice
print(student.get("grade"))     # None
print(student.get("grade", 0))  # 0（預設值）

# 修改值
student["age"] = 21

# 添加新鍵值對
student["grade"] = "A"

# 刪除
del student["grade"]
score = student.pop("score", 0)  # 刪除並返回，不存在時返回 0
```

### 3.3.3 遍歷字典

```python
scores = {"Alice": 90, "Bob": 85, "Charlie": 92}

# 遍歷鍵
for name in scores:
    print(name)

# 遍歷值
for score in scores.values():
    print(score)

# 遍歷鍵值對（推薦）
for name, score in scores.items():
    print(f"{name}: {score}")
```

### 3.3.4 字典方法速查

```python
d = {"a": 1, "b": 2}

d.keys()        # 所有鍵
d.values()      # 所有值
d.items()       # 所有鍵值對
d.get(key, default)  # 安全取值
d.pop(key)      # 刪除並返回值
d.update(other) # 更新字典
d.clear()       # 清空
```

### 3.3.5 實戰：字母計數

```python
# 統計字母出現次數
text = "hello world"
counts = {}

for char in text:
    if char.isalpha():  # 只計算字母
        counts[char] = counts.get(char, 0) + 1

print(counts)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```

---

## 3.4 Set（集合）

### 3.4.1 建立集合

```python
# 空集合（注意：{} 是空字典）
empty = set()

# 有初始值
numbers = {1, 2, 3, 4, 5}
letters = set("hello")  # {'h', 'e', 'l', 'o'}（自動去重）

# 從列表建立
lst = [1, 2, 2, 3, 3, 3]
unique = set(lst)  # {1, 2, 3}
```

### 3.4.2 集合操作

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 聯集
print(a | b)  # {1, 2, 3, 4, 5, 6}
print(a.union(b))

# 交集
print(a & b)  # {3, 4}
print(a.intersection(b))

# 差集
print(a - b)  # {1, 2}
print(a.difference(b))

# 對稱差集
print(a ^ b)  # {1, 2, 5, 6}
```

### 3.4.3 修改集合

```python
s = {1, 2, 3}

s.add(4)       # 添加元素
s.remove(2)    # 刪除元素（不存在會報錯）
s.discard(10)  # 刪除元素（不存在不報錯）
s.clear()      # 清空
```

---

## 3.5 實戰：顧客資料管理系統

### 📝 題目

實作一個簡單的 CRUD（增刪改查）系統，資料存儲在檔案中。

**指令：**

- `@ ID NAME PHONE ADDRESS`：新增顧客
- `# ID`：刪除顧客
- `! ID FIELD VALUE`：更新欄位（0=NAME, 1=PHONE, 2=ADDRESS）
- `$ ID FIELD`：查詢欄位
- `*`：結束

### ✅ 解答

```python
# 讀取檔案資料
customers = {}
try:
    with open('input.txt', 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 4:
                customers[parts[0]] = [parts[1], parts[2], parts[3]]
except:
    pass

def save_data():
    """將資料寫回檔案"""
    with open('input.txt', 'w') as f:
        for id, info in customers.items():
            f.write(f"{id} {info[0]} {info[1]} {info[2]}\n")

# 主程式
while True:
    command = input()
    parts = command.split()

    if len(parts) == 0:
        continue

    # 結束程式
    if parts[0] == '*':
        break

    # 新增顧客
    if parts[0] == '@' and len(parts) >= 5:
        id = parts[1]
        if id in customers:
            print('Exist')
        else:
            customers[id] = [parts[2], parts[3], parts[4]]
            save_data()

    # 刪除顧客
    elif parts[0] == '#' and len(parts) >= 2:
        id = parts[1]
        if id in customers:
            del customers[id]
            save_data()
        else:
            print('None')

    # 更新顧客資料
    elif parts[0] == '!' and len(parts) >= 4:
        id = parts[1]
        field = int(parts[2])
        value = parts[3]
        if id in customers:
            customers[id][field] = value
            save_data()
        else:
            print('None')

    # 查詢顧客資料
    elif parts[0] == '$' and len(parts) >= 3:
        id = parts[1]
        field = int(parts[2])
        if id in customers:
            print(customers[id][field])
        else:
            print('None')
```

---

## 📝 本章總結

### 資料結構選擇指南

| 需求 | 選擇 |
|------|------|
| 有序、可變 | List |
| 有序、不可變 | Tuple |
| 鍵值對應、快速查詢 | Dictionary |
| 唯一元素、集合運算 | Set |

### 效能考量

- List 查詢：O(n)，索引訪問：O(1)
- Dict 查詢：O(1) 平均
- Set 查詢：O(1) 平均

---

**上一章：** [Chapter 02 - 流程控制](./Chapter02-流程控制.md)
**下一章：** [Chapter 04 - 字串處理](./Chapter04-字串處理.md)
