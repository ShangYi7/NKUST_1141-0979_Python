# Chapter 07 - 檔案與例外處理

> 掌握檔案 I/O 與錯誤處理

---

## 📋 本章目標

- 學會檔案讀寫操作
- 理解 with 語句的優勢
- 掌握例外處理機制
- 實作檔案型資料庫系統

---

## 7.1 檔案讀取

### 7.1.1 基本讀取

```python
# 開啟檔案
f = open('file.txt', 'r')  # 'r' 代表讀取模式
content = f.read()          # 讀取全部內容
f.close()                   # 記得關閉檔案

# 讀取所有行（返回列表）
f = open('file.txt', 'r')
lines = f.readlines()       # ['line1\n', 'line2\n', ...]
f.close()

# 逐行讀取
f = open('file.txt', 'r')
for line in f:
    print(line.strip())     # strip() 去除換行符
f.close()
```

### 7.1.2 使用 with 語句（推薦）

```python
# 自動關閉檔案
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
# 離開 with 區塊後自動關閉檔案

# 逐行處理
with open('file.txt', 'r') as f:
    for line in f:
        process(line)
```

### 7.1.3 處理不存在的檔案

```python
# 方法 1：檢查檔案是否存在
import os

if os.path.exists('file.txt'):
    with open('file.txt', 'r') as f:
        content = f.read()
else:
    print("檔案不存在")

# 方法 2：例外處理
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("檔案不存在")
    content = ""
```

---

## 7.2 檔案寫入

### 7.2.1 寫入模式

```python
# 'w' 模式：覆寫（會清空原檔案）
with open('output.txt', 'w') as f:
    f.write("Hello\n")
    f.write("World\n")

# 'a' 模式：追加（不會清空原檔案）
with open('output.txt', 'a') as f:
    f.write("New line\n")

# 寫入多行
lines = ["line1\n", "line2\n", "line3\n"]
with open('output.txt', 'w') as f:
    f.writelines(lines)
```

### 7.2.2 檔案模式總覽

| 模式 | 說明 | 檔案不存在 | 檔案存在 |
|------|------|-----------|----------|
| `'r'` | 讀取 | 錯誤 | 讀取 |
| `'w'` | 寫入 | 建立 | 覆寫 |
| `'a'` | 追加 | 建立 | 追加 |
| `'r+'` | 讀寫 | 錯誤 | 讀寫 |
| `'w+'` | 讀寫 | 建立 | 覆寫 |
| `'a+'` | 讀寫 | 建立 | 追加 |

---

## 7.3 例外處理

### 7.3.1 try-except 基礎

```python
# 基本語法
try:
    # 可能發生錯誤的程式碼
    result = 10 / 0
except ZeroDivisionError:
    # 處理特定錯誤
    print("不能除以零")

# 捕捉多種例外
try:
    value = int(input())
    result = 10 / value
except ValueError:
    print("輸入不是數字")
except ZeroDivisionError:
    print("不能除以零")
```

### 7.3.2 完整語法

```python
try:
    # 嘗試執行
    risky_operation()
except SpecificError as e:
    # 處理特定錯誤
    print(f"錯誤：{e}")
except Exception as e:
    # 處理其他所有錯誤
    print(f"未知錯誤：{e}")
else:
    # 沒有發生錯誤時執行
    print("成功")
finally:
    # 無論如何都會執行
    cleanup()
```

### 7.3.3 常見例外類型

```python
# ValueError：值錯誤
int("abc")  # ValueError

# TypeError：類型錯誤
"hello" + 123  # TypeError

# IndexError：索引錯誤
lst = [1, 2, 3]
print(lst[10])  # IndexError

# KeyError：鍵錯誤
d = {'a': 1}
print(d['b'])  # KeyError

# FileNotFoundError：檔案不存在
open('nonexist.txt', 'r')  # FileNotFoundError

# ZeroDivisionError：除以零
10 / 0  # ZeroDivisionError
```

---

## 7.4 實戰：顧客資料管理系統

### 📝 題目

實作一個簡單的 CRUD 系統，資料存儲在 `input.txt`。

**資料格式：** `ID NAME PHONE ADDRESS`

**指令：**

- `@ ID NAME PHONE ADDRESS` - 新增
- `# ID` - 刪除
- `! ID FIELD VALUE` - 更新（FIELD: 0=NAME, 1=PHONE, 2=ADDRESS）
- `$ ID FIELD` - 查詢
- `*` - 結束

### ✅ 完整解答

