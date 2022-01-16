l=[]
sum = 0
for i in range(5):
    l.append(int(input()))
    
for i in range(5):
    if l[i] < 40:
        l[i] = 40
    sum += l[i]
print(int(sum/5))