import tkinter as tk

n = int(input("請輸入非負整數 N："))

rows = []
for i in range(n + 1):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(rows[i - 1][j - 1] + rows[i - 1][j])
    rows.append(row)

max_value = rows[-1][len(rows[-1]) // 2] if rows else 1
cell_width = len(str(max_value)) + 2

window = tk.Tk()
window.title("Pascal Triangle")
window.geometry("1000x750+10+10")

frame = tk.Frame(window, padx=20, pady=20)
frame.pack(expand=True)

# 總欄數固定為 2N+1，將每層數字放在對稱欄位上
total_cols = 2 * n + 1
for c in range(total_cols):
    frame.grid_columnconfigure(c, weight=1)

for i, row in enumerate(rows):
    for j, value in enumerate(row):
        col = n - i + 2 * j
        tk.Label(
            frame,
            text=str(value).center(cell_width),
            font=("Consolas", 14),
        ).grid(row=i, column=col, padx=2, pady=2)

window.mainloop()
