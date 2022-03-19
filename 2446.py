n = int(input())
for i in range(0,n-1):
    print(' '*i + '*'*((n*2)-1-(i*2)))
for i in range(0,n):
    print(' '*(n-i-1)+'*'*(1+(i*2)))

n = int(input())
for i in range(0,(2*n)):
    if i < n:
        print(' '*i + '*'*((n*2)-1-(i*2)))
    else:
        i%=n
        print(' '*(n-i-1)+'*'*(1+(i*2)))
