import sys
n, m = map(int, sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))
num = 0
max = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            num = l[i]+l[j]+l[k]
            if max <= num:
                if num <= m:
                    max = num
print(max)