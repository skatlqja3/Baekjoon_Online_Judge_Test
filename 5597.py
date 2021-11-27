n = []  # 중복되는 숫자가 없을 경우
m = []
j = 1
k = 0
for i in range(28):
    n.append(int(input()))
n.sort()
while j!=31:
    if n[k] != j:
        m.append(j)
        k-=1
    k+=1
    j+=1
    if len(n) == k:
        k-=1
for i in range(2):
    print(m[i])