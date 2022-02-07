import sys
n=int(sys.stdin.readline())
m=list(map(int,sys.stdin.readline().split()))
m.sort()
if n >= 4:
    print(m[0]*m[n-1])
elif n == 3:
    print(m[n-2]*m[n-2])
elif n == 2:
    print(m[0]*m[1])
elif n == 1:
    print(m[0]*m[0])