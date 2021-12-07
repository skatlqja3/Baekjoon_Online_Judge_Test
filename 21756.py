n = int(input())
m = []
for i in range(n):
    m.append(i+1)
while len(m) != 1:
    for j in range(len(m)):
        if (j+1) % 2 != 0:
            m[j] = 0
    while 0 in m:    
	    m.remove(0)
print(m[0])
