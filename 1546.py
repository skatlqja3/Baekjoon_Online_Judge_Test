n=int(input())
m=[]
sum=0
max=0
m=list(map(int,input().split()))
for i in range(n):
    if max<m[i]:
        max = m[i]
for i in range(n):
    sum+=(m[i]/max)*100
print(sum/n)