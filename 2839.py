n=int(input())
count=0
num=0
i=n//5
while i!=0:
    m=n-(i*5)
    if m%3!=0:
        i-=1
    else:
        i+=m//3
        break
if i==0 and n%3==0:
    i=n//3
    print(i)
elif i==0:
    print("-1")
else:
    print(i)
