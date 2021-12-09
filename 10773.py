import sys
n = int(sys.stdin.readline())
m = []
sum = 0
for i in range(n):
    l = int(sys.stdin.readline())
    if l == 0:
        m.pop()
    if l != 0:
        m.append(l)
for i in m:
    sum += i
print(sum)
