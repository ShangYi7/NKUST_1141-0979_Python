import tkinter as tk

# 建立計算機視窗與顯示框
window = tk.Tk()
window.title("Calculator")
window.geometry("260x360+100+100")
window.resizable(False, False)

# 顯示目前輸入與運算結果
display = tk.Entry(window, justify="right", font=(
    "Consolas", 18), bd=8, relief="sunken")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=6, pady=6)

# 讓按鈕區域在視窗縮放時保持平均分配
for r in range(1, 6):
    window.grid_rowconfigure(r, weight=1)
for c in range(4):
    window.grid_columnconfigure(c, weight=1)


def click(key):
    # C 清除顯示內容，= 進行運算，其餘按鍵直接追加到輸入框
    if key == "C":
        display.delete(0, tk.END)
    elif key == "=":
        try:
            # 直接使用 eval 計算簡單算式
            text = display.get()
            result = eval(text)
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception:
            # 運算失敗時顯示錯誤訊息
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, key)


def add_btn(text, row, col, rowspan=1, colspan=1):
    # 統一建立按鈕，避免重複寫太多相同程式
    tk.Button(
        window,
        text=text,
        font=("Consolas", 14),
        command=lambda: click(text),
    ).grid(
        row=row,
        column=col,
        rowspan=rowspan,
        columnspan=colspan,
        sticky="nsew",
        padx=1,
        pady=1,
    )


# 依照計算機排列建立按鍵
add_btn("C", 1, 0)
add_btn("/", 1, 1)
add_btn("*", 1, 2)
add_btn("-", 1, 3)

add_btn("7", 2, 0)
add_btn("8", 2, 1)
add_btn("9", 2, 2)
add_btn("+", 2, 3, rowspan=2)

add_btn("4", 3, 0)
add_btn("5", 3, 1)
add_btn("6", 3, 2)

add_btn("1", 4, 0)
add_btn("2", 4, 1)
add_btn("3", 4, 2)
add_btn("=", 4, 3, rowspan=2)

add_btn("0", 5, 0, colspan=2)
add_btn(".", 5, 2)

# 啟動 GUI 事件迴圈
window.mainloop()
