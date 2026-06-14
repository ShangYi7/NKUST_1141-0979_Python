# Python Tkinter 零基礎到實戰完整指南

由於原本的 PPT 涵蓋的內容較為精簡，這份文件將為你提供一份**非常完整且深入**的 Tkinter 教學。無論你是剛接觸 GUI (圖形化使用者介面) 程式設計，還是想解決作業中遇到的排版與互動問題，這份筆記都能成為你最強大的字典。

---

## 📖 目錄

1. [Tkinter 的運作原理與生命週期](#1-tkinter-的運作原理與生命週期)
2. [視窗的基礎設定](#2-視窗的基礎設定)
3. [三大佈局管理員 (Layout Managers) 深入解析](#3-三大佈局管理員-layout-managers-深入解析)
4. [基礎元件與屬性 (Widgets)](#4-基礎元件與屬性-widgets)
5. [Tkinter 專屬變數 (Variables)](#5-tkinter-專屬變數-variables)
6. [進階輸入元件 (Radiobutton, OptionMenu, Checkbutton)](#6-進階輸入元件-radiobutton-optionmenu-checkbutton)
7. [事件綁定與回呼函式 (Events & Callbacks)](#7-事件綁定與回呼函式-events--callbacks)
8. [計時器與非同步操作 (root.after)](#8-計時器與非同步操作-rootafter)
9. [彈出視窗與對話框 (Messagebox)](#9-彈出視窗與對話框-messagebox)
10. [畫布元件 (Canvas) 與繪圖](#10-畫布元件-canvas-與繪圖)
11. [在 Tkinter 中使用圖片 (PIL / Pillow)](#11-在-tkinter-中使用圖片-pil--pillow)

---

## 1. Tkinter 的運作原理與生命週期

撰寫任何 Tkinter 程式，都必然遵循以下四個步驟：

```python
import tkinter as tk

# 【步驟一】 建立主視窗 (Root Window)
# 這是所有元件的「地基」或「畫布」
root = tk.Tk()

# 【步驟二】 建立並設定元件 (Widgets)
# 所有的按鈕、文字框等元件，在建立時第一個參數都必須告訴它「你要放在哪裡」(通常是 root)
my_label = tk.Label(root, text="哈囉！")

# 【步驟三】 佈局 (Layout)
# 建立好的元件並不會自動顯示，必須告訴系統它要放在畫面的哪個位置
my_label.pack()

# 【步驟四】 啟動主迴圈 (Main Loop)
# 這是最重要的一步。呼叫後程式會「停在這裡」，不斷監聽使用者的滑鼠、鍵盤動作。
# 所有的程式碼都必須寫在 mainloop 之前！
root.mainloop()
```

---

## 2. 視窗的基礎設定

主視窗 (`root`) 建立後，我們可以對它進行各種外觀設定：

```python
root = tk.Tk()

# 設定視窗標題
root.title("我的應用程式")

# 設定視窗大小與初始位置 ("寬x高+X座標+Y座標")
# 下例為：寬 400，高 300，並在螢幕座標 (100, 100) 的地方開啟
root.geometry("400x300+100+100")

# 設定視窗背景顏色 (可使用英文單字或色碼)
root.config(bg="#f0f0f0")

# 鎖定視窗大小 (不允許使用者拖拉放大縮小)
# 第一個參數是寬度鎖定，第二個是高度鎖定
root.resizable(False, False) 
```

---

## 3. 三大佈局管理員 (Layout Managers) 深入解析

Tkinter 提供了三種佈局方式。**強烈建議在同一個視窗 (或同一個 Frame 容器) 內，只使用其中一種**，絕對不要混用 `pack` 和 `grid`，否則程式會崩潰或卡死。

### A. Pack 排版 (`pack`)
最簡單的排版方式，像堆積木一樣，由上而下或由左至右堆疊。適合單純的排版。

*   `side`: 停靠方向 (`tk.TOP`, `tk.BOTTOM`, `tk.LEFT`, `tk.RIGHT`)。預設為 `TOP`。
*   `padx`, `pady`: 外邊距 (元件外面的留白)。
*   `ipadx`, `ipady`: 內邊距 (元件裡面的留白，會讓元件看起來變大)。
*   `fill`: 填滿方向 (`tk.X` 橫向填滿, `tk.Y` 縱向填滿, `tk.BOTH` 全填滿)。
*   `expand`: 若設為 `True`，當視窗放大時，該元件會自動去搶佔多出來的空白空間。

```python
tk.Button(root, text="按鈕 A").pack(side=tk.LEFT, padx=10, fill=tk.Y)
tk.Button(root, text="按鈕 B").pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
```

### B. Grid 排版 (`grid`)
最強大的排版方式，把視窗當作 **Excel 表格**。對於表單 (如學生資料表的標籤配輸入框)、遊戲棋盤 (如圈圈叉叉) 最為適合。

*   `row`, `column`: 指定放在第幾列、第幾行 (從 0 開始計數)。
*   `rowspan`: 往下合併幾格 (例如 `rowspan=2` 會佔用目前這列與下一列)。
*   `columnspan`: 往右合併幾格。
*   `sticky`: 元件在格子內的對齊方式，使用羅盤方位：
    *   `"w"` (West): 靠左
    *   `"e"` (East): 靠右
    *   `"n"` (North): 靠上
    *   `"s"` (South): 靠下
    *   `"nsew"`: 上下左右全部填滿該格子。

```python
tk.Label(root, text="帳號：").grid(row=0, column=0, sticky="e")
tk.Entry(root).grid(row=0, column=1, sticky="w")
tk.Label(root, text="密碼：").grid(row=1, column=0, sticky="e")
tk.Entry(root).grid(row=1, column=1, sticky="w")
```

### C. Place 排版 (`place`)
給予絕對座標，就像在畫布上指定 X 與 Y。缺點是若使用者的螢幕解析度不同，或改變視窗大小時，元件位置不會跟著移動，容易跑版。
*   `x`, `y`: 距離視窗左上角的絕對像素。
*   `relx`, `rely`: 相對位置 (0.0 到 1.0 之間)。例如 `relx=0.5, rely=0.5` 會在正中央。

```python
tk.Button(root, text="絕對位置").place(x=50, y=100)
```

---

## 4. 基礎元件與屬性 (Widgets)

所有的元件都有一些共通屬性可以設定：
*   `font=("字體名稱", 大小, "樣式")`: 例如 `font=("Arial", 14, "bold")`。
*   `fg` 或 `foreground`: 文字顏色。
*   `bg` 或 `background`: 背景顏色。
*   `width`, `height`: 寬度與高度。**(注意：在 Button 和 Label 中，width 單位是「字元數」而非像素；但在 Canvas 中是像素)。**

### 4.1 Label (標籤)
用來顯示唯讀的文字或圖片。
```python
lbl = tk.Label(root, text="我是標籤", font=("微軟正黑體", 16))
# 事後修改屬性，使用 config 或 configure
lbl.config(text="文字被改變了！", fg="red") 
```

### 4.2 Button (按鈕)
使用者點擊的觸發器。
*   `command`: 綁定一個函式名稱 (注意：**不要加小括號()**，否則程式一執行就會立刻觸發該函式)。
*   `state`: 控制按鈕是否可用 (`"normal"` 正常, `"disabled"` 停用變灰)。

```python
def say_hello():
    print("你好！")

# 正確寫法：command=say_hello
# 錯誤寫法：command=say_hello() 
btn = tk.Button(root, text="點我", command=say_hello)
```

### 4.3 Entry (單行輸入框)
讓使用者輸入簡短文字。
*   `show`: 若要製作密碼輸入框，可設定 `show="*"`。

```python
entry = tk.Entry(root, width=20, font=("Arial", 12))

# 取得文字
user_input = entry.get()

# 清空文字：從第 0 個字元刪除到最後 (tk.END)
entry.delete(0, tk.END)

# 填寫預設值
entry.insert(0, "請輸入姓名")
```

### 4.4 Frame (框架/容器)
**排版的神器！** 當你需要一部分版面用 `grid`，一部分版面用 `pack` 時，你可以建立一個 Frame。
你可以把 Frame 想像成一塊「透明的板子」，你先把元件放在這塊板子上，最後再把板子放到主視窗上。

```python
top_frame = tk.Frame(root, bg="lightblue")
top_frame.pack(side=tk.TOP, fill=tk.X)

bottom_frame = tk.Frame(root, bg="lightgreen")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

# 把按鈕放在 bottom_frame 裡面，而不是 root 裡面
btn1 = tk.Button(bottom_frame, text="按鈕1").pack(side=tk.LEFT)
btn2 = tk.Button(bottom_frame, text="按鈕2").pack(side=tk.LEFT)
```

---

## 5. Tkinter 專屬變數 (Variables)

Python 內建的變數 (`int`, `str`) 無法直接與 Tkinter 的介面連動。Tkinter 提供了專屬的變數型態：
*   `tk.StringVar()`: 字串變數
*   `tk.IntVar()`: 整數變數
*   `tk.BooleanVar()`: 布林變數
*   `tk.DoubleVar()`: 浮點數變數

**重要特性**：當你使用 `set()` 改變這些變數的值時，所有綁定這個變數的 UI 元件（例如 Label, Radiobutton）都會**自動且瞬間更新**畫面！

```python
# 必須在 root = tk.Tk() 之後才能建立
my_var = tk.StringVar(value="初始文字")

# 將 Label 綁定 textvariable (注意不是 text)
lbl = tk.Label(root, textvariable=my_var)
lbl.pack()

# 只要變數改變，標籤畫面就會自動更新為 "文字改變了"
my_var.set("文字改變了")

# 讀取變數值
print(my_var.get())
```

---

## 6. 進階輸入元件 (Radiobutton, OptionMenu, Checkbutton)

### 6.1 Radiobutton (單選按鈕)
要達成「多選一」的效果，**所有的 Radiobutton 必須綁定到同一個 Tkinter 變數上**。

```python
gender_var = tk.StringVar(value="男") # 預設選中 "男"

# variable 綁定同一個變數，value 代表選中該按鈕時，變數會變成什麼值
tk.Radiobutton(root, text="男生", variable=gender_var, value="男").pack()
tk.Radiobutton(root, text="女生", variable=gender_var, value="女").pack()

# 取得結果就是 gender_var.get()
```

### 6.2 OptionMenu (下拉選單)
用來提供多個選項讓使用者選擇。

```python
city_var = tk.StringVar(value="台北")
cities = ["台北", "台中", "高雄", "花蓮"]

# 注意：前面要加星號 * 解包陣列
dropdown = tk.OptionMenu(root, city_var, *cities)
dropdown.pack()
```

### 6.3 Checkbutton (核取方塊 / 複選)
每一個 Checkbutton 通常會綁定一個獨立的 `IntVar` 或 `BooleanVar`。

```python
agree_var = tk.BooleanVar(value=False)

# onvalue 代表打勾時的值，offvalue 代表取消打勾時的值
chk = tk.Checkbutton(root, text="我同意條款", variable=agree_var, onvalue=True, offvalue=False)
chk.pack()

# 檢查是否打勾：agree_var.get() 會回傳 True 或 False
```

---

## 7. 事件綁定與回呼函式 (Events & Callbacks)

除了 Button 的 `command` 屬性外，Tkinter 提供更強大的 `bind` 方法來捕捉鍵盤與滑鼠的動作。

**語法**：`元件.bind("<事件名稱>", 處理函式)`

**重要規則**：被 `bind` 呼叫的處理函式，必須在括號內接收一個名為 `event` 的參數。這個 `event` 物件裡面包含了使用者按了什麼鍵、滑鼠座標在哪裡等資訊。

### 常見事件名稱：
*   `<Button-1>`: 滑鼠左鍵點擊
*   `<Button-3>`: 滑鼠右鍵點擊
*   `<Double-Button-1>`: 滑鼠左鍵雙擊
*   `<Enter>`: 滑鼠游標進入元件範圍 (與鍵盤的 Enter 無關！)
*   `<Leave>`: 滑鼠游標離開元件範圍
*   `<Return>`: 鍵盤的 Enter 鍵
*   `<KeyPress>`: 按下任意鍵

### 範例：綁定 Enter 鍵 (如打字遊戲)
```python
def on_enter_pressed(event):
    print("使用者按下了 Enter 鍵！")
    print("他輸入了：", entry.get())

entry = tk.Entry(root)
entry.pack()
# 將 Enter 鍵綁定到這個 Entry 元件上
entry.bind("<Return>", on_enter_pressed) 
```

### 範例：取得滑鼠點擊座標
```python
def get_mouse_pos(event):
    print(f"滑鼠點擊在 X:{event.x}, Y:{event.y}")

# 綁定在整個主視窗上
root.bind("<Button-1>", get_mouse_pos)
```

---

## 8. 計時器與非同步操作 (root.after)

在一般的 Python 程式中，我們常用 `time.sleep()` 來暫停程式。**但在 Tkinter 中絕對不能使用 `time.sleep()`！** 因為這會讓主迴圈 (`mainloop()`) 停止運轉，導致視窗卡死、無法點擊按鈕、畫面無法更新。

要製作動畫、跑馬燈、計時器，必須使用 **`root.after(毫秒, 函式)`**。它的意思是：「系統請在幾毫秒之後，幫我執行這個函式」。

### 範例：簡單的碼表計時器
```python
seconds = 0
running = True

def update_timer():
    global seconds
    if not running: return # 如果被停止了，就跳出
    
    seconds += 1
    lbl_time.config(text=f"已經過了 {seconds} 秒")
    
    # 【關鍵】執行完畢後，再次排程「1000毫秒後再呼叫一次 update_timer」
    # 這樣就形成了一個不會卡死視窗的無窮迴圈！
    root.after(1000, update_timer)

lbl_time = tk.Label(root, text="0")
lbl_time.pack()

# 手動啟動第一次
update_timer()
```
*(作業 07 老虎機的轉盤、09 打字遊戲的方塊掉落，全部都是使用 `root.after` 來完成的。)*

---

## 9. 彈出視窗與對話框 (Messagebox)

Tkinter 內建了多種常用的對話框。使用前必須先從 `tkinter` 模組中額外引入 `messagebox`。

```python
from tkinter import messagebox

# 一般提示訊息 (只有確定按鈕)
messagebox.showinfo("標題", "這是一個提示訊息！")

# 警告訊息 (圖示會有黃色驚嘆號)
messagebox.showwarning("警告", "密碼長度不足！")

# 錯誤訊息 (圖示會有紅色叉叉)
messagebox.showerror("錯誤", "找不到檔案！")

# 詢問對話框 (有 是/否 按鈕)，會回傳 True 或 False
result = messagebox.askyesno("確認", "你確定要刪除這筆資料嗎？")
if result:
    print("使用者點了 是")
else:
    print("使用者點了 否")
```

---

## 10. 畫布元件 (Canvas) 與繪圖

當你需要製作遊戲（像是貪食蛇、打字遊戲的掉落方塊），或是需要自由繪製幾何圖形時，`Canvas` 是首選元件。它使用的是絕對座標系統，左上角為 (0, 0)。

```python
# 建立一塊寬度 400，高度 300 的畫布
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# 1. 畫一條線 (x1, y1, x2, y2)
canvas.create_line(0, 0, 400, 300, fill="blue", width=5)

# 2. 畫一個矩形 (左上角X, 左上角Y, 右下角X, 右下角Y)
# 函式會回傳一個唯一的整數 ID，你可以把這個 ID 存起來以便之後操作它
rect_id = canvas.create_rectangle(50, 50, 150, 150, fill="red")

# 3. 畫文字
canvas.create_text(200, 150, text="Canvas 教學", font=("Arial", 20))

# 4. 操作已繪製的圖形 (需要圖形的 ID)
# 將剛剛的紅色矩形往右移動 10 像素，往下移動 20 像素
canvas.move(rect_id, 10, 20)

# 修改矩形的顏色為綠色
canvas.itemconfig(rect_id, fill="green")

# 取得圖形目前的座標 [x1, y1, x2, y2]
coords = canvas.coords(rect_id)

# 將圖形從畫布上刪除
canvas.delete(rect_id)

# 清空畫布上所有的東西
canvas.delete("all")
```

---

## 11. 在 Tkinter 中使用圖片 (PIL / Pillow)

Tkinter 原本只支援 `.gif` 格式的圖片。要使用 `.png` 或 `.jpg`，我們必須安裝並使用強大的第三方影像處理套件：**Pillow** (PIL 的更新版)。

> 終端機安裝指令：`pip install Pillow`

```python
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# 1. 使用 PIL 開啟圖片
img = Image.open("my_picture.png")

# 2. (選用) 調整圖片大小：寬 200, 高 150
# 注意這裡傳入的是一個 Tuple (200, 150)
img = img.resize((200, 150))

# 3. 轉換為 Tkinter 能夠理解的圖片格式
photo = ImageTk.PhotoImage(img)

# 4. 把圖片放入 Label 或 Canvas 中
lbl = tk.Label(root, image=photo)
lbl.pack()

# 【超級重要防雷區】
# Python 的垃圾回收機制(Garbage Collection)如果發現變數 photo 沒人在用，就會把它清掉
# 這會導致圖片顯示成空白或破圖。
# 為了避免這個問題，我們必須「手動」把 photo 綁定在 label 的某個屬性上：
lbl.image = photo

root.mainloop()
```

---

## 總結

這份指南涵蓋了 Tkinter 開發中 **95%** 會用到的核心觀念與技巧。當你在寫作業時，如果忘記某個元件怎麼用，隨時打開這份 `markdown` 搜尋對應的標題即可。

**學習建議：**
1. 遇到排版問題 $\rightarrow$ 回來看 **第 3 節 (Pack / Grid / Frame)**。
2. 遇到按鈕沒反應或提早觸發 $\rightarrow$ 回來看 **第 4 節 (Button command) 與 第 7 節 (bind)**。
3. 遇到變數改了畫面沒變 $\rightarrow$ 回來看 **第 5 節 (StringVar / IntVar)**。
4. 遇到迴圈卡死視窗當機 $\rightarrow$ 回來看 **第 8 節 (root.after)**。
5. 遇到圖片顯示不出來 $\rightarrow$ 回來看 **第 11 節 (垃圾回收機制防禦)**。
