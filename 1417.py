import sys
import time

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

l = []
max = 0
num = 0
co = 0
num_co = 0
if n == 1:
    co = 0
elif n != 0:
    for i in range(n-1):
        num =int(sys.stdin.readline())
        l.append(num)
        if max < num:
            max = num
            num_co = i        
    start = time.time()
    while True:
        if max >= m:
            co += 1
            m += 1
            l[num_co] -= 1
            max -= 1
        
        for i in range(n-1):
            if max <= l[i]:
                max = l[i]
                num_co = i
        if max < m :
            break
print(co)
print(time.time()-start)