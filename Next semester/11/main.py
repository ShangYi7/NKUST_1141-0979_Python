import tkinter as tk
from tkinter import messagebox

class CrudApp:
    """
    包含 CRUD 功能的學生資料表應用程式。
    除了具備檢視功能外，另支援對 txt 檔案內容進行即時的更新、刪除與新增。
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
        
        # 用於標記目前是否處於「準備新增一筆全新資料」的狀態
        # 若為 True，則在點擊更新按鈕時，會將表單內容作為新資料附加至陣列尾端，而非覆蓋現有資料
        self.is_adding = False
        
        self.load_data()
        
        # 字典容器：用於集中管理 Entry 元件，便於迴圈與名稱查詢
        self.entries = {}
        
        # 建立 UI 版面配置 (延續作業 10 之樣式)
        tk.Label(root, text="學號：").grid(row=0, column=0, padx=2, pady=2, sticky="e")
        self.entries["學號"] = tk.Entry(root, width=25)
        self.entries["學號"].grid(row=0, column=1, padx=2, pady=2, sticky="w")
        
        tk.Label(root, text="姓名：").grid(row=1, column=0, padx=2, pady=2, sticky="e")
        self.entries["姓名"] = tk.Entry(root, width=25)
        self.entries["姓名"].grid(row=1, column=1, padx=2, pady=2, sticky="w")
        
        self.gender_var = tk.StringVar(value=self.default_gender)
        gender_frame = tk.Frame(root)
        gender_frame.grid(row=2, column=0, columnspan=2, pady=2)
        tk.Radiobutton(gender_frame, text="男", variable=self.gender_var, value="男").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(gender_frame, text="女", variable=self.gender_var, value="女").pack(side=tk.LEFT, padx=10)
        
        tk.Label(root, text="系所：").grid(row=3, column=0, padx=2, pady=2, sticky="e")
        self.entries["系所"] = tk.Entry(root, width=25)
        self.entries["系所"].grid(row=3, column=1, padx=2, pady=2, sticky="w")
        
        tk.Label(root, text="地址：").grid(row=4, column=0, padx=2, pady=2, sticky="e")
        self.entries["地址"] = tk.Entry(root, width=25)
        self.entries["地址"].grid(row=4, column=1, padx=2, pady=2, sticky="w")
        
        tk.Label(root, text="電話：").grid(row=5, column=0, padx=2, pady=2, sticky="e")
        self.entries["電話"] = tk.Entry(root, width=25)
        self.entries["電話"].grid(row=5, column=1, padx=2, pady=2, sticky="w")
                
        # 底部控制按鈕區：包含切換與所有 CRUD 動作
        btn_frame = tk.Frame(root)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=5)
        
        tk.Button(btn_frame, text="<<", command=self.prev_record).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="更新", command=self.update_record).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="刪除", command=self.delete_record).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="新增", command=self.add_record).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text=">>", command=self.next_record).pack(side=tk.LEFT, padx=2)
        
        # 啟動時立刻顯示第一筆資料
        self.show_record()
        
    def load_data(self):
        """
        讀取外部 txt 檔案並將其存入記憶體中的 self.data 二維陣列。
        使用腳本所在之絕對路徑，確保不同路徑啟動也能正確對應。
        """
        import os
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.script_dir, self.data_file)
        self.data = []
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    # 避免空行或不完整的資料破壞程式執行
                    if len(parts) == 6:
                        self.data.append(parts)
        except FileNotFoundError:
            pass
            
    def save_data(self):
        """
        將記憶體中的資料列即時覆寫寫入回 txt 檔案。
        此為所有增刪改操作的最後一步，以確保檔案維持最新狀態。
        """
        with open(self.file_path, "w", encoding="utf-8") as f:
            for record in self.data:
                f.write(",".join(record) + "\n")
                
    def show_record(self):
        """
        顯示指定索引位置的資料到畫面上。
        同時會自動重置「新增模式」狀態，避免使用者切換資料後誤把原本的覆蓋動作變成新增。
        """
        self.is_adding = False
        # 清除目前畫面上所有輸入框舊有內容
        for e in self.entries.values():
            e.delete(0, tk.END)
            
        # 若資料表為空，則留空畫面並結束函式
        if not self.data:
            self.gender_var.set(self.default_gender)
            return
            
        # 依序填入欄位值
        record = self.data[self.current_idx]
        self.entries["學號"].insert(0, record[0])
        self.entries["姓名"].insert(0, record[1])
        self.gender_var.set(record[2])
        self.entries["系所"].insert(0, record[3])
        self.entries["地址"].insert(0, record[4])
        self.entries["電話"].insert(0, record[5])
        
    def prev_record(self):
        # 切換上一筆（防止出界處理）
        if self.current_idx > 0 and self.data:
            self.current_idx -= 1
            self.show_record()
            
    def next_record(self):
        # 切換下一筆（防止出界處理）
        if self.current_idx < len(self.data) - 1 and self.data:
            self.current_idx += 1
            self.show_record()
            
    def get_current_input(self):
        """
        輔助函式：統整收集目前畫面上所有的 Entry 及 Radiobutton 數值，並組成陣列回傳。
        """
        return [
            self.entries["學號"].get().strip(),
            self.entries["姓名"].get().strip(),
            self.gender_var.get(),
            self.entries["系所"].get().strip(),
            self.entries["地址"].get().strip(),
            self.entries["電話"].get().strip()
        ]
            
    def update_record(self):
        """
        「更新」按鈕邏輯。
        根據 is_adding 的布林值來決定是：
        1. True -> 新增一筆全新資料並附加在最後。
        2. False -> 直接替換目前 self.current_idx 上的原有資料。
        """
        new_record = self.get_current_input()
        # 基礎欄位驗證：至少需輸入學號
        if not new_record[0]:
            return
            
        if self.is_adding:
            # 新增邏輯：加入陣列尾端，並將索引切換至該筆最新資料
            self.data.append(new_record)
            self.current_idx = len(self.data) - 1
            self.is_adding = False
        else:
            # 覆蓋舊資料邏輯
            if not self.data: return
            self.data[self.current_idx] = new_record
            
        # 同步更新至檔案，並重整介面
        self.save_data()
        self.show_record()
        
    def delete_record(self):
        """
        「刪除」按鈕邏輯。
        移除目前索引的資料列，並自動判斷下一筆該顯示的索引位置（例如若刪除最後一筆，則退回上一筆）。
        """
        if not self.data: return
        del self.data[self.current_idx]
        
        # 若刪除了最後一筆資料，將索引往後退一格以防止陣列出界
        if self.current_idx >= len(self.data) and self.current_idx > 0:
            self.current_idx -= 1
            
        self.save_data()
        self.show_record()
            
    def add_record(self):
        """
        「新增」按鈕邏輯。
        本身不會將資料寫入檔案，僅負責將介面清空，並設定 is_adding 旗標，
        待使用者輸入完畢按下「更新」時才會正式儲存。
        """
        self.is_adding = True
        for e in self.entries.values():
            e.delete(0, tk.END)
        self.gender_var.set(self.default_gender)

if __name__ == "__main__":
    root = tk.Tk()
    app = CrudApp(root)
    root.mainloop()
