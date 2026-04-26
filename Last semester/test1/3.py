from random import randint

while (1):
    # 使用者輸入 A、B 或 0 結束
    data = input()
    if (data == '0'):
        break
    # 產生兩個 1~6 的隨機點數，模擬擲骰子
    ansA = (randint(1, 6))
    ansB = (randint(1, 6))
    if (ansA > ansB):
        # A 點數較大時，依使用者選擇判斷勝負
        if (data == "A"):
            print("A:", ansA, "B:", ansB, "You Win!")
        elif (data == "B"):
            print("A:", ansA, "B:", ansB, "You Lost!")
    elif (ansA < ansB):
        # B 點數較大時同理處理
        if (data == "A"):
            print("A:", ansA, "B:", ansB, "You Lost!")
        elif (data == "B"):
            print("A:", ansA, "B:", ansB, "You Win!")
    elif (ansA == ansB):
        # 兩邊相同即平手
        print("A:", ansA, "B:", ansB, "Game Tie!")
print()
