n = int(input())
m = []
cm_max = 0
kg_max = 0
for i in range(n):
    m.append(list(map(int,input().split())))
for i in range(n):
    count = 0
    momo = 0
    for j in range(n):
        if i != j:
            if m[i][0] > m[j][0] and m[i][1] > m[j][1]:
                count += 1
            elif m[i][0] >= m[j][0] and m[i][1] <= m[j][1]:  
                momo += 1
            elif m[i][0] <= m[j][0] and m[i][1] >= m[j][1]:   
                momo += 1
    print(n-count-momo,end=' ')
