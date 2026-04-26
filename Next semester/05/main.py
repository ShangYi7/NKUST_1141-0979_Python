import random
import tkinter as tk


# 10 x 10 棋盤，共 100 格，每個數字出現 10 次
SIZE = 10
# 0~9 各出現 10 次，所以總共有 50 組配對
numbers = list(range(10)) * 10
random.shuffle(numbers)

# 存放所有按鈕，方便後續統一更新狀態
buttons = []
# 記錄第一次點擊的位置，用來和第二次點擊做比對
first_pick = None
# 剩餘配對數
remain = 50


def on_click(row, col):
    global first_pick, remain

    button = buttons[row][col]
    # 已經配對成功的按鈕不能再點
    if button["state"] == "disabled":
        return

    # 第一次點擊只記錄座標，不做比對
    if first_pick is None:
        first_pick = (row, col)
        return

    # 不處理同一格被連點兩次
    if first_pick == (row, col):
        return

    # 第二次點擊後開始比對兩格是否相同
    r1, c1 = first_pick
    r2, c2 = row, col

    # 兩個數字相同就判定成功，並鎖定這兩個按鈕
    if numbers[r1 * SIZE + c1] == numbers[r2 * SIZE + c2]:
        buttons[r1][c1].config(state="disabled")
        buttons[r2][c2].config(state="disabled")
        remain -= 1
        status.config(text=f"剩餘配對數: {remain}")
        if remain == 0:
            status.config(text="完成！")

    # 清空第一次點擊，準備下一輪
    first_pick = None


def create_board():
    # 依照亂數序列建立 10 x 10 的按鈕棋盤
    for row in range(SIZE):
        row_buttons = []
        for col in range(SIZE):
            index = row * SIZE + col
            button = tk.Button(
                board,
                text=str(numbers[index]),
                width=3,
                height=1,
                font=("Arial", 12),
                command=lambda r=row, c=col: on_click(r, c),
            )
            button.grid(row=row, column=col, padx=1, pady=1)
            row_buttons.append(button)
        buttons.append(row_buttons)


root = tk.Tk()
root.title("配對遊戲")
root.resizable(False, False)

# 棋盤區
board = tk.Frame(root, padx=6, pady=6)
board.pack()

# 顯示剩餘配對數，讓玩家知道目前進度
status = tk.Label(root, text=f"剩餘配對數: {remain}", font=("Arial", 12))
status.pack(pady=(0, 8))

create_board()

root.mainloop()
