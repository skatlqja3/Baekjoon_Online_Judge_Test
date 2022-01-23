n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()

for i in range(m):
    low=0
    high=n-1
    x=0
    while low<=high:
        mid=(high+low)//2
        if a[mid]==b[i]:
            x=1
            break
        elif a[mid] < b[i]:
            low=mid+1
        else:
            high=mid-1
    print(x,end=" ")