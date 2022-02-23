from re import I


n=input()
x=''#이전값
v=0
for i in range(len(n)):
    if x != n[i]:
        v+=10
        x=n[i]
    elif x == n[i]:
        v+=5
        x=n[i]
print(v)