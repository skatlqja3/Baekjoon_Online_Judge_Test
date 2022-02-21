import sys
n=int(sys.stdin.readline())
for i in range(n):
    m=list(map(int,sys.stdin.readline().split()))
    if m[1]-m[2]==m[0]:
        print('does not matter')
    elif m[1]-m[2]>m[0]:
        print('advertise')
    else:
        print('do not advertise')