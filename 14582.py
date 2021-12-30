import sys
n = list(map(int,sys.stdin.readline().split()))
m = list(map(int,sys.stdin.readline().split()))
num = 0
count = 0
v_nc = False
v_mc = False
for i in range(len(n)):
    num += n[i] 
    if num > 0:
        if v_mc == True:
            count += 1
        v_nc = True
        v_mc = False
    elif num < 0:
        if v_nc == True:
            count -= 1
        v_nc == False
        v_mc == True
    elif num == 0:
        v_nc == False
        v_mc == False
        count = 0
    num -= m[i]
    if num > 0:
        if v_mc == True:
            count += 1
        v_nc = True
        v_mc = False
    elif num < 0:
        if v_nc == True:
            count -= 1
        v_nc == False
        v_mc == True
    elif num == 0:
        v_nc == False
        v_mc == False
if count >= 0:
    print('No')
else:
    print("Yes")