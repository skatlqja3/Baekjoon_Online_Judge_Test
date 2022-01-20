from sys import stdin, stdout
n = stdin.readline()
a = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
b = sorted(map(int,stdin.readline().split()))

def binary(l, a, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == a[m]:
        return 1
    elif l < a[m]:
        return binary(l, a, start, m-1)
    else:
        return binary(l, a, m+1, end)
    
for l in b:
    start = 0
    end = len(a)-1
    print(binary(l,a,start,end))