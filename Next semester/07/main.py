import tkinter as tk
from PIL import Image, ImageTk
import os
import random

class SlotMachineApp:
    """
    老虎機（麻阿台）主程式類別。
    負責載入水果圖片，並以環狀陣列的方式動態呈現跑馬燈抽獎效果。
    """
    def __init__(self, root):
        self.root = root
        self.root.title("麻阿台")
        
        # ==========================================
        # ⬇️⬇️⬇️ 遊戲參數設定區 (可隨意修改) ⬇️⬇️⬇️
        # ==========================================
        self.grid_size = 8             # 環狀邊框的長寬網格數 (例如 8 表示 8x8 的外框)
        self.image_size = 50           # 水果圖片縮放的長寬 (像素)
        self.spin_start_delay = 50     # 剛開始轉動時的速度 (毫秒，越低越快)
        self.spin_friction_min = 2     # 每次轉動後最少增加多少延遲 (減速摩擦力)
        self.spin_friction_max = 10    # 每次轉動後最多增加多少延遲 (減速摩擦力)
        self.spin_stop_threshold = 300 # 當延遲時間大於此數值時，判定為停止轉動
        # ==========================================
        # ⬆️⬆️⬆️ 遊戲參數設定區 (可隨意修改) ⬆️⬆️⬆️
        # ==========================================
        
        self.images = {}
        # 為了避免在不同工作目錄執行腳本時找不到圖片，使用絕對路徑來定位 images 資料夾
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(script_dir, "images")
        
        # 預期的 8 種水果圖示檔名
        files = ["apple.png", "betelnut.png", "double7.png", "grape.png", "orange.png", "ring.png", "star.png", "watermelon.png"]
        
        # 讀取並縮放圖片
        for file in files:
            path = os.path.join(image_dir, file)
            if os.path.exists(path):
                # 調整大小以確保視窗不會過大
                img = Image.open(path).resize((self.image_size, self.image_size))
                self.images[file] = ImageTk.PhotoImage(img)
            else:
                # 容錯處理：若圖片遺失則設為 None，稍後介面會改以文字方塊替代
                self.images[file] = None
                
        self.labels = []
        
        # 產生 8x8 網格外圍的環狀座標，總計 28 格，用以精準重現 PPT 中的框狀佈局
        positions = []
        # 上排
        for c in range(self.grid_size): positions.append((0, c))
        # 右排
        for r in range(1, self.grid_size - 1): positions.append((r, self.grid_size - 1))
        # 下排
        for c in range(self.grid_size - 1, -1, -1): positions.append((self.grid_size - 1, c))
        # 左排
        for r in range(self.grid_size - 2, 0, -1): positions.append((r, 0))
        
        # 根據算好的環狀座標依序擺放 Label
        for idx, pos in enumerate(positions):
            rand_file = random.choice(files)
            lbl = tk.Label(root, image=self.images.get(rand_file, ""), bg="white", width=self.image_size, height=self.image_size)
            # 若載入失敗，給予預設文字長寬，防止因為 None image 造成視窗膨脹
            if not self.images.get(rand_file):
                lbl.config(width=6, height=3)
            lbl.grid(row=pos[0], column=pos[1], padx=2, pady=2)
            self.labels.append(lbl)
            
        # 在中央放置「GO」啟動按鈕
        # 利用 rowspan 和 columnspan 使按鈕跨越中間數個網格，置於環狀的中央區域
        self.btn_go = tk.Button(root, text="GO", font=("Arial", 14), command=self.start_spin)
        self.btn_go.grid(row=3, column=3, rowspan=2, columnspan=2, ipadx=10, ipady=10)
        
        self.current_pos = 0
        self.spinning = False
        self.spin_delay = 50
        
        # 初始化高亮顯示第一個位置
        self.highlight(self.current_pos)
        
    def highlight(self, pos):
        """
        高亮顯示指定的格子，將其背景設定為紅色，其餘為白色。
        藉由快速切換背景顏色來製造跑馬燈的視覺效果。
        """
        for i, lbl in enumerate(self.labels):
            lbl.config(bg="red" if i == pos else "white")
            
    def start_spin(self):
        """
        啟動轉盤。
        防止重複點擊，並重置延遲時間。
        """
        if self.spinning: return
        self.spinning = True
        self.spin_delay = self.spin_start_delay
        self.btn_go.config(state="disabled")
        self.spin()
        
    def spin(self):
        """
        執行跑馬燈轉動邏輯。
        每次呼叫時位置 +1，並逐漸增加下一次執行的延遲時間，以模擬輪盤摩擦力「越轉越慢」的物理效果。
        """
        self.current_pos = (self.current_pos + 1) % len(self.labels)
        self.highlight(self.current_pos)
        
        # 每次轉動後，隨機增加延遲時間，造成減速效果
        self.spin_delay += random.randint(self.spin_friction_min, self.spin_friction_max)
        
        # 若延遲時間小於門檻，表示還沒完全停下，繼續排程下一次轉動
        if self.spin_delay < self.spin_stop_threshold:
            self.root.after(self.spin_delay, self.spin)
        else:
            # 延遲過長，判定為完全停止，恢復按鈕狀態
            self.spinning = False
            self.btn_go.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()
