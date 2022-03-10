n=int(input())
for i in range(n):
    m=int(input())
    number=0
    name=''
    for j in range(m):
        x=list(input().split())
        if int(x[1]) > number:
            name=x[0]
            number=int(x[1])
    print(name)