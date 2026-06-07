import tkinter as tk
import random

class WhackAMoleApp:
    """
    打地鼠遊戲主程式類別。
    利用 Tkinter 的 Button 網格來模擬地鼠洞，透過定時器更新剩餘時間與關卡。
    """
    def __init__(self, root):
        self.root = root
        self.root.title("tk")
        
        # ==========================================
        # ⬇️⬇️⬇️ 遊戲參數設定區 (可隨意修改) ⬇️⬇️⬇️
        # ==========================================
        self.game_time = 10            # 每關的倒數計時時間 (秒)
        self.grid_rows = 10            # 遊戲畫面的網格總列數
        self.grid_cols = 10            # 遊戲畫面的網格總欄數
        self.mole_min = 5              # 每一關最少出現幾隻地鼠
        self.mole_max = 12             # 每一關最多出現幾隻地鼠
        self.mole_char = "!"           # 畫面上代表地鼠的符號
        # ==========================================
        # ⬆️⬆️⬆️ 遊戲參數設定區 (可隨意修改) ⬆️⬆️⬆️
        # ==========================================
        
        # 初始化遊戲狀態參數
        self.stage = 1
        self.score = 0
        self.mole_count = 0
        self.time_left = self.game_time
        self.timer_id = None
        
        # 建立遊戲主要的網格區域 (Top frame)
        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack()
        
        self.buttons = []
        # 建立自訂大小的地鼠網格
        for i in range(self.grid_rows):
            row_btns = []
            for j in range(self.grid_cols):
                # width=2, height=1 的設定是為了讓按鈕呈現接近正方形的小格子
                # command 綁定 click 事件，並將目前的行列座標 (r, c) 傳入，以便知道是哪一個洞被敲擊
                btn = tk.Button(self.grid_frame, text="", width=2, height=1, font=("Courier", 10, "bold"),
                                command=lambda r=i, c=j: self.whack(r, c))
                btn.grid(row=i, column=j, sticky="nsew", padx=0, pady=0)
                row_btns.append(btn)
            self.buttons.append(row_btns)
            
        # 建立下方的遊戲資訊顯示區域 (Bottom frame)
        self.info_frame = tk.Frame(root)
        self.info_frame.pack(fill=tk.X, pady=5)
        
        # 第一列：顯示 Stage (左) 與 地鼠數量 (右)
        self.row1_frame = tk.Frame(self.info_frame)
        self.row1_frame.pack(fill=tk.X, padx=20)
        self.lbl_stage = tk.Label(self.row1_frame, text=f"Stage: {self.stage}")
        self.lbl_stage.pack(side=tk.LEFT)
        self.lbl_mole = tk.Label(self.row1_frame, text=f"地鼠數量: {self.mole_count}")
        self.lbl_mole.pack(side=tk.RIGHT)
        
        # 第二列：顯示總分 (置中)
        self.row2_frame = tk.Frame(self.info_frame)
        self.row2_frame.pack(fill=tk.X)
        self.lbl_score = tk.Label(self.row2_frame, text=f"總分: {self.score}")
        self.lbl_score.pack()
        
        # 初始化完成後，自動啟動第一關
        self.start_stage()
        
    def start_stage(self):
        """
        開始新的一關。
        負責重置時間、清理上一關殘留的地鼠，並隨機生成新的一批地鼠。
        """
        self.time_left = self.game_time
        self.lbl_stage.config(text=f"Stage: {self.stage}")
        
        # 清除畫面上所有的地鼠，恢復為空白按鈕
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                self.buttons[r][c].config(text="", state="normal")
                
        # 隨機決定此關卡的地鼠數量
        num_moles = random.randint(self.mole_min, self.mole_max)
        # 隨機抽取網格座標來放置地鼠
        positions = random.sample([(r, c) for r in range(self.grid_rows) for c in range(self.grid_cols)], min(num_moles, self.grid_rows * self.grid_cols))
        for r, c in positions:
            # 隨機決定是普通地鼠還是黃金地鼠
            if random.random() > 0.8:  # 20% 機率是黃金地鼠
                self.buttons[r][c].config(text="$", fg="gold")
            else:
                self.buttons[r][c].config(text=self.mole_char, fg="black")
            
        self.mole_count = num_moles
        self.lbl_mole.config(text=f"地鼠數量: {self.mole_count}")
        
        # 啟動本關卡的倒數計時器
        self.countdown()
        
    def whack(self, r, c):
        """
        處理玩家敲擊地鼠洞的邏輯。
        當點擊的按鈕上方有地鼠 ('!') 時，消除地鼠並增加得分。
        """
        btn = self.buttons[r][c]
        if btn.cget("text") == self.mole_char:
            # 敲擊成功：將按鈕文字清空，表示地鼠被打掉
            btn.config(text="")
            self.score += 1
            self.lbl_score.config(text=f"總分: {self.score}")
        elif btn.cget("text") == "$":
            # 敲擊黃金地鼠得 5 分
            btn.config(text="")
            self.score += 5
            self.lbl_score.config(text=f"總分: {self.score}")
        else:
            # 打錯洞扣分機制
            if self.score > 0:
                self.score -= 1
            self.lbl_score.config(text=f"總分: {self.score}")
            
    def countdown(self):
        """
        處理遊戲倒數計時。
        每秒遞減一次，當時間歸零時自動進入下一關 (Stage + 1)。
        """
        if self.time_left > 0:
            self.time_left -= 1
            # 使用 tk.after 排程 1000 毫秒後再次呼叫自己，形成迴圈計時器
            self.timer_id = self.root.after(1000, self.countdown)
        else:
            # 時間結束，自動推進到下一關
            self.stage += 1
            self.start_stage()

if __name__ == "__main__":
    root = tk.Tk()
    app = WhackAMoleApp(root)
    root.mainloop()
