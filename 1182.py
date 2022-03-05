import sys
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
count = 0

for i in range(1,n+1):
    per = combinations(l,i)
    for j in list(per):
        num = 0
        for k in j:
            num+=k
        if num == m:
            count+=1
print(count)