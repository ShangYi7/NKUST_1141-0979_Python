import tkinter as tk
import random
import os

# ==========================================
# 1. 設定全域變數 (遊戲參數與狀態)
# ==========================================
data_file = "words.txt"   # 儲存單字題庫的檔名
mask_char = "*"           # 遮蔽字母時使用的替代符號
mask_ratio = 2            # 遮蔽比例 (2 代表遮蔽 1/2 的字母，3 代表 1/3)

words = []                # 存放讀取出來的題庫 (英文, 中文) 的陣列
correct_count = 0         # 答對次數
current_word = ""         # 目前這題正確的英文單字


# ==========================================
# 2. 遊戲主要邏輯
# ==========================================
def load_words():
    """
    從檔案載入單字題庫。
    檔案格式必須為：英文,中文 (例如 apple,蘋果)
    """
    global words
    
    # 取得目前這個 Python 檔案所在的絕對路徑目錄
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 將目錄與檔名合併，組成完整的檔案路徑
    file_path = os.path.join(script_dir, data_file)
    
    try:
        # 開啟檔案 (指定編碼為 utf-8 避免中文亂碼)
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                # 如果這行文字裡面有逗號，才進行處理
                if "," in line:
                    # 使用 split 依照第一個逗號切割成兩半 (英文與中文)
                    eng, chn = line.strip().split(",", 1)
                    # 將這組單字包成一個小組 (tuple)，加入陣列中
                    words.append((eng, chn))
    except FileNotFoundError:
        # 如果找不到 words.txt 檔案，就給幾組預設的單字，以免程式直接掛掉
        words = [("appropriate", "適當的"), ("banana", "香蕉")]


def next_question():
    """
    隨機挑選下一個單字，並將部分字母遮蔽變成 '*'，然後顯示在畫面上。
    """
    global current_word
    
    if not words: 
        return # 題庫空的就不做事
        
    # 隨機從題庫抽一組出來 (eng 是英文，hint 是中文提示)
    current_word, hint = random.choice(words)
    
    # 將英文字串轉換為串列 (List)，例如 "apple" 變成 ['a', 'p', 'p', 'l', 'e']
    # 這樣我們才能去修改裡面的單一字母
    masked = list(current_word)
    
    # 計算需要被遮掉幾個字 (總長度除以 mask_ratio 取整數，最少遮 1 個)
    num_mask = max(1, len(masked) // mask_ratio)
    
    # 隨機抽出幾個「位置索引」(例如抽到第 1 個和第 3 個字母要遮)
    mask_indices = random.sample(range(len(masked)), num_mask)
    
    # 將抽中位置的字母替換成遮蔽符號 '*'
    for i in mask_indices:
        masked[i] = mask_char
        
    # 把處理好的陣列合併回字串，更新到畫面的標籤上
    lbl_masked.config(text=f"英文： {''.join(masked)}")
    lbl_hint.config(text=f"中文： {hint}")
    
    # 清空玩家輸入框
    entry_answer.delete(0, tk.END)


def check_answer():
    """
    檢查玩家輸入的答案是否等於目前的單字。
    """
    global correct_count
    
    # 取得輸入框的文字，並用 strip() 去除前後多餘的空白
    ans = entry_answer.get().strip()
    
    # 為了防止大小寫差異導致算錯，我們把玩家輸入的和標準答案都轉成全小寫 (lower()) 再比對
    if ans.lower() == current_word.lower():
        # 答案正確，加分並更新顯示
        correct_count += 1
        lbl_score.config(text=f"答對數目： {correct_count}")
        
    # 無論答對或答錯，都直接進入下一題 (基礎版的邏輯)
    next_question()


# ==========================================
# 3. 建立視窗與畫面配置 (GUI)
# ==========================================
root = tk.Tk()
root.title("單字測驗 (基礎版)")
root.geometry("250x300") # 設定視窗大小為寬 250，高 300

# 建立顯示被遮蔽的英文標籤
lbl_masked = tk.Label(root, text="", font=("Arial", 12))
lbl_masked.pack(pady=20) # 上下留白 20 像素

# 建立顯示中文提示的標籤
lbl_hint = tk.Label(root, text="", font=("Arial", 12))
lbl_hint.pack(pady=10)

# 建立顯示答對題數的標籤
lbl_score = tk.Label(root, text=f"答對數目： 0", font=("Arial", 12))
lbl_score.pack(pady=20)

# 建立讓玩家輸入答案的輸入框 (Entry)
entry_answer = tk.Entry(root, font=("Arial", 12), width=25)
entry_answer.pack(pady=5)

# 建立確定送出按鈕
btn_submit = tk.Button(root, text="確定", command=check_answer)
btn_submit.pack(pady=5)

# ==========================================
# 4. 啟動程式前先準備資料
# ==========================================
# 先載入外部檔案的單字
load_words()
# 產生第一道題目
next_question()

# 開始等待玩家操作
root.mainloop()
