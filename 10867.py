import sys
n=int(sys.stdin.readline());
m=list(map(int,sys.stdin.readline().split()))
l=sorted(list(set(m)))
for i in l:
    print(i,end=" ")