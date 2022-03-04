n=int(input())
x,y=100,100
for i in range(n):
    m,l=map(int,input().split())
    if m > l:
        y-=m
    elif m < l:
        x-=l
print(x)
print(y)