import sys
def p(n):
    return n * p(n-1) if n > 1 else 1

n = int(sys.stdin.readline())
print(p(n))
