# 🎯 Python 實習 (二) 期末上機考：進階題庫與破解秘笈

老師如果是考進階邏輯，通常會要求您**改變遊戲規則**、**增加新功能**或**修改判定條件**。這份秘笈整理了 06 到 11 作業最有可能出現的「殺手級考題」，以及對應的程式碼修改方式。

---

## 🛠️ 作業 06：打地鼠 (Whack-a-mole)

### 💀 考題 1：加入「扣分機制」（打錯洞扣分）
**題目描述**：如果玩家點擊沒有地鼠（空）的按鈕，總分要倒扣 1 分（最低不扣到負分）。
**破解法**：找到 `def whack(self, r, c):` 函式，加入 `else` 判斷。

```python
    def whack(self, r, c):
        btn = self.buttons[r][c]
        if btn.cget("text") == self.mole_char:
            btn.config(text="")
            self.score += 1
            self.lbl_score.config(text=f"總分: {self.score}")
        else:
            # 【加入這段】打錯扣分機制
            if self.score > 0:
                self.score -= 1
            self.lbl_score.config(text=f"總分: {self.score}")
```

### 💀 考題 2：加入「黃金地鼠」（打中得 5 分）
**題目描述**：讓畫面上有一半機率出現黃金地鼠（符號為 `$`)，打中可以獲得 5 分。
**破解法**：
1. 在 `def start_stage(self):` 中修改放置地鼠的邏輯：
```python
        for r, c in positions:
            # 【修改這段】隨機決定是普通地鼠還是黃金地鼠
            import random
            if random.random() > 0.8:  # 20% 機率是黃金地鼠
                self.buttons[r][c].config(text="$", fg="gold")
            else:
                self.buttons[r][c].config(text=self.mole_char, fg="black")
```
2. 在 `def whack(self, r, c):` 增加得分判定：
```python
    def whack(self, r, c):
        btn = self.buttons[r][c]
        if btn.cget("text") == self.mole_char:
            btn.config(text="")
            self.score += 1
        # 【加入這段】黃金地鼠得 5 分
        elif btn.cget("text") == "$":
            btn.config(text="")
            self.score += 5
            
        self.lbl_score.config(text=f"總分: {self.score}")
```

---

## 🛠️ 作業 07：老虎機 (Slot Machine)

### 💀 考題 1：中獎判定（停在蘋果加 100 分）
**題目描述**：如果轉盤停止時，剛好停在特定的水果上，則提示中獎。
**破解法**：找到 `def spin(self):` 最下方的 `else:` 區塊（表示停止轉動）。

```python
        if self.spin_delay < self.spin_stop_threshold:
            self.root.after(self.spin_delay, self.spin)
        else:
            self.spinning = False
            self.btn_go.config(state="normal")
            
            # 【加入這段】中獎判定
            # 此處的寫法依賴您在建立 Label 時是否有把對應的檔案名存下來
            # 比較快的方式是直接看格子裡的圖片物件是哪一個 (進階做法)
```

### 💀 考題 2：視覺殘影效果
**題目描述**：亮起紅燈時，上一個位子要是黃燈（殘影），而不是直接變白燈。
**破解法**：修改 `def highlight(self, pos):` 邏輯。

```python
    def highlight(self, pos):
        prev_pos = (pos - 1) % len(self.labels) # 計算上一個位子
        for i, lbl in enumerate(self.labels):
            if i == pos:
                lbl.config(bg="red")
            elif i == prev_pos:
                lbl.config(bg="yellow") # 【修改】殘影變黃色
            else:
                lbl.config(bg="white")
```

---

## 🛠️ 作業 08：英文拼字 (Vocab)

### 💀 考題 1：加入「答錯 3 次就跳下一題」
**題目描述**：防止玩家一直卡在同一題，輸入錯誤滿 3 次就強制換題。
**破解法**：
1. 在 `__init__` 加入 `self.wrong_count = 0`。
2. 在 `def next_question(self):` 中重置：`self.wrong_count = 0`。
3. 修改 `def check_answer(self):`：
```python
    def check_answer(self):
        ans = self.entry_answer.get().strip()
        if ans.lower() == self.current_word.lower():
            self.correct_count += 1
            self.lbl_score.config(text=f"答對數目： {self.correct_count}")
            self.next_question()
        else:
            # 【加入這段】錯誤計數
            self.wrong_count += 1
            if self.wrong_count >= 3:
                # 錯 3 次強制跳題
                self.next_question()
            else:
                # 答錯但還沒 3 次，清空輸入框讓玩家重打
                self.entry_answer.delete(0, tk.END)
```

---

## 🛠️ 作業 09：打字掉落 (Typing Fall)

### 💀 考題 1：打錯字倒扣分數，而且加快掉落速度（懲罰）
**題目描述**：如果送出的字串不是目標單字，扣一分，而且接下來所有的方塊掉落速度變快。
**破解法**：修改 `def check_input(self, event):`。

```python
    def check_input(self, event):
        if self.game_over: return
        typed_word = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        
        if typed_word == self.current_word:
            # ... 原本答對的程式碼 ...
        else:
            # 【加入這段】答錯懲罰
            self.score -= 1
            self.lbl_score.config(text=f"score: {self.score}")
            self.fall_pixels += 2  # 每次打錯，掉落速度加快 2 像素
```

---

## 🛠️ 作業 11：資料表 CRUD

### 💀 考題 1：新增「依學號搜尋」功能
**題目描述**：介面上多一個「搜尋」按鈕，輸入學號後可以跳到該筆學生的資料。
**破解法**：
1. 在 `__init__` 最底部的按鈕區加入：
```python
tk.Button(btn_frame, text="搜尋", command=self.search_record).pack(side=tk.LEFT, padx=2)
```
2. 新增 `search_record` 函式：
```python
    def search_record(self):
        target_id = self.entries["學號"].get().strip()
        for i, record in enumerate(self.data):
            if record[0] == target_id:
                self.current_idx = i
                self.show_record()
                return
        from tkinter import messagebox
        messagebox.showinfo("提示", "找不到此學號")
```

### 💀 考題 2：防止新增「重複的學號」
**題目描述**：如果按「更新（新增）」時，學號已經存在於資料庫中，則不允許新增。
**破解法**：在 `def update_record(self):` 中攔截：
```python
    def update_record(self):
        new_record = self.get_current_input()
        if not new_record[0]: return
            
        if self.is_adding:
            # 【加入這段】檢查學號重複
            for record in self.data:
                if record[0] == new_record[0]:
                    from tkinter import messagebox
                    messagebox.showerror("錯誤", "學號已存在！")
                    return
            # ... 下面接原本新增的邏輯 ...
```
