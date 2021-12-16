import sys
n,m = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))
sl = []
co = 0
co_num = []
max = 0
for i in l:
    if i not in sl:
        sl.append(i)
print(sl)
co = len(sl)
for i in sl:
    co_num.append(l.count(i))
print(co_num)
for i in co_num:
    if max < i:
        max = i
print(max)
for k in range(max,0,-1):
    for i in range(co):
        if co_num[i] == k:
            for j in range(k,0,-1):
                print(sl[i],end=' ')
        