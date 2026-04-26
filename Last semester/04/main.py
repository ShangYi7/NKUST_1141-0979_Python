for _ in range(3):
    x = input()

    # 手動計數：只統計英文字母，並把大小寫分開記錄
    counts = {}
    for ch in x:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            counts[ch] = counts.get(ch, 0) + 1

    # 固定輸出順序：先小寫 a-z，再大寫 A-Z
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    parts = []
    for ch in letters:
        n = counts.get(ch, 0)
        if n:
            parts.append(ch + ' ' + ('*' * n))

    print(' '.join(parts))
