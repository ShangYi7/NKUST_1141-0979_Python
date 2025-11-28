# 剪刀石頭布遊戲
# N戰(N+1)/2勝
# Y代表剪刀、M代表石頭、O代表布
while True:
    n=int(input())
    win1=0
    win2=0
    # 檢查是否為正奇數
    if(n%2!=0 and n>0):
        while True:
            data=input().split()
            player1=data[0]
            player2=data[1]


            if(player1=="Y" and player2=="M"):
                win2+=1
            elif(player1=="Y" and player2=="O"):
                win1+=1
            elif(player1=="M" and player2=="Y"):
                win1+=1
            elif(player1=="M" and player2=="O"):
                win2+=1
            elif(player1=="O" and player2=="Y"):
                win2+=1
            elif(player1=="O" and player2=="M"):
                win1+=1
            if(win1>=(n+1)/2):
                print("The first person wins the game")
                break
            elif(win2>=(n+1)/2):
                print("The second person wins the game")
                break
    else:
        break
