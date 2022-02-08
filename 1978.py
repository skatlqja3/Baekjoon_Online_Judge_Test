import sys
n=int(sys.stdin.readline())
m=list(map(int,sys.stdin.readline().split()))
count = 0
def x(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count+=1
    if count == 2:
        return 1
    else :
        return 0

for i in range(n):
    count += x(m[i])
print(count)