n=int(input())
i=1
x,y=1,1
if n==1:
    print("1/1")
else:
    while True:
        n-=i
        i+=1
        if n <= i:
            if i%2==0:
                x,y=n,i-(n-1) 
                break
            else:
                x,y=i-(n-1),n
                break
    print(f"{x}/{y}")