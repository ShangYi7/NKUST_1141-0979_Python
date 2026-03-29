import tkinter as tk

n = int(input("請輸入非負整數 N："))

# --- 1. 計算帕斯卡三角形的數字 ---
rows = []
for i in range(n + 1):
    row = []
    for j in range(i + 1):
        # 邊緣的數字都是 1
        if j == 0 or j == i:
            row.append(1)
        # 中間的數字 = 上一層的左上角 + 上一層的右上角
        else:
            row.append(rows[i - 1][j - 1] + rows[i - 1][j])
    rows.append(row)

# --- 2. 建立圖形介面 (GUI) ---
window = tk.Tk()
window.title("帕斯卡三角形")
window.geometry("800x600")  # 設定視窗大小

# --- 3. 把數字畫到畫面上 ---
for row in rows:
    # 每一層建立一個「框架」(Frame)，預設 pack() 會自動將它置中
    row_frame = tk.Frame(window)
    row_frame.pack(pady=2)

    for value in row:
        # 把每個數字放進「標籤」(Label) 中
        lbl = tk.Label(
            row_frame,
            text=str(value),
            font=("Arial", 14),
            width=4  # 設定固定寬度，讓數字排列更整齊
        )
        # 把標籤由左到右排進框架裡
        lbl.pack(side="left", padx=2)

window.mainloop()
