import sys
n = int(sys.stdin.readline())
for _ in range(n):
    m,l=map(str,sys.stdin.readline().split())
    for i in l:
        print(i*int(m),end='')
    print(end='\n')