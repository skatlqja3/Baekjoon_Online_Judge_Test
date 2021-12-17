import sys

n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
l = list(map(int,sys.stdin.readline().split()))
sum = 0
m.sort()
l.sort(reverse=True)
print(m)
print(l)
for i in range(n):
    sum = (m[i] * l[i])+sum
print(sum)