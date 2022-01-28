import sys
stack_1 = list(sys.stdin.readline().strip())
stack_2 = []
n = int(sys.stdin.readline())
for i in range(n):
    order = sys.stdin.readline().strip()
    if order[0] == "L" and stack_1 != []:
        stack_2.append(stack_1.pop())
    elif order[0] == "D" and stack_2 != []:
        stack_1.append(stack_2.pop())
    elif order[0] == "B" and stack_1 != []:
        stack_1.pop()
    elif order[0] == "P":
        stack_1.append(order[2])
stack_2.reverse()
print("".join(stack_1 + (stack_2)))