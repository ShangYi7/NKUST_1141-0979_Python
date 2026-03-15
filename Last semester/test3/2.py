while 1:
    n=int(input())
    e=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if(n>0 and n<=26):
        k=0
        i=n-1
        j=0
        while k!=n:
            while i!=0:
                print(" ",end="")
                i=i-1
            i=n-k-1
            while j!=n-i:
                print(e[k]," ",end="")
                j=j+1
            j=0
            print("")
            k=k+1
            i=n-k-1

