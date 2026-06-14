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
mole_char = "!"       # 畫面上代表普通地鼠的符號

# 遊戲狀態變數
stage = 1             # 目前關卡
score = 0             # 總分
mole_count = 0        # 目前畫面上有幾隻地鼠
time_left = game_time # 剩餘時間
buttons = []          # 存放所有按鈕的二維陣列


# ==========================================
# 2. 遊戲主要邏輯
# ==========================================
def start_stage():
    """
    開始新的一關。進階版會額外產生黃金地鼠。
    """
    global time_left, stage, mole_count
    
    time_left = game_time
    lbl_stage.config(text=f"Stage: {stage}")
    
    # 清除畫面上的舊地鼠
    for r in range(grid_rows):
        for c in range(grid_cols):
            buttons[r][c].config(text="", state="normal")
            
    # 決定地鼠總數
    num_moles = random.randint(mole_min, mole_max)
    
    # 產生並抽取座標
    all_positions = []
    for r in range(grid_rows):
        for c in range(grid_cols):
            all_positions.append((r, c))
            
    positions = random.sample(all_positions, min(num_moles, grid_rows * grid_cols))
    
    # 將地鼠放進對應格子
    for r, c in positions:
        # 進階版：隨機決定這隻地鼠是不是黃金地鼠
        # random.random() 會產生一個 0.0 到 1.0 的隨機小數
        if random.random() > 0.8:  
            # 20% 的機率是大於 0.8，將其設為黃金地鼠 "$"
            buttons[r][c].config(text="$", fg="gold")
        else:
            # 80% 的機率是普通地鼠 "!"
            buttons[r][c].config(text=mole_char, fg="black")
            
    mole_count = num_moles
    lbl_mole.config(text=f"地鼠數量: {mole_count}")
    
    countdown()


def whack(r, c):
    """
    處理玩家敲擊地鼠洞的邏輯 (包含進階版計分規則)。
    """
    global score
    btn = buttons[r][c]
    
    # 如果打中普通地鼠
    if btn.cget("text") == mole_char:
        btn.config(text="") # 清空地鼠
        score += 1          # 加 1 分
        lbl_score.config(text=f"總分: {score}")
        
    # 如果打中黃金地鼠
    elif btn.cget("text") == "$":
        btn.config(text="")
        score += 5          # 加 5 分！
        lbl_score.config(text=f"總分: {score}")
        
    # 如果打到空的洞 (打錯洞扣分機制)
    else:
        # 如果分數大於 0 才扣，避免被扣到負數
        if score > 0:
            score -= 1
        lbl_score.config(text=f"總分: {score}")


def countdown():
    """
    處理遊戲倒數計時。
    """
    global time_left, stage
    
    if time_left > 0:
        time_left -= 1
        root.after(1000, countdown)
    else:
        stage += 1
        start_stage()


# ==========================================
# 3. 建立視窗與畫面配置 (GUI)
# ==========================================
root = tk.Tk()
root.title("打地鼠遊戲 (進階版：黃金地鼠)")

# 網格區域
grid_frame = tk.Frame(root)
grid_frame.pack()

# 建立地鼠按鈕
for i in range(grid_rows):
    row_btns = []
    for j in range(grid_cols):
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
    buttons.append(row_btns)
    
# 資訊顯示區域
info_frame = tk.Frame(root)
info_frame.pack(fill=tk.X, pady=5)

row1_frame = tk.Frame(info_frame)
row1_frame.pack(fill=tk.X, padx=20)

lbl_stage = tk.Label(row1_frame, text=f"Stage: {stage}")
lbl_stage.pack(side=tk.LEFT)

lbl_mole = tk.Label(row1_frame, text=f"地鼠數量: {mole_count}")
lbl_mole.pack(side=tk.RIGHT)

row2_frame = tk.Frame(info_frame)
row2_frame.pack(fill=tk.X)

lbl_score = tk.Label(row2_frame, text=f"總分: {score}")
lbl_score.pack()

start_stage()

# ==========================================
# 4. 啟動程式
# ==========================================
root.mainloop()
