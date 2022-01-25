from collections import deque
import sys
n=int(sys.stdin.readline())
l=deque()
for _ in range(n):
    m=list(map(str,sys.stdin.readline().split()))
    if m[0] == "push":
        l.append(m[1])
    elif m[0] == "pop":
        if len(l) == 0:
            print('-1')
        else:
            print(l.popleft())
    elif m[0] == "size":
        print(len(l))
    elif m[0] == "empty":
        if len(l) == 0:
            print('1')
        else:
            print('0')
    elif m[0] == 'front':
        if len(l) == 0:
            print('-1')
        else:
            print(l[0])
    elif m[0] == 'back':
        if len(l) == 0:
            print('-1')
        else:
            print(l[len(l)-1])