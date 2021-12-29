import sys

n = int(sys.stdin.readline())

for i in range(n):
    m = list(map(int,sys.stdin.readline().split()))
    sum = 0
    num = 0
    count = 0
    for j in range(1,len(m)):
        num += m[j]
    sum = num / m[0]
    for j in range(1,len(m)):
        if m[j] > sum:  #비율 넘는 카운트
            count += 1
    print('{0:.3f}%'.format(count/m[0]*100)) 