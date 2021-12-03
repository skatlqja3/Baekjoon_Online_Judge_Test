n, co = map(int,input().split())
l = []
num = 0
k = 0
count = 0
num = []
for i in range(n):
    l.append(i+1)
while len(num)!=n:
    if l[k] != 0:   
        count += 1
    if count == co:
        num.append(l[k])
        l[k] = 0
        count = 0
    k += 1
    if k > n-1:
        k = 0
        
print('<',end='')
for i in range(n):
    if i == n-1:
        print(num[i],end='>')
    else :
        print(num[i],end=', ')