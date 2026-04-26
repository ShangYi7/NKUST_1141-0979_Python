while 1:
    # n 控制圖形大小，範圍 1~26
    n = int(input())
    e = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if (n > 0 and n <= 26):
        # 下面用三層迴圈控制每一列的縮排與重複字元數量
        k = 0
        i = n-1
        j = 0
        while k != n:
            while i != 0:
                print(" ", end="")
                i = i-1
            i = n-k-1
            while j != n-i:
                print(e[k], " ", end="")
                j = j+1
            j = 0
            print("")
            k = k+1
            i = n-k-1
