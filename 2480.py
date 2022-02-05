n,m,l = map(int,input().split())
if n == m and m == l and n == l :
    print(10000+(n)*1000)
elif n != m and m != l and n != l :
    if n < m and m < l :
        print(l*100)
    elif n < m and m > l :
        print(m*100)
    elif n > m and n > l:
        print(n*100)
else:
    if n == m:
        print(1000+n*100)
    elif m == l:
        print(1000+m*100)
    else:
        print(1000+l*100) 