from typing import Deque
import sys
from collections import deque
n = int(sys.stdin.readline().strip())
for _ in range(n):
    n_1 = str(sys.stdin.readline().strip())
    n_2 = int(sys.stdin.readline().strip())
    n_3 = sys.stdin.readline().strip()
    index = 0
    if n_3 == '[]':
        n_3_list = []
    else:
        n_3_list = deque(list(map(int,n_3[1:-1].split(','))))
    if n_2 - n_1.count('D')  >= 0:
        for i in range(len(n_1)):
            if n_1[i] == 'R':
                if index == 0:
                    index -=1
                elif index == -1:
                    index +=1
            elif n_1[i] == 'D':
                if index == 0:
                    n_3_list.popleft()
                elif index == -1:
                    n_3_list.pop()
        if index == -1:
            n_3_list.reverse()
        number = list(n_3_list)
        print('[',end="")
        for i in range(len(number)):
            if len(number)-1 == i:
                print('{0}'.format(number[i]),end="")
            else:
                print('{0},'.format(number[i]),end="")
        print(']')
    else:
        print('error')