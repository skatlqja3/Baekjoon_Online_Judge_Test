while True:
    n,m=map(int,input().split())
    if m==0 and n==0:
        break
    elif m%n==0:
        print('factor')
    elif n%m==0:
        print('multiple')
    else:
        print('neither')