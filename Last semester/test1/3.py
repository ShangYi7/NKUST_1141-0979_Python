from random import randint 

while (1):
    data=input()
    if(data=='0'):
        break
    ansA=(randint(1,6))
    ansB=(randint(1,6))
    if(ansA>ansB):
        if(data=="A"):
            print("A:",ansA,"B:",ansB, "You Win!")
        elif(data=="B"):
            print("A:",ansA,"B:",ansB, "You Lost!")
    elif(ansA<ansB):
        if(data=="A"):
            print("A:",ansA,"B:",ansB, "You Lost!")
        elif(data=="B"):
            print("A:",ansA,"B:",ansB, "You Win!")
    elif(ansA==ansB):
        print("A:",ansA,"B:",ansB, "Game Tie!")
print()
