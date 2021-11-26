import math
a,b,v = map(int, input().split())
sum = 0
i = 0

i = math.ceil((v-a)*1/(a-b))
i += 1
print(i)

#while True :
#    i += 1
#    sum = sum + a
#    sum = sum - b
#    if sum >= v-a :
#        i += 1
#        break
#print(i)

