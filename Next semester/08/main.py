import tkinter as tk
import random

class VocabApp:
    """
    英文單字練習主程式類別。
    負責從外部文字檔讀取題庫，隨機遮蔽字母後由使用者輸入答案。
    """
    def __init__(self, root):
        self.root = root
        self.root.title("tk")
        
        # ==========================================
        # ⬇️⬇️⬇️ 遊戲參數設定區 (可隨意修改) ⬇️⬇️⬇️
        # ==========================================
        self.data_file = "words.txt"   # 儲存單字題庫的檔名
        self.mask_char = "*"           # 遮蔽字母時使用的替代符號
        self.mask_ratio = 2            # 遮蔽比例 (2 代表遮蔽 1/2 的字母，3 代表 1/3)
        # ==========================================
        # ⬆️⬆️⬆️ 遊戲參數設定區 (可隨意修改) ⬆️⬆️⬆️
        # ==========================================
        
        self.words = []
        # 初始化時先從 words.txt 載入單字題庫
        self.load_words()
        
        self.correct_count = 0
        self.current_word = ""
        
        # 建立 UI 元件：英文題目、中文提示、答對計數器、輸入框與送出按鈕
        self.lbl_masked = tk.Label(root, text="", font=("Arial", 12))
        self.lbl_masked.pack(pady=20)
        
        self.lbl_hint = tk.Label(root, text="", font=("Arial", 12))
        self.lbl_hint.pack(pady=10)
        
        self.lbl_score = tk.Label(root, text=f"答對數目： 0", font=("Arial", 12))
        self.lbl_score.pack(pady=20)
        
        self.entry_answer = tk.Entry(root, font=("Arial", 12), width=25)
        self.entry_answer.pack(pady=5)
        
        self.btn_submit = tk.Button(root, text="確定", command=self.check_answer)
        self.btn_submit.pack(pady=5)
        
        # 初始化第一道題目
        self.next_question()
        
    def load_words(self):
        """
        載入單字題庫。
        使用絕對路徑讀取 words.txt 以確保跨目錄執行不會拋錯。
        檔案格式預期為：英文,中文 (例如 apple,蘋果)。
        若檔案遺失會套用預設的備用題庫。
        """
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, self.data_file)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    if "," in line:
                        # 依照第一個逗號切割出英文與中文
                        eng, chn = line.strip().split(",", 1)
                        self.words.append((eng, chn))
        except FileNotFoundError:
            # 檔案不存在時的錯誤處理機制，提供基本功能測試
            self.words = [("appropriate", "適當的"), ("banana", "香蕉")]
            
    def next_question(self):
        """
        進入下一題。
        會隨機抽選一個單字，並隨機將該單字至少一半的字母替換成 '*' 符號。
        """
        if not self.words: return
        self.current_word, hint = random.choice(self.words)
        
        # 將單字轉換為陣列以便修改個別字元
        masked = list(self.current_word)
        
        # 計算要遮蔽的字元數量（至少遮蔽一個，且最多遮蔽一定比例的字母）
        # 這是為了確保提示不會過於簡單或完全無法辨識
        num_mask = max(1, len(masked) // self.mask_ratio)
        
        # 隨機抽取需要遮蔽的索引位置
        mask_indices = random.sample(range(len(masked)), num_mask)
        for i in mask_indices:
            masked[i] = self.mask_char
            
        # 更新介面顯示
        self.lbl_masked.config(text=f"英文： {''.join(masked)}")
        self.lbl_hint.config(text=f"中文： {hint}")
        self.entry_answer.delete(0, tk.END)
        
    def check_answer(self):
        """
        驗證使用者輸入的答案是否正確。
        為避免大小寫差異造成誤判，比對時皆轉換為小寫。
        """
        ans = self.entry_answer.get().strip()
        if ans.lower() == self.current_word.lower():
            # 答案正確，加分並更新顯示
            self.correct_count += 1
            self.lbl_score.config(text=f"答對數目： {self.correct_count}")
            
        # 無論對錯皆直接進入下一題（符合 PPT 描述的行為）
        self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("250x300")
    app = VocabApp(root)
    root.mainloop()
