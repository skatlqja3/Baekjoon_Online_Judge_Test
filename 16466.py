import sys
n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
l = [0 for _ in range(1000001)]
for i in range(n):
    l[m[i]-1] = 1
for i in range(1000001):
    if l[i] == 0:
        print(i+1)
        break