```python
def load_data(filename):
    """從檔案載入資料"""
    customers = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 4:
                    id = parts[0]
                    customers[id] = [parts[1], parts[2], parts[3]]
    except FileNotFoundError:
        pass  # 檔案不存在時返回空字典
    return customers

def save_data(filename, customers):
    """將資料存回檔案"""
    with open(filename, 'w') as f:
        for id, info in customers.items():
            f.write(f"{id} {info[0]} {info[1]} {info[2]}\n")

def main():
    filename = 'input.txt'
    customers = load_data(filename)

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
                save_data(filename, customers)

        # 刪除顧客
        elif parts[0] ==  '#' and len(parts) >= 2:
            id = parts[1]
            if id in customers:
                del customers[id]
                save_data(filename, customers)
            else:
                print('None')

        # 更新顧客資料
        elif parts[0] == '!' and len(parts) >= 4:
            id = parts[1]
            field = int(parts[2])
            value = parts[3]
            if id in customers:
                if 0 <= field <= 2:
                    customers[id][field] = value
                    save_data(filename, customers)
            else:
                print('None')

        # 查詢顧客資料
        elif parts[0] == '$' and len(parts) >= 3:
            id = parts[1]
            field = int(parts[2])
            if id in customers:
                if 0 <= field <= 2:
                    print(customers[id][field])
            else:
                print('None')

if __name__ == '__main__':
    main()
```

### 🔍 設計要點

```python
# 1. 函數封裝
# 將讀寫操作封裝成函數，提高可維護性

# 2. 例外處理
try:
    with open('file.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    data = ""  # 檔案不存在時提供預設值

# 3. 字典作為快取
# 在記憶體中維護資料字典，只在需要時寫入檔案

# 4. 輸入驗證
if 0 <= field <= 2:  # 檢查欄位索引是否有效
    customers[id][field] = value
```

---

## 7.5 檔案路徑操作

### 7.5.1 os.path 模組

```python
import os

# 連接路徑
path = os.path.join('folder', 'subfolder', 'file.txt')
# Windows: folder\subfolder\file.txt
# Unix: folder/subfolder/file.txt

# 檢查路徑是否存在
os.path.exists('file.txt')

# 檢查是否為檔案/資料夾
os.path.isfile('file.txt')
os.path.isdir('folder')

# 取得檔案大小
os.path.getsize('file.txt')  # bytes

# 分割路徑
dir, file = os.path.split('/path/to/file.txt')
# dir: '/path/to', file: 'file.txt'

# 取得副檔名
name, ext = os.path.splitext('file.txt')
# name: 'file', ext: '.txt'
```

### 7.5.2 pathlib 模組（Python 3.4+）

```python
from pathlib import Path

# 建立 Path 物件
p = Path('folder/subfolder/file.txt')

# 檢查存在
p.exists()

# 讀寫檔案
content = p.read_text()  # 讀取文字
p.write_text("Hello")    # 寫入文字

# 遍歷資料夾
folder = Path('.')
for file in folder.glob('*.txt'):
    print(file)
```

---

## 7.6 CSV 與 JSON

### 7.6.1 CSV 檔案

```python
import csv

# 讀取 CSV
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # row 是列表

# 寫入 CSV
data = [
    ['Name', 'Age', 'Score'],
    ['Alice', 20, 85],
    ['Bob', 22, 90]
]

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 使用字典
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'], row['Age'])
```

### 7.6.2 JSON 檔案

```python
import json

# 寫入 JSON
data = {
    'name': 'Alice',
    'age': 20,
    'scores': [85, 90, 92]
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)  # indent 美化輸出

# 讀取 JSON
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data['name'])

# 轉換為 JSON 字串
json_str = json.dumps(data, ensure_ascii=False)  # 支援中文
data = json.loads(json_str)  # 從字串解析
```

---

## 7.7 最佳實踐

### 7.7.1 檔案操作 Checklist

```python
# ✅ 使用 with 語句
with open('file.txt', 'r') as f:
    content = f.read()

# ❌ 手動關閉（可能忘記）
f = open('file.txt', 'r')
content = f.read()
f.close()

# ✅ 處理例外
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    content = ""

# ✅ 明確指定編碼
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

### 7.7.2 效能考量

```python
# ❌ 多次開啟檔案
for i in range(1000):
    with open('log.txt', 'a') as f:
        f.write(f"Line {i}\n")

# ✅ 一次性寫入
lines = [f"Line {i}\n" for i in range(1000)]
with open('log.txt', 'a') as f:
    f.writelines(lines)
```

---

## 📝 本章總結

### 核心概念

1. **使用 with 語句**自動管理檔案
2. **'r'/'w'/'a' 模式**：讀取/覆寫/追加
3. **try-except**處理例外
4. **函數封裝**檔案操作邏輯

### 檔案操作速查

```python
# 讀取
with open('file.txt', 'r') as f:
    content = f.read()         # 全部
    lines = f.readlines()      # 列表
    for line in f:             # 逐行
        pass

# 寫入
with open('file.txt', 'w') as f:
    f.write("text")            # 寫入字串
    f.writelines(lines)        # 寫入列表

# 追加
with open('file.txt', 'a') as f:
    f.write("new line\n")
```

---

## 🎯 練習題

1. 實作日誌系統（記錄時間戳和訊息）
2. 實作簡單的文字編輯器
3. 統計檔案中的單字頻率
4. 合併多個文字檔案
5. 實作檔案備份工具

---

**上一章：** [Chapter 06 - 模組與函數](./Chapter06-模組與函數.md)
**下一章：** [Chapter 08 - 實戰專案解析](./Chapter08-實戰專案.md)
