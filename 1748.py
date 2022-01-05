import sys
n = int(sys.stdin.readline())
sum = 0     #
sum_i = 1   #900 90 9
num = 0     #99
for i in range(len(str(n))):
    if i == len(str(n))-1:
        num += ((n-sum)*(i+1))
    else:
        sum += 9*sum_i      #9 ... 99 ... 999
        num += (9*sum_i)*(i+1)
        sum_i *= 10         #1 ... 10 ... 100
        
print(num)