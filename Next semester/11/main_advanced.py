import tkinter as tk
from tkinter import messagebox
import os

# ==========================================
# 1. 設定全域變數 (系統參數與狀態)
# ==========================================
data_file = "data.txt"    # 儲存學生資料的檔名
default_gender = "男"     # 預設選取的性別

data = []                 # 儲存從 txt 檔案讀取出來的所有學生資料 (二維陣列)
current_idx = 0           # 記錄目前畫面上顯示的是第幾筆資料 (0 代表第一筆)
entries = {}              # 用來集中管理畫面上的輸入框 (Entry)
gender_var = None         # 單選按鈕變數

# 標記目前是否處於「新增模式」
is_adding = False


# ==========================================
# 2. 主要功能邏輯 (載入、存檔與顯示)
# ==========================================
def load_data():
    """從 data.txt 讀取資料"""
    global data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, data_file)
    data = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 6:
                    data.append(parts)
    except FileNotFoundError:
        pass


def save_data():
    """將記憶體中的資料列即時寫入回 txt 檔案"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, data_file)
    
    with open(file_path, "w", encoding="utf-8") as f:
        for record in data:
            f.write(",".join(record) + "\n")


def show_record():
    """顯示指定索引位置的資料到畫面上"""
    global is_adding
    is_adding = False # 重置新增模式
    
    for e in entries.values():
        e.delete(0, tk.END)
        
    if not data:
        gender_var.set(default_gender)
        return
        
    record = data[current_idx]
    entries["學號"].insert(0, record[0])
    entries["姓名"].insert(0, record[1])
    gender_var.set(record[2])
    entries["系所"].insert(0, record[3])
    entries["地址"].insert(0, record[4])
    entries["電話"].insert(0, record[5])


# ==========================================
# 3. 增刪改查 (CRUD) 相關功能
# ==========================================
def prev_record():
    global current_idx
    if current_idx > 0 and data:
        current_idx -= 1
        show_record()


def next_record():
    global current_idx
    if current_idx < len(data) - 1 and data:
        current_idx += 1
        show_record()


def get_current_input():
    return [
        entries["學號"].get().strip(),
        entries["姓名"].get().strip(),
        gender_var.get(),
        entries["系所"].get().strip(),
        entries["地址"].get().strip(),
        entries["電話"].get().strip()
    ]


def update_record():
    global current_idx, is_adding
    
    new_record = get_current_input()
    if not new_record[0]:
        return
        
    if is_adding:
        # 進階版：檢查學號是否已經存在，防止重複新增
        for record in data:
            if record[0] == new_record[0]:
                messagebox.showerror("錯誤", "學號已存在！無法新增重複的學生。")
                return
                
        data.append(new_record)
        current_idx = len(data) - 1
        is_adding = False
    else:
        if not data: return
        data[current_idx] = new_record
        
    save_data()
    show_record()


def delete_record():
    global current_idx
    if not data: return
        
    del data[current_idx]
    
    if current_idx >= len(data) and current_idx > 0:
        current_idx -= 1
        
    save_data()
    show_record()


def add_record():
    global is_adding
    is_adding = True
    for e in entries.values():
        e.delete(0, tk.END)
    gender_var.set(default_gender)


def search_record():
    """
    【進階版新增功能】搜尋邏輯：
    比對所有資料中的學號，若找到則切換顯示該筆，找不到則跳出提示。
    """
    global current_idx
    
    target_id = entries["學號"].get().strip()
    if not target_id:
        messagebox.showwarning("警告", "請輸入要搜尋的學號！")
        return
        
    # 用 enumerate 同時取得索引 (i) 和資料 (record)
    for i, record in enumerate(data):
        if record[0] == target_id:
            current_idx = i
            show_record()
            return
            
    # 如果迴圈跑完都沒找到，跳出提示
    messagebox.showinfo("提示", "找不到此學號")


# ==========================================
# 4. 建立視窗與畫面配置 (GUI)
# ==========================================
root = tk.Tk()
root.title("學生資料表 (進階版：防呆與搜尋)")

gender_var = tk.StringVar(value=default_gender)

# -- 建立所有的輸入框與標籤 --
tk.Label(root, text="學號：").grid(row=0, column=0, padx=2, pady=2, sticky="e")
entries["學號"] = tk.Entry(root, width=25)
entries["學號"].grid(row=0, column=1, padx=2, pady=2, sticky="w")

tk.Label(root, text="姓名：").grid(row=1, column=0, padx=2, pady=2, sticky="e")
entries["姓名"] = tk.Entry(root, width=25)
entries["姓名"].grid(row=1, column=1, padx=2, pady=2, sticky="w")

gender_frame = tk.Frame(root)
gender_frame.grid(row=2, column=0, columnspan=2, pady=2)
tk.Radiobutton(gender_frame, text="男", variable=gender_var, value="男").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(gender_frame, text="女", variable=gender_var, value="女").pack(side=tk.LEFT, padx=10)

tk.Label(root, text="系所：").grid(row=3, column=0, padx=2, pady=2, sticky="e")
entries["系所"] = tk.Entry(root, width=25)
entries["系所"].grid(row=3, column=1, padx=2, pady=2, sticky="w")

tk.Label(root, text="地址：").grid(row=4, column=0, padx=2, pady=2, sticky="e")
entries["地址"] = tk.Entry(root, width=25)
entries["地址"].grid(row=4, column=1, padx=2, pady=2, sticky="w")

tk.Label(root, text="電話：").grid(row=5, column=0, padx=2, pady=2, sticky="e")
entries["電話"] = tk.Entry(root, width=25)
entries["電話"].grid(row=5, column=1, padx=2, pady=2, sticky="w")
        
# -- 建立下方的所有控制按鈕 --
btn_frame = tk.Frame(root)
btn_frame.grid(row=6, column=0, columnspan=2, pady=5)

tk.Button(btn_frame, text="<<", command=prev_record).pack(side=tk.LEFT, padx=2)
tk.Button(btn_frame, text="更新", command=update_record).pack(side=tk.LEFT, padx=2)
tk.Button(btn_frame, text="刪除", command=delete_record).pack(side=tk.LEFT, padx=2)
tk.Button(btn_frame, text="新增", command=add_record).pack(side=tk.LEFT, padx=2)
tk.Button(btn_frame, text="搜尋", command=search_record).pack(side=tk.LEFT, padx=2)
tk.Button(btn_frame, text=">>", command=next_record).pack(side=tk.LEFT, padx=2)


# ==========================================
# 5. 啟動程式前先準備資料
# ==========================================
load_data()
show_record()

root.mainloop()
