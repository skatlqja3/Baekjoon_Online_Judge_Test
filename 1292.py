import sys
n,m = map(int,sys.stdin.readline().split())
l = 0
sum = 0
num = 0
co = 0
x = 1
for i in range(1,m+1):
    num += x
    co += 1
    if i >= n:
        sum += x
    if co == x:
        x += 1
        co = 0
    
print(sum)