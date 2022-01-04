import sys
n = int(sys.stdin.readline())
m = 1
sum =0
while True:
    sum+=m
    if n-sum < 0:
        break
    m+=1
print(m-1)