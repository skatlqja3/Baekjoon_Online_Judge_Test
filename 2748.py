import sys
n = int(sys.stdin.readline())
i = 2
a = [0,1]
while i >=2 and i<=n:
    a.append(a[i-2]+a[i-1])
    i = i +1
print(a[n])