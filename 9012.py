n=int(input())
for _ in range(n):
    r,l,x=0,0,0
    m=list(map(str,input()))
    if len(m) % 2 != 0:
        print("NO")
    else:
        for i in m:
            if i == '(':
                l+=1
            else:
                r+=1
                if r > l :
                    x=1
                    break
        if l == r:
            print("YES")
        elif x == 1:
            print("NO")
        else:
            print("NO")