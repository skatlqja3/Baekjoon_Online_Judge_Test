n,m = map(int,input().split())
y=0
if m-45 < 0:
    y=15+m
    n -=1
    if n < 0:
        n=23
else:
    y=m-45
print(f"{n} {y}") 