n,m=map(int,input().split())
l=int(input())
m=m+l
if m>=60:
    t=int(m/60)
    m=m%60
    n=n+t
    if n>=24:
        n=n%24    
print(f"{n} {m}")