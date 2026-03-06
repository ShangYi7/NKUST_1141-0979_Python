# Chapter 08 - 實戰專案解析

> 綜合應用所學知識解決實際問題

---

## 📋 本章目標

- 分析完整專案的需求與設計
- 學習問題拆解與模組化思維
- 掌握程式碼優化技巧
- 培養除錯與測試能力

---

## 8.1 專案 1：九九乘法表特殊排序

### 📝 需求分析

將九九乘法表（1×1 到 9×9）按以下規則排序並輸出：

**排序規則：**

1. **第一組：** M1 為奇數的公式（1×1, 1×2, ..., 9×9）
2. **第二組：** M1 為偶數但 M2 為奇數的公式（2×1, 2×3, ...）
3. **第三組：** M1、M2 都是偶數的公式（2×2, 2×4, ...）

每組內部按 M1 升序，M1 相同時按 M2 升序。

### 🎯 解題思路

```
步驟 1：生成所有 81 個公式
步驟 2：根據規則分成三組
步驟 3：每組內部排序
步驟 4：合併並格式化輸出
```

### ✅ 完整實作

```python
# Step 1: 生成所有公式
all_formulas = []
for m1 in range(1, 10):
    for m2 in range(1, 10):
        product = m1 * m2
        all_formulas.append((m1, m2, product))

# Step 2: 分組
# 第一組：M1 為奇數
group1 = [(m1, m2, p) for m1, m2, p in all_formulas if m1 % 2 == 1]

# 第二組：M1 為偶數且 M2 為奇數
group2 = [(m1, m2, p) for m1, m2, p in all_formulas
          if m1 % 2 == 0 and m2 % 2 == 1]

# 第三組：M1、M2 都是偶數
group3 = [(m1, m2, p) for m1, m2, p in all_formulas
          if m1 % 2 == 0 and m2 % 2 == 0]

# Step 3: 每組內部排序
group1.sort(key=lambda x: (x[0], x[1]))
group2.sort(key=lambda x: (x[0], x[1]))
group3.sort(key=lambda x: (x[0], x[1]))

# Step 4: 合併
all_sorted = group1 + group2 + group3

# 格式化輸出（每行 9 個）
formulas_per_row = 9
for i in range(0, len(all_sorted), formulas_per_row):
    row = all_sorted[i:i+formulas_per_row]
    formatted = [f"{m1} X {m2} = {p}" for m1, m2, p in row]
    print("\t".join(formatted))
```

### 🔍 關鍵技術點

**1. List Comprehension 過濾**

```python
# 條件過濾
group1 = [item for item in all_formulas if m1 % 2 == 1]

# 等同於
group1 = []
for item in all_formulas:
    m1, m2, p = item
    if m1 % 2 == 1:
        group1.append(item)
```

**2. Lambda 多鍵排序**

```python
# 先按 m1，再按 m2
data.sort(key=lambda x: (x[0], x[1]))

# 如果要降序
data.sort(key=lambda x: (x[0], -x[1]))  # m2 降序
```

**3. 列表切片批次處理**

```python
# 每次取 9 個
for i in range(0, len(data), 9):
    batch = data[i:i+9]
    process(batch)
```

---

## 8.2 專案 2：多人剪刀石頭布競賽

### 📝 需求分析

實作 N 局制猜拳遊戲（N 為正奇數），先贏 (N+1)/2 局者獲勝。

**規則：**

- Y = 剪刀，M = 石頭，O = 布
- 剪刀贏布，石頭贏剪刀，布贏石頭
- 平手不計分

### 🎯 解題思路

```
步驟 1：讀取並驗證 N（必須是正奇數）
步驟 2：計算獲勝所需局數 = (N+1)/2
步驟 3：逐局判斷勝負並計分
步驟 4：有人達到獲勝局數時結束
```

### ✅ 完整實作

```python
def judge_winner(p1, p2):
    """判斷一局的勝負
    返回：1（玩家1贏）、2（玩家2贏）、0（平手）
    """
    if p1 == p2:
        return 0

    # 玩家1贏的情況
    win_cases = [
        ("Y", "O"),  # 剪刀贏布
        ("M", "Y"),  # 石頭贏剪刀
        ("O", "M")   # 布贏石頭
    ]

    if (p1, p2) in win_cases:
        return 1
    else:
        return 2

def play_game(n):
    """進行一場 N 局制遊戲"""
    win_threshold = (n + 1) / 2
    win1, win2 = 0, 0

    while True:
        p1, p2 = input().split()

        # 判斷本局勝負
        result = judge_winner(p1, p2)

        if result == 1:
            win1 += 1
        elif result == 2:
            win2 += 1
        # result == 0 時不計分

        # 檢查是否有人獲勝
        if win1 >= win_threshold:
            return "The first person wins the game"
        elif win2 >= win_threshold:
            return "The second person wins the game"

# 主程式
while True:
    n = int(input())

    #驗證 N 是否為正奇數
    if n <= 0 or n % 2 == 0:
        break

    # 進行遊戲並輸出結果
    result = play_game(n)
    print(result)
```

