import tkinter as tk
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

# 用於標記目前是否處於「準備新增一筆全新資料」的狀態
# 若為 True，則在點擊更新按鈕時，會將表單內容作為新資料附加至陣列尾端，而非覆蓋現有資料
is_adding = False


# ==========================================
# 2. 主要功能邏輯 (載入、存檔與顯示)
# ==========================================
def load_data():
    """
    從 data.txt 讀取資料並存入二維陣列 data 中。
    """
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
    """
    將記憶體中的資料列即時覆寫寫入回 txt 檔案。
    此為所有增刪改操作的最後一步，以確保檔案維持最新狀態。
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, data_file)
    
    with open(file_path, "w", encoding="utf-8") as f:
        for record in data:
            # 將陣列元素用逗號合併回字串，並加上換行符號
            f.write(",".join(record) + "\n")


def show_record():
    """
    顯示指定索引位置的資料到畫面上。
    """
    global is_adding
    # 同時會自動重置「新增模式」狀態，避免使用者切換資料後誤把原本的覆蓋動作變成新增
    is_adding = False
    
    # 清除目前畫面上所有輸入框舊有內容
    for e in entries.values():
        e.delete(0, tk.END)
        
    # 若資料表為空，則留空畫面並結束函式
    if not data:
        gender_var.set(default_gender)
        return
        
    # 依序填入欄位值
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
    """切換上一筆"""
    global current_idx
    if current_idx > 0 and data:
        current_idx -= 1
        show_record()


def next_record():
    """切換下一筆"""
    global current_idx
    if current_idx < len(data) - 1 and data:
        current_idx += 1
        show_record()


def get_current_input():
    """
    輔助函式：統整收集目前畫面上所有的 Entry 及 Radiobutton 數值，並組成陣列回傳。
    """
    return [
        entries["學號"].get().strip(),
        entries["姓名"].get().strip(),
        gender_var.get(),
        entries["系所"].get().strip(),
        entries["地址"].get().strip(),
        entries["電話"].get().strip()
    ]


def update_record():
    """
    「更新」按鈕邏輯。
    """
    global current_idx, is_adding
    
    new_record = get_current_input()
    
    # 基礎欄位驗證：至少需輸入學號
    if not new_record[0]:
        return
        
    if is_adding:
        # 新增邏輯：加入陣列尾端，並將索引切換至該筆最新資料
        data.append(new_record)
        current_idx = len(data) - 1
        is_adding = False
    else:
        # 覆蓋舊資料邏輯
        if not data: 
            return
        data[current_idx] = new_record
        
    # 同步更新至檔案，並重整介面顯示
    save_data()
    show_record()


def delete_record():
    """
    「刪除」按鈕邏輯。
    """
    global current_idx
    if not data: 
        return
        
    # 從陣列中刪除這筆資料
    del data[current_idx]
    
    # 若刪除了最後一筆資料，將索引往後退一格以防止陣列出界
    if current_idx >= len(data) and current_idx > 0:
        current_idx -= 1
        
    # 存檔並重整畫面
    save_data()
    show_record()


def add_record():
    """
    「新增」按鈕邏輯。
    本身不會將資料寫入檔案，僅負責將介面清空，並設定 is_adding 旗標。
    待使用者輸入完畢按下「更新」時才會正式儲存。
    """
    global is_adding
    is_adding = True
    
    # 清空所有輸入框
    for e in entries.values():
        e.delete(0, tk.END)
    # 恢復預設性別
    gender_var.set(default_gender)


# ==========================================
# 4. 建立視窗與畫面配置 (GUI)
# ==========================================
root = tk.Tk()
root.title("學生資料表 (CRUD 基礎版)")

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
tk.Button(btn_frame, text=">>", command=next_record).pack(side=tk.LEFT, padx=2)


# ==========================================
# 5. 啟動程式前先準備資料
# ==========================================
load_data()
show_record()

root.mainloop()
