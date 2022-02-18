import sys
n=int(input())
max = 0
for i in range(n):
    x = 0
    m=list(map(int,input().split()))
    if m[0] == m[1] and m[1] == m[2] and m[0] == m[2]:
        x=10000+m[0]*1000
    elif m[0] != m[1] and m[1] != m[2] and m[0] != m[2]:
        if m[0] < m[1]:
            if m[1] < m[2]:
                x = m[2]*100
            else:
                x = m[1]*100
        elif m[0] < m[2]:
            x = m[2]*100
        elif m[2] < m[0]:
            x = m[0]*100
    else:
        if m[0]==m[1]:
            x = m[0]*100+1000
        elif m[1]==m[2]:
            x = m[1]*100+1000
        elif m[0]==m[2]:
            x = m[0]*100+1000
    if max < x:
        max = x
print(max)