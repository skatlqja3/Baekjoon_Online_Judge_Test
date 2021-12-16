import sys
n = int(sys.stdin.readline())
m = str(n)
l = []
for i in m:
    l.append(i)
for i in range(len(m)):
    for j in range(i+1,len(m)):
        if l[i] < l[j]:
            l[i],l[j] = l[j],l[i]
for i in l:
    print(i,end='')