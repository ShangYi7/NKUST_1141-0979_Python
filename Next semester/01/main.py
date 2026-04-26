import tkinter as tk

# 讀入要產生的帕斯卡三角形層數
n = int(input("請輸入非負整數 N："))

# --- 1. 計算帕斯卡三角形的數字 ---
rows = []
for i in range(n + 1):
    row = []
    for j in range(i + 1):
        # 每一列的最左邊與最右邊一定是 1
        if j == 0 or j == i:
            row.append(1)
        # 中間的數字等於上一列相鄰兩個數字的和
        else:
            row.append(rows[i - 1][j - 1] + rows[i - 1][j])
    rows.append(row)

# --- 2. 建立圖形介面 (GUI) ---
window = tk.Tk()
window.title("帕斯卡三角形")
window.geometry("800x600")  # 設定視窗大小

# --- 3. 把數字畫到畫面上 ---
for row in rows:
    # 每一列用一個 Frame 包起來，方便水平排列
    row_frame = tk.Frame(window)
    row_frame.pack(pady=2)

    for value in row:
        # 用 Label 顯示每個數字，並固定寬度讓排版整齊
        lbl = tk.Label(
            row_frame,
            text=str(value),
            font=("Arial", 14),
            width=4  # 設定固定寬度，讓數字排列更整齊
        )
        # 由左到右放入同一列
        lbl.pack(side="left", padx=2)

# 啟動 GUI 事件迴圈
window.mainloop()
