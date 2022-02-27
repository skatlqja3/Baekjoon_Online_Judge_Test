n=int(input())
for i in range(n):
    m=input()
    count = 0
    x=1
    for j in range(len(m)):
        if m[j] == 'O':
            count = count + x
            x = x + 1
        else :
            x=1
    print(count)