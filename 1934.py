n=int(input())
for _ in range(n):
    m,l = map(int,input().split())
    max=m*l
    if m < l:
        m,l = l,m
    while l!=0:
        r=m%l
        m=l
        l=r
    print(int(max/m))