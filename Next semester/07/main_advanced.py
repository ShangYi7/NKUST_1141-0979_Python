import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random

# ==========================================
# 1. 設定全域變數 (遊戲參數)
# ==========================================
grid_size = 8             # 環狀邊框的長寬網格數 (例如 8 表示 8x8 的外框)
image_size = 50           # 水果圖片縮放的長寬 (像素)
spin_start_delay = 50     # 剛開始轉動時的速度 (毫秒)
spin_friction_min = 2     # 每次轉動後最少增加多少延遲 (模擬減速)
spin_friction_max = 10    # 每次轉動後最多增加多少延遲
spin_stop_threshold = 300 # 當延遲時間大於此數值時，判定為停止轉動

images = {}               # 用來存放圖片物件
labels = []               # 用來存放組成外框的 Label 元件
current_pos = 0           # 記錄目前亮起的位置索引 (0 ~ 27)
spinning = False          # 記錄目前轉盤是否正在轉動中
spin_delay = 50           # 當下轉動的延遲時間


# ==========================================
# 2. 遊戲主要邏輯 (進階版高亮與彈窗)
# ==========================================
def highlight(pos):
    """
    高亮顯示指定的格子為紅色。
    進階版：加入殘影效果，將前一個格子設定為黃色，其他為白色。
    """
    # 算出「前一格」的位置。如果 pos 是 0，(0 - 1) 取餘數會跑到陣列的最後面，這正是我們要的環狀效果
    prev_pos = (pos - 1) % len(labels) 
    
    for i, lbl in enumerate(labels):
        if i == pos:
            lbl.config(bg="red")      # 當前格子：紅色
        elif i == prev_pos:
            lbl.config(bg="yellow")   # 前一個格子 (殘影)：黃色
        else:
            lbl.config(bg="white")    # 其他：白色


def start_spin():
    """
    按下 GO 按鈕後啟動轉盤。
    """
    global spinning, spin_delay
    if spinning: 
        return
        
    spinning = True
    spin_delay = spin_start_delay 
    btn_go.config(state="disabled") 
    spin()


def spin():
    """
    跑馬燈轉動邏輯。
    """
    global current_pos, spin_delay, spinning
    
    # 往前推進一格，並使用取餘數確保繞圈圈
    current_pos = (current_pos + 1) % len(labels)
    highlight(current_pos)
    
    # 增加延遲，讓轉盤越來越慢
    spin_delay += random.randint(spin_friction_min, spin_friction_max)
    
    # 如果還沒停
    if spin_delay < spin_stop_threshold:
        root.after(spin_delay, spin)
    else:
        # 進階版：完全停止後，跳出訊息視窗
        spinning = False
        btn_go.config(state="normal")
        
        # 使用 messagebox 顯示結果視窗
        messagebox.showinfo("結果", "轉盤停止了！看看你抽中了什麼！")


# ==========================================
# 3. 建立視窗與載入圖片
# ==========================================
root = tk.Tk()
root.title("麻阿台 (老虎機) - 進階版")

script_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(script_dir, "images")

files = [
    "apple.png", "betelnut.png", "double7.png", "grape.png", 
    "orange.png", "ring.png", "star.png", "watermelon.png"
]

for file in files:
    path = os.path.join(image_dir, file)
    if os.path.exists(path):
        img = Image.open(path).resize((image_size, image_size))
        images[file] = ImageTk.PhotoImage(img) 
    else:
        images[file] = None


# ==========================================
# 4. 產生網格與按鈕配置
# ==========================================
positions = []
# 上排
for c in range(grid_size): positions.append((0, c))
# 右排
for r in range(1, grid_size - 1): positions.append((r, grid_size - 1))
# 下排
for c in range(grid_size - 1, -1, -1): positions.append((grid_size - 1, c))
# 左排
for r in range(grid_size - 2, 0, -1): positions.append((r, 0))

# 擺放 Label
for idx, pos in enumerate(positions):
    rand_file = random.choice(files)
    img_obj = images.get(rand_file, "")
    lbl = tk.Label(root, image=img_obj, bg="white", width=image_size, height=image_size)
    if not img_obj:
        lbl.config(width=6, height=3)
    lbl.grid(row=pos[0], column=pos[1], padx=2, pady=2)
    labels.append(lbl)

# 中央 GO 按鈕
btn_go = tk.Button(root, text="GO", font=("Arial", 14), command=start_spin)
btn_go.grid(row=3, column=3, rowspan=2, columnspan=2, ipadx=10, ipady=10)

# 初始化第一格的顏色
highlight(current_pos)

# ==========================================
# 5. 啟動程式
# ==========================================
root.mainloop()
