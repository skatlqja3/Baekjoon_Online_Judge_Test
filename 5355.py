from re import M
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    x=0.0
    m=list(map(str,sys.stdin.readline().split()))
    x=float(m[0])
    for i in range(1,len(m)):
        if m[i] == '@':
            x*=3
        elif m[i] == '#':
            x-=7
        elif m[i] == '%':
            x+=5
    print(f'{x:.2f}')