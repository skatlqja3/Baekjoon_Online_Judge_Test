while True:
    n = int(input())
    if n == -1:
        break
    num=1
    list_m=[1]
    for i in range(2,n):
        if n%i==0:
            list_m.append(i)
            num+=i
    if num==n:
        print(f'{n} = ',end='')
        for i in range(len(list_m)):
            if len(list_m)-1 == i:
                print(f'{list_m[i]}')
            else:
                print(f'{list_m[i]} + ',end='')
    else:
        print(f'{n} is NOT perfect.')