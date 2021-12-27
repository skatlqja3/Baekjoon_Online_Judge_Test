import sys
n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
l = [0] * 1000001
count = 0
for i in range(n):
    if l[m[i]] == 0:
        count += 1
        l[m[i]-1] += 1
    else :
        l[m[i]] -= 1
        l[m[i]-1] += 1
print(count)