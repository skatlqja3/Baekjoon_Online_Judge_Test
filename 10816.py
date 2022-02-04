import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
a.sort()
def lll(t,len):
    low=0
    high=len
    while low<high:
        mid=(high+low)//2
        if a[mid]>=t:
            high = mid
        else:
            low=mid+1
    return low
def rrr(t,len):
    low=0
    high=len
    while low<high:
        mid=(high+low)//2
        if a[mid]>t:
            high = mid
        else:
            low=mid+1
    return low
for i in range(m):   
    print(rrr(b[i],n)-lll(b[i],n),end=" ")