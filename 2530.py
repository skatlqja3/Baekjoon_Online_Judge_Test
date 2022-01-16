n,m,l=map(int,input().split())
l+=int(input())
m+=l//60
n+=m//60
print(n%24,m%60,l%60)