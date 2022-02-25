n = int(input())
m = input()
count_A=0
count_B=0
for i in range(n):
    if m[i] == 'A':
        count_A+=1
    elif m[i] == 'B':
        count_B+=1
if count_B < count_A:
    print('A')
elif count_B > count_A:
    print('B')
elif count_B == count_A:
    print('Tie')