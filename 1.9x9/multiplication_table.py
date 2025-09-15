# 九九乘法表排序程式
# 規則：
# 1. 先由小到大列出九九乘法表中 M1為奇數的公式，若M1相同時，則根據M2由小到大列出
# 2. 接下來列出剩餘的九九乘法表中M2為奇數的公式(M1越小越先列出，若M1相同則根據M2由小到大列出)
# 3. 最後列出剩餘的公式(M1越小越先列出，若M1相同則根據M2由小到大列出)

# 生成所有九九乘法表公式
all_formulas = []
for m1 in range(1, 10):
    for m2 in range(1, 10):
        p = m1 * m2
        all_formulas.append((m1, m2, p))

# 第一組：M1為奇數的公式
group1 = []
for m1, m2, p in all_formulas:
    if m1 % 2 == 1:  # M1為奇數
        group1.append((m1, m2, p))

# 排序：M1由小到大，若M1相同則M2由小到大
group1.sort(key=lambda x: (x[0], x[1]))

# 第二組：剩餘的M2為奇數的公式（M1必須是偶數）
group2 = []
for m1, m2, p in all_formulas:
    if m1 % 2 == 0 and m2 % 2 == 1:  # M1為偶數且M2為奇數
        group2.append((m1, m2, p))

# 排序：M1由小到大，若M1相同則M2由小到大
group2.sort(key=lambda x: (x[0], x[1]))

# 第三組：剩餘的公式（M1為偶數且M2為偶數）
group3 = []
for m1, m2, p in all_formulas:
    if m1 % 2 == 0 and m2 % 2 == 0:  # M1為偶數且M2為偶數
        group3.append((m1, m2, p))

# 排序：M1由小到大，若M1相同則M2由小到大
group3.sort(key=lambda x: (x[0], x[1]))

# 合併所有公式並按順序排列
all_sorted_formulas = group1 + group2 + group3

# 輸出結果 - 橫向排列格式
formulas_per_row = 9  # 每行顯示9個公式

for i in range(0, len(all_sorted_formulas), formulas_per_row):
    row_formulas = all_sorted_formulas[i:i+formulas_per_row]
    formatted_row = []
    
    for m1, m2, p in row_formulas:
        # 格式化每個公式，確保對齊
        formula = f"{m1} X {m2} = {p}"
        formatted_row.append(f"{formula:>8}")
    
    # 輸出這一行
    print("    ".join(formatted_row))

print(f"\n總共 {len(all_sorted_formulas)} 個公式")

# 驗證是否為81個公式
if len(all_sorted_formulas) == 81:
    print("✓ 確認包含九九乘法表的所有81個公式")
else:
    print("✗ 公式數量不正確")