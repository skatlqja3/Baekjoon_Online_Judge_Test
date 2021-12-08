import sys
import time
import math
start = time.time()
n = int(sys.stdin.readline())
m = []
l = []
co = 0
for i in str(n):
    m.append(i)
for i in range(10):
    l.append(m.count(str(i)))
    if i == 9:
        l[9] = l[6] + l[9]
        l[6] = 0
for i in range(10):
    if co < l[i]:
        if i != 9:
            co = l[i]
        if i == 9:
            co = math.ceil(l[i]/2)    
print(co)
end = time.time()
print(end-start)