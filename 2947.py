import sys
import time
start = time.time()
n = list(map(int,sys.stdin.readline().split()))
m = 0
co = 9
while co != 4:
    co = 0
    for i in range(len(n)-1):
        if n[i] == i+1:
            co += 1
        if n[i] > n[i+1]:
            m = n[i]
            n[i] = n[i+1]
            n[i+1] = m
            for j in range(len(n)):
                if j==len(n)-1:
                    print(n[j])
                    break
                print(n[j],end=' ')
print(time.time()-start)