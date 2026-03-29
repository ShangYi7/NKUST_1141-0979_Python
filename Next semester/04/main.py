import tkinter as tk

# === 全局變數 ===
size = 3
current_player = 0
game_over = False
buttons = []
symbols = ["O", "X"]

# === 遊戲功能函數 ===
def create_board():
    global buttons
    # 每次產生新盤面前，先清空原本的按鈕
    for widget in board_frame.winfo_children():
        widget.destroy()
    
    buttons = []
    for r in range(size):
        row_buttons = []
        for c in range(size):
            # 建立按鈕
            btn = tk.Button(board_frame, text="", font=("Arial", 20), width=4, height=2,
                            command=lambda row=r, col=c: on_click(row, col))
            btn.grid(row=r, column=c)
            row_buttons.append(btn)
        buttons.append(row_buttons)

def on_click(r, c):
    global current_player, game_over

    # 如果已經有字，或是遊戲結束，就不做任何事
    if buttons[r][c]["text"] != "" or game_over:
        return

    # 在按鈕上寫字
    sym = symbols[current_player]
    buttons[r][c]["text"] = sym

    # 檢查是否有人贏了或是平手
    if check_win(sym):
        label.config(text=f"玩家{current_player}獲得勝利")
        game_over = True
    elif check_draw():
        label.config(text="平手!!!遊戲結束!!!")
        game_over = True
    else:
        # 換下一位玩家 (把 0 變 1，把 1 變 0)
        current_player = 1 - current_player
        label.config(text=f"換玩家{current_player}了")

def check_win(sym):
    # 1. 檢查橫排
    for i in range(size):
        win = True
        for j in range(size):
            if buttons[i][j]["text"] != sym:
                win = False
                break
        if win: return True

    # 2. 檢查直排
    for i in range(size):
        win = True
        for j in range(size):
            if buttons[j][i]["text"] != sym:
                win = False
                break
        if win: return True

    # 3. 檢查左上到右下的對角線
    win = True
    for i in range(size):
        if buttons[i][i]["text"] != sym:
            win = False
            break
    if win: return True

    # 4. 檢查右上到左下的對角線
    win = True
    for i in range(size):
        if buttons[i][size - 1 - i]["text"] != sym:
            win = False
            break
    if win: return True

    return False

def check_draw():
    # 檢查是不是全部格子都滿了
    for r in range(size):
        for c in range(size):
            if buttons[r][c]["text"] == "":
                return False  # 還有空格，不是平手
    return True

def restart():
    global current_player, game_over
    current_player = 0
    game_over = False
    label.config(text="遊戲開始!!請玩家0先下")
    create_board()

def next_level():
    global size
    size += 1
    restart()

# === 畫面設計設定 ===
# 建立主視窗
root = tk.Tk()
root.title("tk")

# 上方黃色標籤
label = tk.Label(root, text="遊戲開始!!請玩家0先下", bg="yellow", font=("Arial", 12), height=2)
label.pack(fill=tk.X)

# 中間的九宮格框架
board_frame = tk.Frame(root)
board_frame.pack()

# 下方的按鈕框架
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X)

btn_restart = tk.Button(bottom_frame, text="Restart", command=restart, height=2)
btn_restart.pack(side=tk.LEFT, expand=True, fill=tk.X)

btn_next = tk.Button(bottom_frame, text="下一關", command=next_level, height=2)
btn_next.pack(side=tk.LEFT, expand=True, fill=tk.X)

# 遊戲開始，產生第一關棋盤
create_board()

# 啟動視窗迴圈
root.mainloop()
