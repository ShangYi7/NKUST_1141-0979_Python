import tkinter as tk  # 匯入 tkinter 模組，並縮寫為 tk，用於建立圖形介面

# ==========================================
# 1. 建立計算機視窗與顯示框
# ==========================================
window = tk.Tk()                    # 建立一個主視窗物件
window.title("Calculator")          # 設定視窗標題
window.geometry("260x360+100+100")  # 設定視窗大小為寬260x高360，並設定出現在螢幕的座標位置
window.resizable(False, False)      # 設定視窗不能被改變大小 (禁止改變寬度和高度)

# 建立一個 Entry (輸入框) 用來顯示目前的輸入內容與運算結果
# justify="right" 表示文字靠右對齊
# bd=8 表示邊框寬度為 8，relief="sunken" 讓輸入框有凹陷的立體感
display = tk.Entry(window, justify="right", font=("Consolas", 18), bd=8, relief="sunken")
# 使用 grid() 排版方式將輸入框放置在第 0 列、第 0 欄，並且跨越 4 個欄位 (columnspan=4)
# sticky="nsew" 代表向四周對齊填滿，padx 和 pady 分別是水平和垂直的留白
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=6, pady=6)

# 為了讓按鈕區域在視窗內平均分配空間，我們設定每一列(row)和每一欄(column)的權重 (weight)
for r in range(1, 6):
    window.grid_rowconfigure(r, weight=1)  # 設定第 1 到 5 列的權重
for c in range(4):
    window.grid_columnconfigure(c, weight=1) # 設定第 0 到 3 欄的權重


# ==========================================
# 2. 定義按鈕點擊後要執行的功能
# ==========================================
def click(key):
    """
    處理按鈕點擊事件的函式
    :param key: 被點擊的按鈕文字 (例如 "1", "+", "C", "=")
    """
    if key == "C":
        # 如果按下的按鈕是 "C" (Clear)，就清空顯示框的內容
        # 0 代表從第一個字元開始，tk.END 代表到最後一個字元
        display.delete(0, tk.END)
        
    elif key == "=":
        # 如果按下的按鈕是 "="，則嘗試計算輸入框內的數學算式
        try:
            # 取得輸入框內的文字
            text = display.get()
            # 使用 Python 內建的 eval() 函式來直接計算這個數學字串的結果
            result = eval(text)
            # 顯示結果前先清空輸入框
            display.delete(0, tk.END)
            # 將算出來的結果插入到輸入框的最後面
            display.insert(tk.END, result)
        except Exception:
            # 如果算式有錯 (例如 1/0 或是語法不對)，就顯示 "Error"
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
            
    else:
        # 如果按下的是數字或加減乘除符號，就直接將該字元加到輸入框的最後面
        display.insert(tk.END, key)


# ==========================================
# 3. 建立輔助函式，方便快速產生按鈕
# ==========================================
def add_btn(text, row, col, rowspan=1, colspan=1):
    """
    在畫面上產生一個按鈕
    :param text: 按鈕上要顯示的文字
    :param row: 按鈕所在的列 (Y 軸位置)
    :param col: 按鈕所在的欄 (X 軸位置)
    :param rowspan: 按鈕要跨越幾列 (預設為 1)
    :param colspan: 按鈕要跨越幾欄 (預設為 1)
    """
    # 建立一個按鈕物件
    # command=lambda: click(text) 表示當按鈕被點擊時，會呼叫我們上面定義的 click 函式，並把自己的文字傳進去
    btn = tk.Button(
        window,
        text=text,
        font=("Consolas", 14),
        command=lambda: click(text)
    )
    # 使用 grid 排版法，將按鈕放到指定的位置
    btn.grid(
        row=row,
        column=col,
        rowspan=rowspan,
        columnspan=colspan,
        sticky="nsew",  # 讓按鈕向上下左右填滿它所在的格子
        padx=1,         # 按鈕之間的水平間距
        pady=1          # 按鈕之間的垂直間距
    )


# ==========================================
# 4. 依照計算機的排列方式，呼叫函式建立所有按鍵
# ==========================================
# 第一排 (列號為 1)
add_btn("C", 1, 0)
add_btn("/", 1, 1)
add_btn("*", 1, 2)
add_btn("-", 1, 3)

# 第二排 (列號為 2)
add_btn("7", 2, 0)
add_btn("8", 2, 1)
add_btn("9", 2, 2)
# 加號跨越兩列，所以設定 rowspan=2
add_btn("+", 2, 3, rowspan=2)

# 第三排 (列號為 3)
add_btn("4", 3, 0)
add_btn("5", 3, 1)
add_btn("6", 3, 2)
# 第 3 欄已經被上面的 "+" 號跨越佔用了，所以這一排沒有第 3 欄的按鈕

# 第四排 (列號為 4)
add_btn("1", 4, 0)
add_btn("2", 4, 1)
add_btn("3", 4, 2)
# 等號跨越兩列，設定 rowspan=2
add_btn("=", 4, 3, rowspan=2)

# 第五排 (列號為 5)
# 數字 0 跨越兩欄，設定 colspan=2
add_btn("0", 5, 0, colspan=2)
add_btn(".", 5, 2)
# 第 3 欄已經被上面的 "=" 號跨越佔用了

# ==========================================
# 5. 啟動程式
# ==========================================
# 啟動 GUI 事件迴圈，開始監聽使用者的按鈕點擊等操作
window.mainloop()
