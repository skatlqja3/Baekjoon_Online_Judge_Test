from collections import Counter
import sys
n = int(sys.stdin.readline())
m = [int(sys.stdin.readline().strip()) for i in range(n)]
print(round(sum(m)/n))
m.sort()
print(m[n//2])
l = []
num_count = Counter(m).most_common()
for i in num_count:
    if i[1] == num_count[0][1]:
        l.append(i[0])
if len(l) == 1:
    print(l[0])
else:
    print(l[1])
print(max(m)-min(m))