### 🔍 設計亮點

**1. 函數封裝**

```python
# 將判斷邏輯獨立成函數
def judge_winner(p1, p2):
    # 清晰的邏輯
    pass

# 好處：
# - 可讀性高
# - 易於測試
# - 可重用
```

**2. 資料結構選擇**

```python
# 使用 tuple 列表表示勝利條件
win_cases = [("Y", "O"), ("M", "Y"), ("O", "M")]

# 使用 in 運算子檢查
if (p1, p2) in win_cases:
    return 1
```

---

## 8.3 專案 3：二維圖案生成器

### 📝 需求分析

給定層數 L 和三個符號，生成同心方框圖案。

**範例：** L=3, 符號=['A', 'B', 'C']

```
A A A A A
A B B B A
A B C B A
A B B B A
A A A A A
```

### 🎯 解題思路

```
觀察規律：
- 總大小：(2L-1) × (2L-1)
- 每個位置的符號由「到最近邊的距離」決定
- 距離為 0 → 最外層符號
- 距離為 1 → 第二層符號
- 以此類推
```

### ✅ 完整實作

```python
while True:
    L = int(input())
    if L <= 0:
        break

    tokens = input().split()  # [t[0], t[1], t[2]]
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

            # 選擇符號（循環使用三個符號）
            index = (L - 1 - layer) % 3
            token = tokens[index]

            print(token, end=" ")
        print()  # 換行
```

### 🔍 數學分析

**位置計算：**

```
對於 5×5 的矩陣（L=3）：
  0 1 2 3 4  (j)
0 0 0 0 0 0
1 0 1 1 1 0
2 0 1 2 1 0
3 0 1 1 1 0
4 0 0 0 0 0
(i)

每個位置的層數：
layer = min(i, j, size-1-i, size-1-j)
```

**符號選擇：**

```python
# L=3, layer範圍: 0, 1, 2
# 符號索引：(3-1-layer) % 3
layer=0 → index=(3-1-0)%3=2 → tokens[2]='C'
layer=1 → index=(3-1-1)%3=1 → tokens[1]='B'
layer=2 → index=(3-1-2)%3=0 → tokens[0]='A'
```

---

## 8.4 專案 4：日期與星期查詢系統

### 📝 需求分析

輸入日期和天數差，輸出：

1. 該日期是星期幾
2. N 天後/前的日期

### ✅ 完整實作與優化

```python
import calendar
import datetime

# 預定義常數
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

WEEKDAYS = [
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
]

def parse_date(date_str):
    """解析日期字串"""
    year = int(date_str[0:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])
    return year, month, day

def is_valid_date(year, month, day):
    """驗證日期有效性"""
    if month == 2 and day == 29 and not calendar.isleap(year):
        return False
    return True

def format_date(year, month, day):
    """格式化日期輸出"""
    return f"{MONTHS[month-1]} {day:02d}, {year}"

def process_date_query(date_str, n):
    """處理日期查詢"""
    year, month, day = parse_date(date_str)

    # 驗證日期
    if not is_valid_date(year, month, day):
        return None

    # 第一行：星期幾
    weekday = calendar.weekday(year, month, day)
    line1 = f"The day of the week on {format_date(year, month, day)} is {WEEKDAYS[weekday]}"

    # 第二行：N 天後/前
    current_date = datetime.date(year, month, day)
    new_date = current_date + datetime.timedelta(days=n)

    if n < 0:
        direction = "before"
        n = abs(n)
    else:
        direction = "after"

    line2 = f"The date {direction} {n} days is {format_date(new_date.year, new_date.month, new_date.day)}"

    return line1, line2

# 主程式
while True:
    data = input().split()
    date_str = data[0]
    n = int(data[1])

    result = process_date_query(date_str, n)

    if result is None:
        break

    print(result[0])
    print(result[1])
```

### 🔍 優化重點

1. **常數提取**：月份、星期名稱存為常數
2. **函數拆分**：每個函數單一職責
3. **錯誤處理**：驗證日期有效性
4. **格式化統一**：使用專門的格式化函數

---

## 8.5 專案 5：完整資料管理系統

### 📝 需求分析

實作支援以下功能的資料庫系統：

- CREATE：新增資料
- READ：查詢資料
- UPDATE：更新資料
- DELETE：刪除資料
- 持久化存儲（檔案）

### ✅ 物件導向設計

