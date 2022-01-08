n=input()
num = len(n)
check = 1
for i in range(num//2):
    if n[i] != n[-(i+1)]:
        check = 0
print(check)