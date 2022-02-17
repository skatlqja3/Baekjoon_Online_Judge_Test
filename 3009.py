import sys
n,m=[],[]
x,y=0,0
for _ in range(3):
    nn,mm=map(int,sys.stdin.readline().split())
    n.append(nn)
    m.append(mm)
for i in range(3):
    if n.count(n[i])==1:
        x=n[i]
    if m.count(m[i])==1:
        y=m[i]
print(f'{x} {y}')