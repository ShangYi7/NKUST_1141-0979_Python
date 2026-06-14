import tkinter as tk
import random
import string

# ==========================================
# 1. 設定全域變數 (遊戲參數與狀態)
# ==========================================
max_blocks = 10           # 遊戲總共會掉落多少個方塊 (破關條件)
grid_cols = 10            # 遊戲畫面的網格總欄數 (橫向格數)
grid_rows = 10            # 遊戲畫面的網格總列數 (縱向格數)
cell_size = 30            # 每個格子的寬度與高度 (像素)

word_length = 5           # 隨機生成的英文字母長度

spawn_min_time = 1500     # 產生下一個方塊的最短等待時間 (毫秒)
spawn_max_time = 3000     # 產生下一個方塊的最長等待時間 (毫秒)

fall_interval = 100       # 方塊多久往下掉落一次 (毫秒)
fall_pixels = 5           # 每次掉落要往下移動多少像素

score = 0                 # 玩家目前分數
blocks = []               # 儲存畫布上方塊物件 (Rectangle ID) 的清單
blocks_dropped = 0        # 記錄已經掉落了幾個方塊
game_over = False         # 遊戲是否結束
current_word = ""         # 目前玩家需要輸入的目標單字


# ==========================================
# 2. 遊戲主要邏輯
# ==========================================
def generate_word():
    """
    隨機生成指定長度的英文字串作為玩家輸入的目標。
    """
    # random.choices 從 a-z 隨機抽出 word_length 個字母，然後用 join 黏成一個字串
    return "".join(random.choices(string.ascii_lowercase, k=word_length))


def spawn_block():
    """
    從最上方隨機一欄產生掉落方塊。
    """
    global blocks_dropped
    
    # 如果已經產生了足夠的方塊，或是遊戲結束了，就不再產生
    if blocks_dropped >= max_blocks or game_over:
        return
        
    # 隨機挑選一個欄位 (0 到 grid_cols-1)
    col = random.randint(0, grid_cols - 1)
    
    # 計算方塊的左上角 (x1, y1) 與右下角 (x2, y2) 座標
    x1 = col * cell_size
    y1 = 0
    x2 = x1 + cell_size
    y2 = cell_size
    
    # 在畫布上產生方塊，canvas.create_rectangle 會回傳這個方塊的專屬 ID
    rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
    
    # 將這個方塊 ID 加入清單中追蹤
    blocks.append(rect_id)
    blocks_dropped += 1
        
    # 隨機延遲一段時間後，再呼叫自己產生下一個方塊
    next_spawn_time = random.randint(spawn_min_time, spawn_max_time)
    root.after(next_spawn_time, spawn_block)


def update_fall():
    """
    方塊的下落邏輯更新循環。
    處理方塊的向下移動、邊界偵測（掉出畫面則銷毀），以及遊戲結束判定。
    """
    global blocks
    
    if game_over: 
        return
    
    # 建立一個新的清單，用來存放「還在畫面上」的方塊
    remaining_blocks = []
    # 計算畫布的總高度
    canvas_height = cell_size * grid_rows
    
    for rect_id in blocks:
        # 將方塊往下移動 fall_pixels 個像素
        canvas.move(rect_id, 0, fall_pixels)
        
        # 取得方塊移動後的新座標 [x1, y1, x2, y2]
        coords = canvas.coords(rect_id)
        
        # 判斷方塊是否還在畫面內（y1 座標還沒超過畫布高度）
        if coords and coords[1] < canvas_height:
            remaining_blocks.append(rect_id) # 還在畫面內，保留
        else:
            # 已經掉出畫面了，把它從畫布上永久刪除
            canvas.delete(rect_id)
            
    # 更新清單，覆蓋掉舊的
    blocks = remaining_blocks
        
    # 檢查是否破關：掉落的方塊數達到上限，且畫面上已經沒有剩餘的方塊了
    if blocks_dropped >= max_blocks and not blocks:
        end_game()
        return
        
    # 每隔 fall_interval 毫秒，執行一次下落更新
    root.after(fall_interval, update_fall)


def check_input(event):
    """
    驗證使用者的輸入內容。
    當玩家在輸入框按下 Enter 鍵時會觸發 (由 bind 綁定傳入 event 參數)。
    """
    global score, current_word
    
    if game_over: 
        return
        
    # 取得輸入的文字，並清除輸入框
    typed_word = entry.get().strip()
    entry.delete(0, tk.END)
    
    # 如果輸入正確
    if typed_word == current_word:
        # 尋找 Y 座標最大（離底部最近）的方塊
        best_idx = -1
        max_y = -1
        
        for i, rect_id in enumerate(blocks):
            coords = canvas.coords(rect_id)
            if coords and coords[3] > max_y:
                max_y = coords[3]
                best_idx = i
                
        # 如果畫面上確實有方塊
        if best_idx != -1:
            # 將它從陣列中拔除，並從畫布上刪除
            rect_id = blocks.pop(best_idx)
            canvas.delete(rect_id)
            
            # 加分並更新介面
            score += 1
            lbl_score.config(text=f"score: {score}")
            
        # 只要打字正確，就換一個新單字
        current_word = generate_word()
        lbl_target.config(text=current_word)
        
    # 如果打字正確且畫面上已經清空了最後一個方塊，檢查是否破關
    if blocks_dropped >= max_blocks and not blocks:
        end_game()


def end_game():
    """
    遊戲結束處理。
    """
    global game_over
    game_over = True
    lbl_target.config(text="Game Over")


# ==========================================
# 3. 建立視窗與畫面配置 (GUI)
# ==========================================
root = tk.Tk()
root.title("打字消除遊戲 (基礎版)")

# 計算畫布大小
canvas_width = cell_size * grid_cols
canvas_height = cell_size * grid_rows

# 建立畫布 (Canvas)
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# 繪製背景的格線 (方便對齊)
for i in range(grid_cols + 1):
    canvas.create_line(i*cell_size, 0, i*cell_size, canvas_height, fill="gray")
for i in range(grid_rows + 1):
    canvas.create_line(0, i*cell_size, canvas_width, i*cell_size, fill="gray")
    
# 底部控制介面
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X, pady=2)

# 目標單字提示區
lbl_target = tk.Label(bottom_frame, text="", width=10, anchor="e")
lbl_target.pack(side=tk.LEFT)

# 輸入框
entry = tk.Entry(bottom_frame, width=15)
entry.pack(side=tk.LEFT, padx=5)
# 綁定 Enter 鍵觸發 check_input
entry.bind("<Return>", check_input)
# 讓游標自動跳到輸入框
entry.focus()

# 分數顯示區
lbl_score = tk.Label(bottom_frame, text=f"score: {score}", anchor="e")
lbl_score.pack(side=tk.RIGHT, padx=5)


# ==========================================
# 4. 啟動遊戲
# ==========================================
# 產生第一個目標單字
current_word = generate_word()
lbl_target.config(text=current_word)

# 開始產生方塊與下落動畫
spawn_block()
update_fall()

# 啟動事件迴圈
root.mainloop()
