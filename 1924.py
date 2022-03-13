x,y = map(int , input().split())
days_31=[1,3,5,7,8,10,12]
days_30=[4,6,9,11]
days_28=[2]
num=0
for i in range(1,x):
    if i in days_31:
        num += 31
    elif i in days_30:
        num += 30
    elif i in days_28:
        num += 28
num += y
if num%7 == 1:
    print('MON')
elif num%7 == 2:
    print('TUE')
elif num%7 == 3:
    print('WED')
elif num%7 == 4:
    print('THU')
elif num%7 == 5:
    print('FRI')
elif num%7 == 6:
    print('SAT')
elif num%7 == 0:
    print('SUN')