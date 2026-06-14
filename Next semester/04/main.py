import tkinter as tk

# ==========================================
# 1. 宣告全域變數 (記錄遊戲的狀態)
# ==========================================
size = 3               # 棋盤大小，預設為 3 (代表 3x3 九宮格)
current_player = 0     # 記錄現在輪到哪位玩家 (0 代表玩家0，1 代表玩家1)
game_over = False      # 記錄遊戲是否已經結束
buttons = []           # 存放棋盤上所有的按鈕元件 (二維陣列)
symbols = ["O", "X"]   # 兩位玩家所使用的符號 (玩家0用 O，玩家1用 X)


# ==========================================
# 2. 定義遊戲邏輯與功能函式
# ==========================================
def create_board():
    """
    根據目前的 size (棋盤大小) 動態產生對應數量的按鈕，並畫到畫面上。
    """
    global buttons
    
    # 每次重新建立棋盤前，必須先清掉畫面舊有的按鈕，避免上一局的按鈕殘留在畫面上
    # winfo_children() 可以抓出 board_frame 裡面所有的元件
    for widget in board_frame.winfo_children():
        widget.destroy() # 銷毀元件

    buttons = [] # 清空按鈕陣列，準備重新存放新的按鈕

    # 利用雙層迴圈建立 size * size 個按鈕
    for r in range(size):
        row_buttons = [] # 用來裝同一列的所有按鈕
        for c in range(size):
            # 每個格子都建立一個 Button 元件
            # command=lambda 綁定點擊事件，讓按鈕被按下去時，能把自己的座標 (r, c) 傳給 on_click 函式
            btn = tk.Button(
                board_frame, 
                text="", 
                font=("Arial", 20), 
                width=4, 
                height=2,
                command=lambda row=r, col=c: on_click(row, col)
            )
            # 使用 grid 排版法放置按鈕
            btn.grid(row=r, column=c)
            # 將這個按鈕加入當前這一列的陣列中
            row_buttons.append(btn)
            
        # 將整列按鈕加入總按鈕陣列中，形成二維陣列
        buttons.append(row_buttons)


def on_click(r, c):
    """
    當玩家點擊棋盤上的某個格子時會觸發的函式
    :param r: 被點擊的格子位在第幾列
    :param c: 被點擊的格子位在第幾欄
    """
    global current_player, game_over

    # 若該格已經有下過符號了，或者是遊戲已經宣告結束，就直接忽略這次點擊 (return 中斷函式)
    if buttons[r][c]["text"] != "" or game_over:
        return

    # 取得目前玩家的符號 ("O" 或 "X")
    sym = symbols[current_player]
    # 將被點擊的那個按鈕的文字，設定為該玩家的符號
    buttons[r][c]["text"] = sym

    # 下完這步棋後，先檢查有沒有人勝利；如果沒有，再檢查是不是所有格子都滿了 (平手)
    if check_win(sym):
        label.config(text=f"玩家{current_player}獲得勝利") # 更新上方提示文字
        game_over = True # 設定遊戲結束
    elif check_draw():
        label.config(text="平手!!!遊戲結束!!!")
        game_over = True
    else:
        # 如果沒贏也沒平手，就交換玩家 (0 變 1，1 變 0)
        # 巧妙的算法： 1 - 0 = 1， 1 - 1 = 0
        current_player = 1 - current_player
        label.config(text=f"換玩家{current_player}了")


def check_win(sym):
    """
    檢查傳入的符號 (sym) 是否有連線獲勝
    :param sym: 要檢查的符號 ("O" 或 "X")
    :return: 獲勝回傳 True，沒獲勝回傳 False
    """
    # 檢查【橫排】是否整列都相同
    for i in range(size):
        win = True # 先假設這排贏了
        for j in range(size):
            if buttons[i][j]["text"] != sym:
                win = False # 只要有一個字元不一樣，就代表沒贏，提早中斷這排的檢查
                break
        if win:
            return True # 如果某排檢查完 win 還是 True，代表整排一樣，宣告勝利

    # 檢查【直排】是否整欄都相同
    for i in range(size):
        win = True
        for j in range(size):
            # 注意這裡中括號內是 [j][i]，代表固定第 i 欄，往下檢查每一列 (j)
            if buttons[j][i]["text"] != sym:
                win = False
                break
        if win:
            return True

    # 檢查【左上到右下】的主對角線 (特徵：行列座標數字一樣，例如 [0][0], [1][1], [2][2])
    win = True
    for i in range(size):
        if buttons[i][i]["text"] != sym:
            win = False
            break
    if win:
        return True

    # 檢查【右上到左下】的副對角線 (特徵：行與列座標相加等於 size-1)
    win = True
    for i in range(size):
        if buttons[i][size - 1 - i]["text"] != sym:
            win = False
            break
    if win:
        return True

    # 全部都檢查完還沒回傳 True，代表還沒人獲勝
    return False


def check_draw():
    """
    檢查是否平手 (所有格子都被填滿)
    """
    # 走訪所有的格子
    for r in range(size):
        for c in range(size):
            # 只要發現還有一個格子是空的，就代表還沒平手，回傳 False
            if buttons[r][c]["text"] == "":
                return False  
    # 全部都不是空的，代表滿了，回傳 True
    return True


def restart():
    """
    重新開始同一關卡的遊戲 (棋盤大小不變)
    """
    global current_player, game_over
    
    # 重設全域變數
    current_player = 0
    game_over = False
    
    # 更新標籤文字
    label.config(text="遊戲開始!!請玩家0先下")
    
    # 重新產生棋盤按鈕
    create_board()


def next_level():
    """
    進入下一關：將棋盤尺寸加大一格 (例如 3x3 變 4x4)，並重新開始遊戲
    """
    global size
    size += 1   # 將棋盤寬高加 1
    restart()   # 呼叫 restart 函式來重新初始化遊戲與畫面


# ==========================================
# 3. 建立視窗與畫面設計 (GUI)
# ==========================================
# 建立主視窗物件
root = tk.Tk()
root.title("進階版圈圈叉叉 (可無限擴大規模)")

# 在畫面上方放置一個標籤 (Label)，用來顯示目前的遊戲狀態或該誰下棋
# bg="yellow" 表示背景為黃色
label = tk.Label(
    root, 
    text="遊戲開始!!請玩家0先下", 
    bg="yellow",
    font=("Arial", 12), 
    height=2
)
label.pack(fill=tk.X) # fill=tk.X 表示在 X 軸 (水平方向) 填滿視窗

# 中間放置一個框架 (Frame)，用來裝所有的九宮格按鈕
board_frame = tk.Frame(root)
board_frame.pack()

# 下方放置一個框架，用來裝兩顆控制按鈕 (Restart / 下一關)
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X)

# 建立 Restart (重新開始) 按鈕
btn_restart = tk.Button(
    bottom_frame, 
    text="Restart",
    command=restart, # 綁定 restart 函式
    height=2
)
btn_restart.pack(side=tk.LEFT, expand=True, fill=tk.X)

# 建立「下一關」按鈕
btn_next = tk.Button(
    bottom_frame, 
    text="下一關", 
    command=next_level, # 綁定 next_level 函式
    height=2
)
btn_next.pack(side=tk.LEFT, expand=True, fill=tk.X)

# 遊戲啟動前，先呼叫 create_board 產生第一關 (3x3) 的棋盤
create_board()

# ==========================================
# 4. 啟動程式
# ==========================================
# 啟動視窗的事件迴圈，讓視窗保持開啟狀態，等待玩家互動
root.mainloop()
