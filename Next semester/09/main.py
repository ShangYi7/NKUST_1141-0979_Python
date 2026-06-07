import tkinter as tk
import random
import string

class TypingGameApp:
    """
    打字消除遊戲主程式類別。
    方塊會從畫面頂部不斷掉落，玩家需要輸入左下角提示的指定文字來消除畫面中最底層的方塊。
    """
    def __init__(self, root):
        self.root = root
        self.root.title("TOD")
        
        # ==========================================
        # ⬇️⬇️⬇️ 遊戲參數設定區 (可隨意修改) ⬇️⬇️⬇️
        # ==========================================
        self.max_blocks = 10           # 遊戲總共會掉落多少個方塊 (破關條件)
        self.grid_cols = 10            # 遊戲畫面的網格總欄數 (橫向格數)
        self.grid_rows = 10            # 遊戲畫面的網格總列數 (縱向格數)
        self.cell_size = 30            # 每個格子的寬度與高度 (像素)
        
        self.word_length = 5           # 隨機生成的英文字母長度
        
        self.spawn_min_time = 1500     # 產生下一個方塊的最短等待時間 (毫秒)
        self.spawn_max_time = 3000     # 產生下一個方塊的最長等待時間 (毫秒)
        
        self.fall_interval = 100       # 方塊多久往下掉落一次 (毫秒，越低越平滑但也越耗資源)
        self.fall_pixels = 5           # 每次掉落要往下移動多少像素 (越大掉越快)
        # ==========================================
        # ⬆️⬆️⬆️ 遊戲參數設定區 (可隨意修改) ⬆️⬆️⬆️
        # ==========================================
        
        self.score = 0
        self.blocks = []               # 儲存畫布上方塊物件 (Rectangle ID) 的清單
        self.blocks_dropped = 0
        self.game_over = False
        
        # 建立畫布作為遊戲區 (根據設定自動計算總寬高)
        canvas_width = self.cell_size * self.grid_cols
        canvas_height = self.cell_size * self.grid_rows
        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.pack()
        
        # 繪製背景參考用的格線
        for i in range(self.grid_cols + 1):
            self.canvas.create_line(i*self.cell_size, 0, i*self.cell_size, canvas_height, fill="gray")
        for i in range(self.grid_rows + 1):
            self.canvas.create_line(0, i*self.cell_size, canvas_width, i*self.cell_size, fill="gray")
            
        # 建立底部的控制介面：顯示目標單字、輸入框、與分數
        self.bottom_frame = tk.Frame(root)
        self.bottom_frame.pack(fill=tk.X, pady=2)
        
        self.lbl_target = tk.Label(self.bottom_frame, text="", width=10, anchor="e")
        self.lbl_target.pack(side=tk.LEFT)
        
        self.entry = tk.Entry(self.bottom_frame, width=15)
        self.entry.pack(side=tk.LEFT, padx=5)
        # 綁定 Enter 鍵，玩家輸入完畢不需用滑鼠點擊即可送出檢查
        self.entry.bind("<Return>", self.check_input)
        self.entry.focus()
        
        self.lbl_score = tk.Label(self.bottom_frame, text=f"score: {self.score}", anchor="e")
        self.lbl_score.pack(side=tk.RIGHT, padx=5)
        
        # 產生第一個目標單字
        self.current_word = self.generate_word()
        self.lbl_target.config(text=self.current_word)
        
        # 開始方塊掉落的循環迴圈
        self.spawn_block()
        self.update_fall()
        
    def generate_word(self):
        """
        隨機生成指定長度的英文字串作為玩家輸入的目標。
        """
        return "".join(random.choices(string.ascii_lowercase, k=self.word_length))
        
    def spawn_block(self):
        """
        從最上方隨機一欄產生掉落方塊。
        會受到總數量限制，達到限制數量則不再產生。
        """
        if self.blocks_dropped >= self.max_blocks or self.game_over:
            return
            
        col = random.randint(0, self.grid_cols - 1)
        x1 = col * self.cell_size
        y1 = 0
        x2 = x1 + self.cell_size
        y2 = self.cell_size
        
        # 在畫布上產生方塊，並將 ID 存入 self.blocks 進行後續追蹤
        rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
        
        self.blocks.append(rect_id)
        self.blocks_dropped += 1
            
        # 隨機延遲後，排程產生下一顆方塊
        next_spawn_time = random.randint(self.spawn_min_time, self.spawn_max_time)
        self.root.after(next_spawn_time, self.spawn_block)
        
    def update_fall(self):
        """
        方塊的下落邏輯更新循環。
        處理方塊的向下移動、邊界偵測（掉出畫面則銷毀），以及遊戲結束判定。
        """
        if self.game_over: return
        
        remaining_blocks = []
        canvas_height = self.cell_size * self.grid_rows
        
        for rect_id in self.blocks:
            # 每個方塊往下移動指定的像素
            self.canvas.move(rect_id, 0, self.fall_pixels)
            coords = self.canvas.coords(rect_id)
            # 判斷方塊是否還在畫面內（Y 座標還沒超過畫布高度）
            if coords and coords[1] < canvas_height:
                remaining_blocks.append(rect_id)
            else:
                # 方塊已完全掉出畫面，從畫布與追蹤陣列中刪除
                self.canvas.delete(rect_id)
                
        # 更新陣列，只保留還在畫面上的方塊
        self.blocks = remaining_blocks
            
        # 檢查遊戲結束條件：已達最大產生數量，且畫面上已經沒有剩餘的方塊
        if self.blocks_dropped >= self.max_blocks and not self.blocks:
            self.end_game()
            return
            
        # 排程執行下一次物理更新
        self.root.after(self.fall_interval, self.update_fall)
        
    def check_input(self, event):
        """
        驗證使用者的輸入內容。
        若與目標單字相符，則尋找並消除畫面上離底部最近的方塊，並加分。
        """
        if self.game_over: return
        typed_word = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        
        if typed_word == self.current_word:
            # 尋找 Y 座標最大（離底部最近）的方塊索引
            best_idx = -1
            max_y = -1
            
            for i, rect_id in enumerate(self.blocks):
                coords = self.canvas.coords(rect_id)
                if coords and coords[3] > max_y:
                    max_y = coords[3]
                    best_idx = i
                    
            if best_idx != -1:
                # 將方塊自陣列移除並從畫布刪除
                rect_id = self.blocks.pop(best_idx)
                self.canvas.delete(rect_id)
                
                # 更新分數
                self.score += 1
                self.lbl_score.config(text=f"score: {self.score}")
                
            # 無論畫面上是否還有方塊，只要打字正確就產生新題目
            self.current_word = self.generate_word()
            self.lbl_target.config(text=self.current_word)
            
        # 若因為提早將畫面上所有方塊消除完而滿足條件，立即結束遊戲
        if self.blocks_dropped >= self.max_blocks and not self.blocks:
            self.end_game()
            
    def end_game(self):
        """
        遊戲結束處理，更新介面並停止遊戲邏輯。
        """
        self.game_over = True
        self.lbl_target.config(text="Game Over")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingGameApp(root)
    root.mainloop()
