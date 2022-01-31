n=int(input())
m=set()
for _ in range(n):
    m.add(input())
l=sorted(m)
for i in range(1,51):
    for j in l:
        if len(j) == i:
            print(j)