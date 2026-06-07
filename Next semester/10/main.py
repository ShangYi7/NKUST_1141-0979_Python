import tkinter as tk

class DataApp:
    """
    學生資料表檢視應用程式。
    負責讀取 data.txt 並以表單的形式呈現各項欄位，可透過上下筆按鈕切換資料。
    """
    def __init__(self, root):
        self.root = root
        self.root.title("tk")
        
        # ==========================================
        # ⬇️⬇️⬇️ 遊戲參數設定區 (可隨意修改) ⬇️⬇️⬇️
        # ==========================================
        self.data_file = "data.txt"    # 儲存學生資料的檔名
        self.default_gender = "男"     # 預設選取的性別
        # ==========================================
        # ⬆️⬆️⬆️ 遊戲參數設定區 (可隨意修改) ⬆️⬆️⬆️
        # ==========================================
        
        self.data = []
        self.current_idx = 0
        # 啟動時立刻載入外部的 txt 資料
        self.load_data()
        
        # 使用字典儲存各個 Entry 元件，方便後續透過欄位名稱來進行更新或取值
        self.entries = {}
        
        # 建立 UI 版面配置，統一使用 grid 進行對齊，達成表單的視覺效果
        # -- 學號欄位 --
        tk.Label(root, text="學號：").grid(row=0, column=0, padx=2, pady=2, sticky="e")
        self.entries["學號"] = tk.Entry(root, width=25)
        self.entries["學號"].grid(row=0, column=1, padx=2, pady=2, sticky="w")
        
        # -- 姓名欄位 --
        tk.Label(root, text="姓名：").grid(row=1, column=0, padx=2, pady=2, sticky="e")
        self.entries["姓名"] = tk.Entry(root, width=25)
        self.entries["姓名"].grid(row=1, column=1, padx=2, pady=2, sticky="w")
        
        # -- 性別欄位 (使用 Radiobutton 互斥選項) --
        # 因為 PPT 截圖中，性別列沒有左側的 Label，故直接合併跨欄顯示
        self.gender_var = tk.StringVar(value=self.default_gender)
        gender_frame = tk.Frame(root)
        gender_frame.grid(row=2, column=0, columnspan=2, pady=2)
        tk.Radiobutton(gender_frame, text="男", variable=self.gender_var, value="男").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(gender_frame, text="女", variable=self.gender_var, value="女").pack(side=tk.LEFT, padx=10)
        
        # -- 系所欄位 --
        tk.Label(root, text="系所：").grid(row=3, column=0, padx=2, pady=2, sticky="e")
        self.entries["系所"] = tk.Entry(root, width=25)
        self.entries["系所"].grid(row=3, column=1, padx=2, pady=2, sticky="w")
        
        # -- 地址欄位 --
        tk.Label(root, text="地址：").grid(row=4, column=0, padx=2, pady=2, sticky="e")
        self.entries["地址"] = tk.Entry(root, width=25)
        self.entries["地址"].grid(row=4, column=1, padx=2, pady=2, sticky="w")
        
        # -- 電話欄位 --
        tk.Label(root, text="電話：").grid(row=5, column=0, padx=2, pady=2, sticky="e")
        self.entries["電話"] = tk.Entry(root, width=25)
        self.entries["電話"].grid(row=5, column=1, padx=2, pady=2, sticky="w")
                
        # 底部控制按鈕區
        btn_frame = tk.Frame(root)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=5)
        
        tk.Button(btn_frame, text="前一筆", width=10, command=self.prev_record).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="下一筆", width=10, command=self.next_record).pack(side=tk.LEFT, padx=2)
        
        # 初始化介面時預設顯示第一筆資料
        self.show_record()
        
    def load_data(self):
        """
        從 data.txt 讀取資料。
        為了確保從命令列的不同層級資料夾執行時都能找到檔案，使用了腳本絕對路徑。
        """
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, self.data_file)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    # 必須確保資料剛好有 6 個欄位，以防出現空行或格式損壞
                    if len(parts) == 6:
                        self.data.append(parts)
        except FileNotFoundError:
            # 例外處理：檔案遺失時提供預設測試資料，避免系統直接崩潰
            self.data = [["1103301234", "王大明", "男", "電子系", "高雄市建工路10號", "3814526"]]
            
    def show_record(self):
        """
        將目前索引 (self.current_idx) 所指向的資料更新至所有 Entry 及 Radiobutton 介面上。
        """
        if not self.data: return
        
        record = self.data[self.current_idx]
        
        # 更新 Entry 前必須先 delete 清空，再 insert 新資料
        self.entries["學號"].delete(0, tk.END)
        self.entries["學號"].insert(0, record[0])
        
        self.entries["姓名"].delete(0, tk.END)
        self.entries["姓名"].insert(0, record[1])
        
        # 更新 StringVar 會自動連動改變 Radiobutton 介面的選擇狀態
        self.gender_var.set(record[2])
        
        self.entries["系所"].delete(0, tk.END)
        self.entries["系所"].insert(0, record[3])
        
        self.entries["地址"].delete(0, tk.END)
        self.entries["地址"].insert(0, record[4])
        
        self.entries["電話"].delete(0, tk.END)
        self.entries["電話"].insert(0, record[5])
        
    def prev_record(self):
        """
        切換至上一筆資料。
        加入了邊界檢查，確保索引不會變成負數。
        """
        if self.current_idx > 0:
            self.current_idx -= 1
            self.show_record()
            
    def next_record(self):
        """
        切換至下一筆資料。
        加入了邊界檢查，確保索引不會超出串列總長度。
        """
        if self.current_idx < len(self.data) - 1:
            self.current_idx += 1
            self.show_record()

if __name__ == "__main__":
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()
