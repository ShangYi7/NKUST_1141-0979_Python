for _ in range(3):
    x = input()

    # 手動計數（大小寫分開）
    counts = {}
    for ch in x:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            counts[ch] = counts.get(ch, 0) + 1

    # 固定輸出順序：a-z 接著 A-Z
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    parts = []
    for ch in letters:
        n = counts.get(ch, 0)
        if n:
            parts.append(ch + ' ' + ('*' * n))

    print(' '.join(parts))