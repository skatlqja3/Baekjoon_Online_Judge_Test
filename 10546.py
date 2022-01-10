import sys
from collections import deque
n=int(sys.stdin.readline())
m=deque()
for i in range(n):
    m.append(sys.stdin.readline().strip())
for i in range(n-1):
    m.remove(sys.stdin.readline().strip())
print(m.pop())