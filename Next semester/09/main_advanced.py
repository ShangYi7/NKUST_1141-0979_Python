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
    return "".join(random.choices(string.ascii_lowercase, k=word_length))


def spawn_block():
    """
    從最上方隨機一欄產生掉落方塊。
    """
    global blocks_dropped
    
    if blocks_dropped >= max_blocks or game_over:
        return
        
    col = random.randint(0, grid_cols - 1)
    
    x1 = col * cell_size
    y1 = 0
    x2 = x1 + cell_size
    y2 = cell_size
    
    rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
    
    blocks.append(rect_id)
    blocks_dropped += 1
        
    next_spawn_time = random.randint(spawn_min_time, spawn_max_time)
    root.after(next_spawn_time, spawn_block)


def update_fall():
    """
    方塊的下落邏輯更新循環。
    """
    global blocks
    
    if game_over: 
        return
    
    remaining_blocks = []
    canvas_height = cell_size * grid_rows
    
    for rect_id in blocks:
        canvas.move(rect_id, 0, fall_pixels)
        coords = canvas.coords(rect_id)
        
        if coords and coords[1] < canvas_height:
            remaining_blocks.append(rect_id) 
        else:
            canvas.delete(rect_id)
            
    blocks = remaining_blocks
        
    if blocks_dropped >= max_blocks and not blocks:
        end_game()
        return
        
    root.after(fall_interval, update_fall)


def check_input(event):
    """
    驗證使用者的輸入內容。
    進階版：加入答錯懲罰機制 (扣分並加快方塊掉落速度)。
    """
    global score, current_word, fall_pixels
    
    if game_over: 
        return
        
    typed_word = entry.get().strip()
    entry.delete(0, tk.END)
    
    if typed_word == current_word:
        # 輸入正確
        best_idx = -1
        max_y = -1
        
        for i, rect_id in enumerate(blocks):
            coords = canvas.coords(rect_id)
            if coords and coords[3] > max_y:
                max_y = coords[3]
                best_idx = i
                
        if best_idx != -1:
            rect_id = blocks.pop(best_idx)
            canvas.delete(rect_id)
            
            score += 1
            lbl_score.config(text=f"score: {score}")
            
        current_word = generate_word()
        lbl_target.config(text=current_word)
        
    else:
        # 【進階版】答錯懲罰 (扣分且加快掉落速度)
        if score > 0:
            score -= 1  # 扣一分
        lbl_score.config(text=f"score: {score}")
        
        # 掉落速度加快 2 像素，讓遊戲越來越難！
        fall_pixels += 2  
            
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
root.title("打字消除遊戲 (進階版：答錯懲罰)")

canvas_width = cell_size * grid_cols
canvas_height = cell_size * grid_rows

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

for i in range(grid_cols + 1):
    canvas.create_line(i*cell_size, 0, i*cell_size, canvas_height, fill="gray")
for i in range(grid_rows + 1):
    canvas.create_line(0, i*cell_size, canvas_width, i*cell_size, fill="gray")
    
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X, pady=2)

lbl_target = tk.Label(bottom_frame, text="", width=10, anchor="e")
lbl_target.pack(side=tk.LEFT)

entry = tk.Entry(bottom_frame, width=15)
entry.pack(side=tk.LEFT, padx=5)
entry.bind("<Return>", check_input)
entry.focus()

lbl_score = tk.Label(bottom_frame, text=f"score: {score}", anchor="e")
lbl_score.pack(side=tk.RIGHT, padx=5)


# ==========================================
# 4. 啟動遊戲
# ==========================================
current_word = generate_word()
lbl_target.config(text=current_word)

spawn_block()
update_fall()

root.mainloop()
