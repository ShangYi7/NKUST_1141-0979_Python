import random
import tkinter as tk

# ==========================================
# 1. 設定全域變數 (遊戲參數)
# ==========================================
# 設定棋盤的大小為 10 x 10 (總共 100 格)
SIZE = 10

# 建立一個清單，包含 0 到 9 的數字，然後重複 10 次
# list(range(10)) 會產生 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 乘以 10 之後，陣列就會有 100 個元素 (每個數字出現 10 次，所以共有 50 組配對)
numbers = list(range(10)) * 10

# 使用 random 模組將 list 裡面的順序隨機打亂，這樣按鈕背後的數字才會是隨機的
random.shuffle(numbers)

# 存放所有建立出來的按鈕元件，方便後續透過迴圈去修改它們的狀態
buttons = []
# 記錄玩家點擊的「第一格」的座標 (row, col)，用來跟第二次點擊做比對。初始為 None 代表還沒點。
first_pick = None
# 記錄還有多少組配對沒有完成，初始為 50 組
remain = 50


# ==========================================
# 2. 遊戲主要邏輯 (點擊按鈕時觸發的事件)
# ==========================================
def on_click(row, col):
    """
    當玩家點下棋盤中某個按鈕時會呼叫此函式
    :param row: 點擊的按鈕位在第幾列
    :param col: 點擊的按鈕位在第幾欄
    """
    # 宣告我們要修改全域變數
    global first_pick, remain

    # 先取得玩家點擊的那個按鈕元件
    button = buttons[row][col]
    
    # 判斷：如果這個按鈕已經被配對成功，狀態會是 "disabled" (被鎖定停用)
    # 這種按鈕不能再點，直接結束函式
    if button["state"] == "disabled":
        return

    # 判斷：如果是這回合的「第一次」點擊
    if first_pick is None:
        # 把這格的座標記錄下來，然後直接結束函式，等待玩家點擊第二個格子
        first_pick = (row, col)
        return

    # 判斷：如果玩家這回合「第二次」點擊的格子，跟第一次點擊的格子完全一樣 (也就是連點同一個格子兩次)
    if first_pick == (row, col):
        # 不算數，直接結束函式
        return

    # 走到這裡，代表玩家點了第二個「不一樣」的格子，我們準備開始比對
    r1, c1 = first_pick # 取出第一次點擊的座標
    r2, c2 = row, col   # 取出第二次點擊的座標

    # 比對兩格背後的數字是否相同
    # 由於 numbers 是一維陣列，我們必須用 (列 * 總列數 + 欄) 換算出陣列的索引位置
    index1 = r1 * SIZE + c1
    index2 = r2 * SIZE + c2
    
    if numbers[index1] == numbers[index2]:
        # 如果兩個數字相同，代表配對成功！
        # 將這兩個按鈕鎖定停用 (state="disabled")
        buttons[r1][c1].config(state="disabled")
        buttons[r2][c2].config(state="disabled")
        
        # 剩餘配對數減 1
        remain -= 1
        # 更新畫面上方的剩餘數量文字
        status.config(text=f"剩餘配對數: {remain}")
        
        # 如果剩餘配對數變成 0，代表遊戲破關
        if remain == 0:
            status.config(text="恭喜完成所有配對！")

    # 無論這回合有沒有配對成功，都把 first_pick 清空，準備迎接下一輪新的點擊
    first_pick = None


# ==========================================
# 3. 建立棋盤介面函式
# ==========================================
def create_board():
    """
    依照亂數序列，建立 10 x 10 的按鈕棋盤並放置到畫面上
    """
    global buttons
    
    for row in range(SIZE):
        row_buttons = [] # 用來裝每一列的 10 個按鈕
        for col in range(SIZE):
            # 計算一維陣列的索引值
            index = row * SIZE + col
            
            # 建立一個按鈕，文字內容直接顯示打亂後的數字 (作弊版配對，給初學者看原理用的)
            button = tk.Button(
                board,
                text=str(numbers[index]), # 直接顯示數字
                width=3,
                height=1,
                font=("Arial", 12),
                # 綁定點擊事件，並傳遞自己的 (row, col)
                command=lambda r=row, c=col: on_click(r, c),
            )
            # 使用 grid 將按鈕排成方陣
            button.grid(row=row, column=col, padx=1, pady=1)
            row_buttons.append(button) # 把按鈕加到該列的陣列中
            
        # 把這列的陣列加到整體的 buttons 陣列中
        buttons.append(row_buttons)


# ==========================================
# 4. 建立主視窗與介面排版
# ==========================================
# 建立主視窗
root = tk.Tk()
root.title("配對遊戲")
root.resizable(False, False) # 鎖定視窗大小

# 建立一個棋盤區 (Frame)，專門用來放 100 個按鈕
board = tk.Frame(root, padx=6, pady=6)
board.pack()

# 建立標籤 (Label)，用來顯示目前的剩餘配對數量
status = tk.Label(root, text=f"剩餘配對數: {remain}", font=("Arial", 12))
status.pack(pady=(0, 8)) # 底部留白 8 像素

# 呼叫函式建立棋盤按鈕
create_board()

# ==========================================
# 5. 啟動程式
# ==========================================
# 讓視窗保持顯示並開始監聽滑鼠鍵盤動作
root.mainloop()
