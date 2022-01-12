import sys
n = int(sys.stdin.readline())
m=[]
for i in range(n):
    m.append(int(sys.stdin.readline()))
for i in m:
    l_0=[1,0,1]
    l_1=[0,1,1]
    if i <= 2:
        print(f"{l_0[i]} {l_1[i]}")
    else:
        for j in range(3,i+1):
            num_0 = l_0[j-2]+l_0[j-1]
            num_1 = l_1[j-2]+l_1[j-1]
            l_0.append(num_0)
            l_1.append(num_1)
        print(f"{l_0[i]} {l_1[i]}")