m=int(input())
n=int(input())
i=1
num=0
sum=0
min=0
while num <= n:
    num=i*i    
    if m <= num <= n:
        sum+=num
        if min==0:
            min=num
    i+=1
if sum == 0:
    print('-1')
else:
    print(sum)
    print(min)      