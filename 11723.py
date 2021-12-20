import sys
n = int(sys.stdin.readline())
l = [0] * 20
for i in range(n):
    m = sys.stdin.readline().split()
    if m[0] == 'add':
        if l[int(m[1])-1] == 0:
            l[int(m[1])-1] = 1
    elif m[0] == 'remove':
        if l[int(m[1])-1] == 1:
            l[int(m[1])-1] = 0
    elif m[0] == 'check':
        if l[int(m[1])-1] == 1:
            print(1)
        else:
            print(0)
    elif m[0] == 'toggle':
        if l[int(m[1])-1] == 0:
            l[int(m[1])-1] = 1
        else:
            l[int(m[1])-1] = 0
    elif m[0] == 'all':
        del l
        l = [1] * 20
    elif m[0] == 'empty':
        del l
        l = [0] * 20