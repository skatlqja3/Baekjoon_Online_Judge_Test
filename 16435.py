import sys
n,m = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))
l.sort()
for i in l:   
    if m >= i:
        m += 1
print(m)
