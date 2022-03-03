n=int(input())
for _ in range(n):
    y,k=0,0
    for _ in range(9):
        m,l=map(int,input().split())
        y+=m
        m+=l
    if k < y:
        print('Yonsei')
    elif k > y:
        print('Korea')
    else:
        print('Draw')