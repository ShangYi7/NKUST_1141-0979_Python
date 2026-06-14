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
correct_count = 0         # 答對總次數
wrong_count = 0           # 【進階版】目前這題答錯了幾次
current_word = ""         # 目前這題正確的英文單字


# ==========================================
# 2. 遊戲主要邏輯
# ==========================================
def load_words():
    """
    從檔案載入單字題庫。
    """
    global words
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, data_file)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if "," in line:
                    eng, chn = line.strip().split(",", 1)
                    words.append((eng, chn))
    except FileNotFoundError:
        words = [("appropriate", "適當的"), ("banana", "香蕉")]


def next_question():
    """
    隨機挑選下一個單字，並遮蔽部分字母。
    """
    global current_word, wrong_count
    
    if not words: return
    
    # 【進階版】每次換新題目時，要把這題的答錯次數歸零
    wrong_count = 0  
    
    # 隨機挑出一個單字與提示
    current_word, hint = random.choice(words)
    masked = list(current_word)
    num_mask = max(1, len(masked) // mask_ratio)
    
    mask_indices = random.sample(range(len(masked)), num_mask)
    for i in mask_indices:
        masked[i] = mask_char
        
    # 更新標籤顯示
    lbl_masked.config(text=f"英文： {''.join(masked)}")
    lbl_hint.config(text=f"中文： {hint}")
    entry_answer.delete(0, tk.END)


def check_answer():
    """
    檢查玩家輸入的答案是否正確。
    進階版：加入答錯計數機制，答錯滿 3 次強制換題。
    """
    global correct_count, wrong_count
    
    ans = entry_answer.get().strip()
    
    if ans.lower() == current_word.lower():
        # 答案正確
        correct_count += 1
        lbl_score.config(text=f"答對數目： {correct_count}")
        # 答對就直接換下一題
        next_question()
    else:
        # 【進階版】答案錯誤的懲罰機制
        wrong_count += 1
        
        # 如果已經連續答錯 3 次
        if wrong_count >= 3:
            # 錯滿 3 次，沒耐心了，直接強制換下一題
            next_question()
        else:
            # 答錯但還沒滿 3 次，清空輸入框讓玩家再重打一次
            entry_answer.delete(0, tk.END)


# ==========================================
# 3. 建立視窗與畫面配置 (GUI)
# ==========================================
root = tk.Tk()
root.title("單字測驗 (進階版：容錯三次)")
root.geometry("250x300")

lbl_masked = tk.Label(root, text="", font=("Arial", 12))
lbl_masked.pack(pady=20)

lbl_hint = tk.Label(root, text="", font=("Arial", 12))
lbl_hint.pack(pady=10)

lbl_score = tk.Label(root, text=f"答對數目： 0", font=("Arial", 12))
lbl_score.pack(pady=20)

entry_answer = tk.Entry(root, font=("Arial", 12), width=25)
entry_answer.pack(pady=5)

btn_submit = tk.Button(root, text="確定", command=check_answer)
btn_submit.pack(pady=5)

# ==========================================
# 4. 啟動程式前先準備資料
# ==========================================
load_words()
next_question()

root.mainloop()
