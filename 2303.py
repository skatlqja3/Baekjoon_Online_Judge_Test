m = []
ch = []
sum = 0
num = 0
co = 0
max = 0
n = int(input())
for i in range(n):
    m.append(list(map(int,input().split())))
for c in range(n):
    for i in range(3):
        for j in range(i+1,3):
            for k in range(j+1,4):
                num = 0
                num = (m[c][i] + m[c][j] + m[c][k])%10
                print(num)
                if sum < num :
                    sum = num
    ch.append(sum)
    sum = 0
for i in range(n):
    if max < ch[i]:
        max = ch[i]
        co = i+1
print(co)