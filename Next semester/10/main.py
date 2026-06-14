import tkinter as tk
import os

# ==========================================
# 1. 設定全域變數 (系統參數與狀態)
# ==========================================
data_file = "data.txt"    # 儲存學生資料的檔名
default_gender = "男"     # 預設選取的性別

data = []                 # 儲存從 txt 檔案讀取出來的所有學生資料 (二維陣列)
current_idx = 0           # 記錄目前畫面上顯示的是第幾筆資料 (0 代表第一筆)
entries = {}              # 用來集中管理畫面上的輸入框 (Entry)，方便我們用名稱尋找它
gender_var = None         # 稍後用來綁定性別單選按鈕的變數


# ==========================================
# 2. 主要功能邏輯
# ==========================================
def load_data():
    """
    從 data.txt 讀取資料。
    如果檔案不存在，會先提供一筆預設的測試資料避免程式出錯。
    """
    global data
    
    # 取得目前這個 Python 檔案所在的絕對路徑目錄
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, data_file)
    
    try:
        # 開啟文字檔讀取，使用 utf-8 確保中文正常顯示
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                # 使用 split() 把逗號隔開的字串，變成一個陣列
                parts = line.strip().split(",")
                # 必須確保資料剛好有 6 個欄位，以防出現空行或格式損壞
                if len(parts) == 6:
                    data.append(parts)
    except FileNotFoundError:
        # 例外處理：檔案遺失時提供預設測試資料，避免系統直接崩潰
        data = [["1103301234", "王大明", "男", "電子系", "高雄市建工路10號", "3814526"]]


def show_record():
    """
    將目前索引 (current_idx) 所指向的資料更新至畫面上的各個輸入框中。
    """
    # 如果資料陣列是空的，就不做事
    if not data: 
        return
        
    # 取出目前這筆資料
    record = data[current_idx]
    
    # 更新學號輸入框 (必須先清空 delete，再插入 insert)
    entries["學號"].delete(0, tk.END)
    entries["學號"].insert(0, record[0])
    
    # 更新姓名
    entries["姓名"].delete(0, tk.END)
    entries["姓名"].insert(0, record[1])
    
    # 更新性別 (修改這個變數，畫面上的單選按鈕就會自動切換)
    gender_var.set(record[2])
    
    # 更新系所
    entries["系所"].delete(0, tk.END)
    entries["系所"].insert(0, record[3])
    
    # 更新地址
    entries["地址"].delete(0, tk.END)
    entries["地址"].insert(0, record[4])
    
    # 更新電話
    entries["電話"].delete(0, tk.END)
    entries["電話"].insert(0, record[5])


def prev_record():
    """
    切換至上一筆資料。
    """
    global current_idx
    # 確保目前的索引大於 0 (第一筆)，才能往回切換
    if current_idx > 0:
        current_idx -= 1
        show_record() # 重新顯示畫面


def next_record():
    """
    切換至下一筆資料。
    """
    global current_idx
    # 確保目前的索引沒有超過總長度，才能往下一筆切換
    if current_idx < len(data) - 1:
        current_idx += 1
        show_record() # 重新顯示畫面


# ==========================================
# 3. 建立視窗與畫面配置 (GUI)
# ==========================================
root = tk.Tk()
root.title("學生資料表 (檢視)")

# 必須在建立 root 視窗後，才能建立 StringVar
gender_var = tk.StringVar(value=default_gender)

# 為了排版整齊，我們統一使用 grid (網格排版)
# -- 學號欄位 --
tk.Label(root, text="學號：").grid(row=0, column=0, padx=2, pady=2, sticky="e")
entries["學號"] = tk.Entry(root, width=25)
entries["學號"].grid(row=0, column=1, padx=2, pady=2, sticky="w")

# -- 姓名欄位 --
tk.Label(root, text="姓名：").grid(row=1, column=0, padx=2, pady=2, sticky="e")
entries["姓名"] = tk.Entry(root, width=25)
entries["姓名"].grid(row=1, column=1, padx=2, pady=2, sticky="w")

# -- 性別欄位 (使用 Radiobutton 單選按鈕) --
gender_frame = tk.Frame(root)
# 橫跨兩個網格欄位 (columnspan=2)
gender_frame.grid(row=2, column=0, columnspan=2, pady=2)
# variable 綁定到同一個 gender_var，這就是讓它們互斥單選的關鍵
tk.Radiobutton(gender_frame, text="男", variable=gender_var, value="男").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(gender_frame, text="女", variable=gender_var, value="女").pack(side=tk.LEFT, padx=10)

# -- 系所欄位 --
tk.Label(root, text="系所：").grid(row=3, column=0, padx=2, pady=2, sticky="e")
entries["系所"] = tk.Entry(root, width=25)
entries["系所"].grid(row=3, column=1, padx=2, pady=2, sticky="w")

# -- 地址欄位 --
tk.Label(root, text="地址：").grid(row=4, column=0, padx=2, pady=2, sticky="e")
entries["地址"] = tk.Entry(root, width=25)
entries["地址"].grid(row=4, column=1, padx=2, pady=2, sticky="w")

# -- 電話欄位 --
tk.Label(root, text="電話：").grid(row=5, column=0, padx=2, pady=2, sticky="e")
entries["電話"] = tk.Entry(root, width=25)
entries["電話"].grid(row=5, column=1, padx=2, pady=2, sticky="w")

# -- 底部控制按鈕區 --
btn_frame = tk.Frame(root)
btn_frame.grid(row=6, column=0, columnspan=2, pady=5)

# 前一筆、下一筆按鈕，綁定對應的函式
tk.Button(btn_frame, text="前一筆", width=10, command=prev_record).pack(side=tk.LEFT, padx=2)
tk.Button(btn_frame, text="下一筆", width=10, command=next_record).pack(side=tk.LEFT, padx=2)


# ==========================================
# 4. 啟動程式前先載入資料
# ==========================================
load_data()
show_record() # 顯示第一筆資料

root.mainloop()
