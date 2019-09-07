def printTriangle(n):
    if(n >= 3):
        print(' '.join(['*']*(n+2)))
        s = int((n/2)+1)
        for i in range(s):
            star_list = ['  ']*(n+2)
            star_list[-i-2] = ' *'
            star_list[i+1] = '*'
            print(''.join(star_list))
    else:
        print("Minimal 3")
printTriangle(5)
