import sys
n=int(sys.stdin.readline().strip())
m=sys.stdin.readline().strip()
sum=0
x=1
for i in range(len(m),0,-1):
    num = n*int(m[i-1])
    print(num)
    sum+=num*x
    x*=10
print(sum)