import sys
n,m = map(int,(sys.stdin.readline().split()))
l = [False for _ in range(m+1)]
l[0]=True
l[1]=True
for i in range(2,m+1):
   if l[i]:
       continue 
   for j in range(i+i,m+1,i):
       l[j]=True
for i in range(n,m+1):
    if l[i]==False:
        print(i)