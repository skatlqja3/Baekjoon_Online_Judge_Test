count = 0
x = []
y = []
n = int(input())    # 0 <= n <= 99

if n <= 9 :
    x.append('0')
    x.append(str(n))
    y.append('0')
    y.append(str(n))
else :
    x.append(str(n//10))
    x.append(str(n%10))
    y.append(str(n//10))
    y.append(str(n%10))
while True :
    a =(int(x[0])+int(x[1]))%10
    del x[0]
    x.append(str(a))
    count += 1
    if y == x :
        break
print(count)