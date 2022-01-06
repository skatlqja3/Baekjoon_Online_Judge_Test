import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
l = [[0 for _ in range(n)]for _ in range(n)]
num = n*n
num_n = n
x,y=0,0
co_1=0
co_2=-1
co_3=0
co_4=0
a,b=0,0
while True:
    for i in range(co_4,num_n): #아래
        l[i][y]=num
        x=i
        if num == m:
            a,b=x+1,y+1
        num-=1
        if num == 0:
            break
    if num == 0:
        break
    co_1+=1
    for i in range(co_1,num_n): #오른
        l[x][i]=num
        y=i
        if num == m:
            a,b=x+1,y+1
        num-=1
        if num == 0:
            break
    if num == 0:
        break
    num_n-=2
    for i in range(num_n,co_2,-1): #위
        l[i][y]=num
        x=i
        if num == m:
            a,b=x+1,y+1
        num-=1
        if num == 0:
            break
    if num == 0:
        break
    co_2+=1
    for i in range(num_n,co_3,-1): #왼
        l[x][i]=num
        y=i
        if num == m:
            a,b=x+1,y+1
        num-=1
        if num == 0:
            break
    if num == 0:
        break
    co_3+=1
    co_4+=1
    num_n+=1
for i in range(n):
    for j in range(n):
        print(f"{l[i][j]}",end=" ")
    print("")
print(f"{a} {b}")