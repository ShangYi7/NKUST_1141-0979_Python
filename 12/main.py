# 讀取檔案資料
customers = {}
try:
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        parts = line.split()
        if len(parts) >= 4:
            customers[parts[0]] = [parts[1], parts[2], parts[3]]
except:
    pass

# 主程式
while True:
    command = input()
    parts = command.split()

    if len(parts) == 0:
        continue

    # 結束程式
    if parts[0] == '*':
        break

    # 新增顧客資料
    if parts[0] == '@' and len(parts) >= 5:
        if parts[1] in customers:
            print('Exist')
        else:
            customers[parts[1]] = [parts[2], parts[3], parts[4]]
            # 寫入檔案
            f = open('input.txt', 'w')
            for id in customers:
                f.write(id + ' ' + customers[id][0] + ' ' + customers[id][1] + ' ' + customers[id][2] + '\n')
            f.close()

    # 刪除顧客資料
    elif parts[0] == '#' and len(parts) >= 2:
        if parts[1] in customers:
            del customers[parts[1]]
            # 寫入檔案
            f = open('input.txt', 'w')
            for id in customers:
                f.write(id + ' ' + customers[id][0] + ' ' + customers[id][1] + ' ' + customers[id][2] + '\n')
            f.close()
        else:
            print('None')

    # 更改顧客資料
    elif parts[0] == '!' and len(parts) >= 4:
        if parts[1] in customers:
            if parts[2] == '0':
                customers[parts[1]][0] = parts[3]
            elif parts[2] == '1':
                customers[parts[1]][1] = parts[3]
            elif parts[2] == '2':
                customers[parts[1]][2] = parts[3]
            # 寫入檔案
            f = open('input.txt', 'w')
            for id in customers:
                f.write(id + ' ' + customers[id][0] + ' ' + customers[id][1] + ' ' + customers[id][2] + '\n')
            f.close()
        else:
            print('None')

    # 查詢顧客資料
    elif parts[0] == '$' and len(parts) >= 3:
        if parts[1] in customers:
            if parts[2] == '0':
                print(customers[parts[1]][0])
            elif parts[2] == '1':
                print(customers[parts[1]][1])
            elif parts[2] == '2':
                print(customers[parts[1]][2])
        else:
            print('None')