```python
class CustomerDatabase:
    """顧客資料庫管理系統"""

    def __init__(self, filename='data.txt'):
        self.filename = filename
        self.customers = {}
        self.load()

    def load(self):
        """從檔案載入資料"""
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) >= 4:
                        id, name, phone, address = parts[:4]
                        self.customers[id] = {
                            'name': name,
                            'phone': phone,
                            'address': address
                        }
        except FileNotFoundError:
            pass

    def save(self):
        """存回檔案"""
        with open(self.filename, 'w') as f:
            for id, info in self.customers.items():
                f.write(f"{id} {info['name']} {info['phone']} {info['address']}\n")

    def create(self, id, name, phone, address):
        """新增顧客"""
        if id in self.customers:
            return False, "Exist"
        self.customers[id] = {
            'name': name,
            'phone': phone,
            'address': address
        }
        self.save()
        return True, "Success"

    def read(self, id, field):
        """查詢顧客資料"""
        if id not in self.customers:
            return None, "None"

        fields = ['name', 'phone', 'address']
        if 0 <= field < len(fields):
            value = self.customers[id][fields[field]]
            return value, "Success"
        return None, "Invalid field"

    def update(self, id, field, value):
        """更新顧客資料"""
        if id not in self.customers:
            return False, "None"

        fields = ['name', 'phone', 'address']
        if 0 <= field < len(fields):
            self.customers[id][fields[field]] = value
            self.save()
            return True, "Success"
        return False, "Invalid field"

    def delete(self, id):
        """刪除顧客"""
        if id not in self.customers:
            return False, "None"
        del self.customers[id]
        self.save()
        return True, "Success"

# 主程式
def main():
    db = CustomerDatabase('input.txt')

    while True:
        command = input()
        parts = command.split()

        if not parts or parts[0] == '*':
            break

        if parts[0] == '@' and len(parts) >= 5:
            success, msg = db.create(parts[1], parts[2], parts[3], parts[4])
            if not success:
                print(msg)

        elif parts[0] == '#' and len(parts) >= 2:
            success, msg = db.delete(parts[1])
            if not success:
                print(msg)

        elif parts[0] == '!' and len(parts) >= 4:
            success, msg = db.update(parts[1], int(parts[2]), parts[3])
            if not success:
                print(msg)

        elif parts[0] == '$' and len(parts) >= 3:
            value, msg = db.read(parts[1], int(parts[2]))
            if value:
                print(value)
            else:
                print(msg)

if __name__ == '__main__':
    main()
```

### 🔍 設計模式

**1. 封裝（Encapsulation）**

```python
# 將資料和操作封裝在類別中
class CustomerDatabase:
    def __init__(self):
        self.customers = {}  # 私有資料
```

**2. 單一職責原則**

```python
# 每個方法只做一件事
def load(self):  # 只負責載入
def save(self):  # 只負責存儲
```

**3. 錯誤處理**

```python
# 統一的錯誤回傳格式
return success, message
```

---

## 8.6 專案開發最佳實踐

### 8.6.1 程式碼組織

```python
# 模組結構
project/
├── main.py          # 主程式
├── database.py      # 資料庫邏輯
├── utils.py         # 工具函數
└── config.py        # 設定檔
```

### 8.6.2 測試驅動開發

```python
# 先寫測試
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# 再寫實作
def add(a, b):
    return a + b
```

### 8.6.3 文件化

```python
def calculate_discount(price, discount_rate):
    """計算折扣後的價格

    Args:
        price (float): 原價
        discount_rate (float): 折扣率（0-1）

    Returns:
        float: 折扣後價格

    Examples:
        >>> calculate_discount(100, 0.2)
        80.0
    """
    return price * (1 - discount_rate)
```

---

## 📝 本章總結

### 專案開發流程

```
1. 需求分析 → 理解問題
2. 設計架構 → 拆解模組
3. 編寫程式碼 → 實作功能
4. 測試驗證 → 確保正確
5. 優化重構 → 提升品質
```

### 核心技能

| 技能 | 應用場景 |
|------|----------|
| 問題拆解 | 複雜專案分析 |
| 函數封裝 | 程式碼重用 |
| 資料結構選擇 | 效能優化 |
| 錯誤處理 | 程式穩定性 |

---

## 🎯 進階挑戰

1. 為資料庫系統加上搜尋功能
2. 實作圖形化使用者介面（GUI）
3. 加入密碼保護機制
4. 實作資料匯出為 CSV/JSON
5. 設計 API 介面讓其他程式使用

---

**上一章：** [Chapter 07 - 檔案操作](./Chapter07-檔案操作.md)
**下一章：** [附錄 A - 速查表](./AppendixA-速查表.md)
