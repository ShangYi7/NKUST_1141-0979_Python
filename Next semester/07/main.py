import tkinter as tk
from PIL import Image, ImageTk
import os
import random

# ==========================================
# 1. 設定全域變數 (遊戲參數)
# ==========================================
grid_size = 8             # 環狀邊框的長寬網格數 (例如 8 表示 8x8 的外框)
image_size = 50           # 水果圖片縮放的長寬 (像素)
spin_start_delay = 50     # 剛開始轉動時的速度 (毫秒，數值越低代表轉越快)
spin_friction_min = 2     # 每次轉動後最少增加多少延遲 (用來模擬減速摩擦力)
spin_friction_max = 10    # 每次轉動後最多增加多少延遲 
spin_stop_threshold = 300 # 當延遲時間大於此數值時，判定為停止轉動

# 系統狀態變數
images = {}               # 用來存放載入並縮放後的水果圖片物件字典
labels = []               # 用來存放畫面上組成外框的標籤(Label)元件陣列
current_pos = 0           # 記錄目前跑馬燈亮起的位置索引 (0 ~ 27)
spinning = False          # 記錄目前轉盤是否正在轉動中 (避免重複啟動)
spin_delay = 50           # 當下這次轉動的延遲時間


# ==========================================
# 2. 遊戲主要邏輯 (高亮顯示與轉盤動畫)
# ==========================================
def highlight(pos):
    """
    高亮顯示指定的格子，將其背景設定為紅色，其餘恢復為白色。
    藉由快速切換背景顏色來製造跑馬燈的視覺效果。
    :param pos: 要高亮顯示的索引位置 (0 到 len(labels)-1)
    """
    # 使用 enumerate 走訪所有的標籤元件，i 是索引，lbl 是元件本身
    for i, lbl in enumerate(labels):
        if i == pos:
            lbl.config(bg="red")   # 亮起
        else:
            lbl.config(bg="white") # 熄滅


def start_spin():
    """
    按下 GO 按鈕後啟動轉盤。
    """
    global spinning, spin_delay
    
    # 如果已經在轉了，就不做任何事直接跳出 (防連點)
    if spinning: 
        return
        
    spinning = True
    spin_delay = spin_start_delay # 重置延遲時間為初始速度
    btn_go.config(state="disabled") # 轉動期間先把 GO 按鈕鎖定停用
    
    # 開始執行轉動迴圈
    spin()


def spin():
    """
    執行跑馬燈轉動邏輯。
    每次呼叫時位置 +1，並排程下一次呼叫自己，同時增加延遲時間。
    """
    global current_pos, spin_delay, spinning
    
    # 將目前位置加 1，如果超過最大索引值，就用 % (取餘數) 讓它回到 0，形成環狀
    current_pos = (current_pos + 1) % len(labels)
    # 呼叫高亮顯示函式
    highlight(current_pos)
    
    # 每次轉動後，隨機增加一點延遲時間，造成慢慢減速的效果
    spin_delay += random.randint(spin_friction_min, spin_friction_max)
    
    # 若延遲時間還沒達到停止門檻，就繼續排程下一次轉動
    if spin_delay < spin_stop_threshold:
        # root.after 可以在指定的毫秒後，呼叫指定的函式
        root.after(spin_delay, spin)
    else:
        # 延遲過長，判定為完全停止
        spinning = False
        btn_go.config(state="normal") # 恢復 GO 按鈕的使用


# ==========================================
# 3. 建立視窗與載入圖片
# ==========================================
root = tk.Tk()
root.title("麻阿台 (老虎機) - 基礎版")

# 為了避免在不同工作目錄執行腳本時找不到圖片，使用 os 模組取得目前腳本的絕對路徑來定位 images 資料夾
script_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(script_dir, "images")

# 預期的 8 種水果圖示檔名
files = [
    "apple.png", "betelnut.png", "double7.png", "grape.png", 
    "orange.png", "ring.png", "star.png", "watermelon.png"
]

# 讀取並縮放這 8 張圖片
for file in files:
    path = os.path.join(image_dir, file)
    if os.path.exists(path):
        # 調整大小以確保視窗不會過大 (Image.open 是 Pillow 套件的功能)
        img = Image.open(path).resize((image_size, image_size))
        images[file] = ImageTk.PhotoImage(img) # 轉成 Tkinter 看得懂的格式並存入字典
    else:
        # 容錯處理：若電腦裡找不到圖片，則設為 None，稍後會改以文字方塊替代
        images[file] = None


# ==========================================
# 4. 產生 8x8 網格外圍的環狀座標並放置標籤
# ==========================================
positions = []
# 用 4 個迴圈分別算出上、右、下、左四個邊的網格座標 (例如 [0,0], [0,1]...)
# 上排
for c in range(grid_size): 
    positions.append((0, c))
# 右排
for r in range(1, grid_size - 1): 
    positions.append((r, grid_size - 1))
# 下排 (從右到左所以是遞減 -1)
for c in range(grid_size - 1, -1, -1): 
    positions.append((grid_size - 1, c))
# 左排 (從下到上遞減 -1)
for r in range(grid_size - 2, 0, -1): 
    positions.append((r, 0))

# 根據上面算好的 28 個環狀座標位置，依序擺放 Label 元件
for idx, pos in enumerate(positions):
    # 每個格子隨機挑選一張水果圖片
    rand_file = random.choice(files)
    # 從字典中取出圖片物件
    img_obj = images.get(rand_file, "")
    
    lbl = tk.Label(root, image=img_obj, bg="white", width=image_size, height=image_size)
    
    # 若載入失敗 (圖片是 None)，給予預設的文字寬高，防止因為沒圖片造成排版壞掉
    if not img_obj:
        lbl.config(width=6, height=3)
        
    # 將 Label 放上對應的座標 (row, col)
    lbl.grid(row=pos[0], column=pos[1], padx=2, pady=2)
    # 將建立好的 Label 加進陣列中，以便後續可以修改它的背景色
    labels.append(lbl)

# ==========================================
# 5. 在中央放置「GO」啟動按鈕
# ==========================================
# 利用 rowspan=2 和 columnspan=2，使這個按鈕跨越中間數個網格，剛好置於 8x8 環狀的中央區域
btn_go = tk.Button(root, text="GO", font=("Arial", 14), command=start_spin)
btn_go.grid(row=3, column=3, rowspan=2, columnspan=2, ipadx=10, ipady=10)

# 初始化時，先高亮顯示第 0 個位置
highlight(current_pos)

# ==========================================
# 6. 啟動程式
# ==========================================
root.mainloop()
