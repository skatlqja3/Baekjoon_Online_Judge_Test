n,m = map(int,input().split())
l=0
max,min = 0,0 #최대,최소
# 최대공약수 유클리드 호제법 사용
min=n*m
if n<m:
    n,m=m,n
while True:  # n > m 경우
    l=n%m
    if l==0:
        max=m
        break
    n,m=m,l
# 최소 공배수 = 두 자연수의 곱 / 최대 공약수
min=int(min/max)
print(max)
print(min)