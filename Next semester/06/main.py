import tkinter as tk
import random

# ==========================================
# 1. 設定全域變數 (遊戲參數)
# ==========================================
game_time = 10        # 每關的倒數計時時間 (秒)
grid_rows = 10        # 遊戲畫面的網格總列數
grid_cols = 10        # 遊戲畫面的網格總欄數
mole_min = 5          # 每一關最少出現幾隻地鼠
mole_max = 12         # 每一關最多出現幾隻地鼠
mole_char = "!"       # 畫面上代表地鼠的符號

# 遊戲狀態變數
stage = 1             # 目前關卡
score = 0             # 總分
mole_count = 0        # 目前畫面上有幾隻地鼠
time_left = game_time # 剩餘時間
buttons = []          # 存放所有按鈕的二維陣列


# ==========================================
# 2. 遊戲主要邏輯 (打地鼠、開始新關卡、倒數計時)
# ==========================================
def start_stage():
    """
    開始新的一關。
    負責重置時間、清理上一關殘留的地鼠，並隨機生成新的一批地鼠。
    """
    global time_left, stage, mole_count
    
    # 重設剩餘時間為這關預設的時間
    time_left = game_time
    # 更新畫面上的關卡文字
    lbl_stage.config(text=f"Stage: {stage}")
    
    # 第一步：清除畫面上所有的地鼠，把每個格子都恢復為空白按鈕
    for r in range(grid_rows):
        for c in range(grid_cols):
            buttons[r][c].config(text="", state="normal")
            
    # 第二步：隨機決定這關要出現幾隻地鼠
    # random.randint(a, b) 會產生一個 a 到 b 之間的隨機整數
    num_moles = random.randint(mole_min, mole_max)
    
    # 產生所有可能出現的座標位置 (例如 (0,0) 到 (9,9))
    all_positions = []
    for r in range(grid_rows):
        for c in range(grid_cols):
            all_positions.append((r, c))
            
    # 使用 random.sample 從所有座標中，隨機抽出我們要的數量 (不會重複抽到同一個格子)
    positions = random.sample(all_positions, num_moles)
    
    # 針對抽出來的這些座標，把代表地鼠的符號放進去
    for r, c in positions:
        buttons[r][c].config(text=mole_char)
        
    # 更新畫面上方的地鼠數量標籤
    mole_count = num_moles
    lbl_mole.config(text=f"地鼠數量: {mole_count}")
    
    # 呼叫計時器函式開始倒數
    countdown()


def whack(r, c):
    """
    處理玩家敲擊地鼠洞的邏輯。
    當點擊的按鈕上方有地鼠 ('!') 時，消除地鼠並增加得分。
    """
    global score
    
    # 取得被點擊的那個按鈕元件
    btn = buttons[r][c]
    
    # 如果這個按鈕上面的文字剛好是代表地鼠的符號
    if btn.cget("text") == mole_char:
        # 敲擊成功：將按鈕文字清空，表示地鼠被打掉了
        btn.config(text="")
        # 總分加 1
        score += 1
        # 更新畫面的總分文字
        lbl_score.config(text=f"總分: {score}")


def countdown():
    """
    處理遊戲倒數計時。
    每秒遞減一次，當時間歸零時自動進入下一關 (Stage + 1)。
    """
    global time_left, stage
    
    # 只要時間還大於 0，就繼續倒數
    if time_left > 0:
        time_left -= 1
        # 使用 root.after() 方法，讓程式在 1000 毫秒 (1 秒) 後，再執行一次 countdown 函式
        root.after(1000, countdown)
    else:
        # 如果時間歸零了，就代表這關結束，進入下一關
        stage += 1
        start_stage()


# ==========================================
# 3. 建立視窗與畫面配置 (GUI)
# ==========================================
root = tk.Tk()
root.title("打地鼠遊戲 (基礎版)")

# 上半部：建立遊戲主要的網格區域 (地鼠洞)
grid_frame = tk.Frame(root)
grid_frame.pack()

# 使用雙層迴圈建立自訂大小的地鼠網格 (按鈕)
for i in range(grid_rows):
    row_btns = []
    for j in range(grid_cols):
        # width=2, height=1 的設定是為了讓按鈕呈現接近正方形的小格子
        # command 綁定點擊事件，並將目前的行列座標 (i, j) 傳入 whack 函式
        btn = tk.Button(
            grid_frame, 
            text="", 
            width=2, 
            height=1, 
            font=("Courier", 10, "bold"),
            command=lambda r=i, c=j: whack(r, c)
        )
        btn.grid(row=i, column=j, sticky="nsew", padx=0, pady=0)
        row_btns.append(btn)
    buttons.append(row_btns) # 將一整列按鈕放入整體陣列中
    
# 下半部：建立遊戲資訊顯示區域
info_frame = tk.Frame(root)
info_frame.pack(fill=tk.X, pady=5)

# 第一列資訊：顯示 Stage (左) 與 地鼠數量 (右)
row1_frame = tk.Frame(info_frame)
row1_frame.pack(fill=tk.X, padx=20)

lbl_stage = tk.Label(row1_frame, text=f"Stage: {stage}")
lbl_stage.pack(side=tk.LEFT)

lbl_mole = tk.Label(row1_frame, text=f"地鼠數量: {mole_count}")
lbl_mole.pack(side=tk.RIGHT)

# 第二列資訊：顯示總分 (置中)
row2_frame = tk.Frame(info_frame)
row2_frame.pack(fill=tk.X)

lbl_score = tk.Label(row2_frame, text=f"總分: {score}")
lbl_score.pack()

# 初始化介面完成後，立刻啟動第一關
start_stage()

# ==========================================
# 4. 啟動程式
# ==========================================
root.mainloop()
