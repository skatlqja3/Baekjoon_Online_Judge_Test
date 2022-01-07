import sys
n,m = map(int,sys.stdin.readline().split())
l = [1 for _ in range(n)]
l[0]=0  # 1
x=1
num=0
count=0
check=0
while x!=n:
    i=2
    if l[x] != 0:
        l[x]=0
        count+=1
        num = x+1
        if count==m:
            check = num
        while True:            
            if num*i <= n:
                if l[(num*i)-1]!=0:
                    l[(num*i)-1]=0
                    count+=1
                    if count==m:
                        check = (num*i)
                i+=1
            else:
                break
    x+=1
print(check)