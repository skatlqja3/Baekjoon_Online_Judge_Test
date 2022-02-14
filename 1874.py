import sys
n = int(sys.stdin.readline())
m=[]
i = 2
ccc = 0
s=[]
on=False
for _ in range(n):
    m.append(int(sys.stdin.readline()))
l=[1]
s.append('+')
while ccc != len(m):    #카운트가 리스트수랑 같을 때 가지
    if len(l) == 0:
        l.append(i)
        i+=1
        s.append('+')
    if l[len(l)-1] == m[ccc]: 
        l.pop()
        s.append('-')
        ccc+=1
    else :
        if on == True:
            break
        if i <= n:
            l.append(i)
            i+=1
            s.append('+')
        else:
            on = True
    
if on == True:
    print('NO')
else:
    for i in s:
        print(i)