import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("圓圈叉叉遊戲")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # 遊戲狀態
        self.board = [''] * 9  # 0-8 代表9個方格
        self.current_player = 'O'  # O 先手
        self.game_over = False

        # 創建上方狀態標籤
        self.status_label = tk.Label(
            root,
            text="玩家 O 的回合",
            font=("Arial", 16, "bold"),
            bg="yellow",
            fg="black",
            pady=10
        )
        self.status_label.pack(fill=tk.X)

        # 創建棋盤框架
        self.board_frame = tk.Frame(root, bg="black", padx=5, pady=5)
        self.board_frame.pack(pady=20)

        # 創建按鈕
        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                self.board_frame,
                text='',
                font=("Arial", 24, "bold"),
                width=6,
                height=2,
                command=lambda idx=i: self.click_button(idx),
                bg="lightgray",
                activebackground="white"
            )
            row = i // 3
            col = i % 3
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append(btn)

        # 創建按鈕框架
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(pady=10)

        # 重新開始按鈕
        restart_btn = tk.Button(
            bottom_frame,
            text="重新開始",
            font=("Arial", 12),
            command=self.restart_game,
            bg="lightgreen",
            padx=20,
            pady=5
        )
        restart_btn.pack()

    def click_button(self, index):
        """處理按鈕點擊"""
        if self.game_over:
            messagebox.showwarning("遊戲結束", "遊戲已結束，請按重新開始")
            return

        if self.board[index] != '':
            messagebox.showwarning("無效操作", "該方格已被佔用")
            return

        # 更新棋盤和按鈕
        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player, state="disabled")

        # 檢查勝負
        if self.check_winner():
            self.game_over = True
            self.status_label.config(
                text=f"玩家 {self.current_player} 獲勝！",
                bg="lightgreen"
            )
            self.disable_all_buttons()
            return

        # 檢查平手
        if self.check_draw():
            self.game_over = True
            self.status_label.config(text="平手！", bg="lightcoral")
            self.disable_all_buttons()
            return

        # 切換玩家
        self.current_player = 'X' if self.current_player == 'O' else 'O'
        self.status_label.config(text=f"玩家 {self.current_player} 的回合")

    def check_winner(self):
        """檢查是否有贏家"""
        # 所有可能的勝利組合
        win_combinations = [
            [0, 1, 2],  # 第一行
            [3, 4, 5],  # 第二行
            [6, 7, 8],  # 第三行
            [0, 3, 6],  # 第一列
            [1, 4, 7],  # 第二列
            [2, 5, 8],  # 第三列
            [0, 4, 8],  # 左上到右下
            [2, 4, 6],  # 右上到左下
        ]

        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] ==
                    self.board[combo[2]] == self.current_player):
                return True
        return False

    def check_draw(self):
        """檢查是否平手"""
        return all(cell != '' for cell in self.board)

    def disable_all_buttons(self):
        """禁用所有按鈕"""
        for btn in self.buttons:
            btn.config(state="disabled")

    def restart_game(self):
        """重新開始遊戲"""
        self.board = [''] * 9
        self.current_player = 'O'
        self.game_over = False
        self.status_label.config(text="玩家 O 的回合", bg="yellow")

        for btn in self.buttons:
            btn.config(text='', state="normal", bg="lightgray")


# 主程式
if __name__ == "__main__":
    windows = tk.Tk()
    game = TicTacToe(windows)
    windows.mainloop()
