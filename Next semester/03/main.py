import tkinter as tk
from tkinter import messagebox

# ==========================================
# 1. 定義全域變數 (記錄遊戲的狀態)
# ==========================================
# 棋盤用 9 個空字串表示，索引 0 到 8 對應 3x3 的方格
board = [''] * 9
# 設定先手玩家為 'O'
current_player = 'O'
# 記錄遊戲是否已經結束 (若為 True 則不允許再下棋)
game_over = False
# 用來存放畫面上 9 個按鈕元件的串列，方便後續透過迴圈去修改按鈕的文字與狀態
buttons = []


# ==========================================
# 2. 定義遊戲邏輯與相關函式
# ==========================================
def click_button(index):
    """
    處理玩家點擊棋盤格子的事件
    :param index: 被點擊的格子編號 (0 到 8)
    """
    # 宣告我們要修改的是全域變數 (因為遊戲狀態需要持續被記憶下來)
    global current_player, game_over

    # 如果遊戲已經結束，就跳出警告視窗，並且中斷這個函式的執行 (return)
    if game_over:
        messagebox.showwarning("遊戲結束", "遊戲已結束，請按重新開始")
        return

    # 如果被點擊的格子不是空的 (已經有 'O' 或 'X')，代表不能重複下，給予警告
    if board[index] != '':
        messagebox.showwarning("無效操作", "該方格已被佔用")
        return

    # 將目前玩家的標記 ('O' 或是 'X') 寫入全域變數 board 的對應位置中
    board[index] = current_player
    # 同步更新畫面上的按鈕：顯示玩家標記，並設定狀態為 "disabled" 讓它不能再被點擊
    buttons[index].config(text=current_player, state="disabled")

    # 檢查是否因為這一步棋而連線獲勝
    if check_winner():
        game_over = True  # 遊戲結束
        # 更新上方的狀態文字與背景顏色
        status_label.config(
            text=f"玩家 {current_player} 獲勝！",
            bg="lightgreen"
        )
        disable_all_buttons()  # 把剩下的格子都鎖起來
        return  # 獲勝後就不需要檢查平手或換人，直接結束函式

    # 如果沒有獲勝，再檢查是否所有格子都被填滿 (平手)
    if check_draw():
        game_over = True
        status_label.config(text="平手！", bg="lightcoral")
        disable_all_buttons()
        return

    # 若遊戲還沒結束 (沒贏也沒平手)，就換另一位玩家回合
    if current_player == 'O':
        current_player = 'X'
    else:
        current_player = 'O'
        
    # 更新上方的提示文字，告訴玩家現在換誰了
    status_label.config(text=f"玩家 {current_player} 的回合")


def check_winner():
    """
    檢查目前玩家是否達成任一勝利條件 (三點連線)
    :return: True 代表獲勝，False 代表沒獲勝
    """
    # 定義所有可能的獲勝連線組合 (3 條橫排、3 條直排、2 條對角線，共 8 種)
    win_combinations = [
        [0, 1, 2],  # 第一行
        [3, 4, 5],  # 第二行
        [6, 7, 8],  # 第三行
        [0, 3, 6],  # 第一列
        [1, 4, 7],  # 第二列
        [2, 5, 8],  # 第三列
        [0, 4, 8],  # 左上到右下的對角線
        [2, 4, 6],  # 右上到左下的對角線
    ]

    # 使用迴圈檢查這 8 種連線組合
    for combo in win_combinations:
        # 如果某個連線組合的三個位置，存放的內容都一樣，且等於「目前玩家的符號」
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == current_player:
            return True  # 只要有一組達成連線，就回傳 True (獲勝)
            
    # 如果 8 組都檢查完還沒獲勝，就回傳 False
    return False


def check_draw():
    """
    檢查是否平手 (當棋盤沒有空字串時視為平手)
    :return: True 代表平手，False 代表還沒平手
    """
    # 檢查 board 裡面的每一個格子，如果發現還有空字串 ''，就代表還有格子可以下，回傳 False
    for cell in board:
        if cell == '':
            return False
    # 如果迴圈跑完都沒發現空字串，就代表填滿了，回傳 True
    return True


def disable_all_buttons():
    """
    比賽結束後，將畫面上所有的格子都鎖定，避免玩家繼續點擊
    """
    for btn in buttons:
        btn.config(state="disabled")


def restart_game():
    """
    重設所有變數與畫面狀態，重新開始一局新遊戲
    """
    global board, current_player, game_over
    
    # 1. 變數狀態回歸預設值
    board = [''] * 9
    current_player = 'O'
    game_over = False
    
    # 2. 畫面上方的提示文字恢復預設
    status_label.config(text="玩家 O 的回合", bg="yellow")

    # 3. 把畫面上的 9 個按鈕清空，並解除鎖定 (狀態設為 "normal")
    for btn in buttons:
        btn.config(text='', state="normal", bg="lightgray")


# ==========================================
# 3. 建立圖形介面 (GUI)
# ==========================================
windows = tk.Tk()
windows.title("圓圈叉叉遊戲")
windows.geometry("400x500")
windows.resizable(False, False)  # 禁止調整視窗大小

# 建立上方狀態列，用來顯示輪到誰或比賽結果
status_label = tk.Label(
    windows,
    text="玩家 O 的回合",
    font=("Arial", 16, "bold"),
    bg="yellow",
    fg="black",
    pady=10
)
status_label.pack(fill=tk.X)  # fill=tk.X 讓標籤在水平方向填滿

# 建立棋盤的框架 (Frame)，所有的按鈕都會放在這裡面
board_frame = tk.Frame(windows, bg="black", padx=5, pady=5)
board_frame.pack(pady=20)

# 使用迴圈建立 3x3 棋盤按鈕
for i in range(9):
    # 建立按鈕元件
    btn = tk.Button(
        board_frame,
        text='',
        font=("Arial", 24, "bold"),
        width=6,
        height=2,
        # 重點：使用 lambda 函式將這個按鈕對應的索引編號 (i) 綁定到 click_button 函式
        command=lambda idx=i: click_button(idx),
        bg="lightgray",
        activebackground="white"
    )
    # 計算這個格子應該放在第幾列(row)與第幾欄(col)
    row = i // 3  # 例如 i=4，4除以3的商數為1，代表放在第1列 (從0開始算)
    col = i % 3   # 例如 i=4，4除以3的餘數為1，代表放在第1欄 (從0開始算)
    
    # 把按鈕放在框架中指定的網格位置
    btn.grid(row=row, column=col, padx=2, pady=2)
    
    # 將這個按鈕存入全域變數 buttons 串列中，以便後續可以修改它
    buttons.append(btn)

# 建立下方控制區，放重新開始按鈕
bottom_frame = tk.Frame(windows)
bottom_frame.pack(pady=10)

restart_btn = tk.Button(
    bottom_frame,
    text="重新開始",
    font=("Arial", 12),
    command=restart_game, # 點擊時呼叫 restart_game 函式
    bg="lightgreen",
    padx=20,
    pady=5
)
restart_btn.pack()

# ==========================================
# 4. 啟動程式
# ==========================================
windows.mainloop()
