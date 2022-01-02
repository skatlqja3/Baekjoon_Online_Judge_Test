import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
l = [i+1 for i in range(n)]
deq = deque(l)
print(f"<",end="")
for i in range(n):
    deq.rotate(-(m-1))
    num = deq.popleft()
    if i == n-1:
        print(f'{num}>')
    else:    
        print(f'{num}, ',end="")