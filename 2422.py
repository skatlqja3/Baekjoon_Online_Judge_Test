import sys
n,m = map(int,sys.stdin.readline().split())
l=[[False for _ in range(n)]for _ in range(n)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    l[a-1][b-1] = True
    l[b-1][a-1] = True
num=0
for i in range(n):
    for j in range(i+1,n):
            for k in range(j+1,n):
                if not l[i][j] and not l[i][k] and not l[j][k]:
                    num+=1
print(num)