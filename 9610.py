n=int(input())
q1,q2,q3,q4,axis=0,0,0,0,0
for _ in range(n):
    m,l=list(map(int,input().split()))
    if m == 0 or l == 0:
        axis+=1
    elif m>0 and l>0:
        q1+=1
    elif m<0 and l>0:
        q2+=1
    elif m<0 and l<0:
        q3+=1
    elif m>0 and l<0:
        q4+=1
print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}")
print(f"Q4: {q4}")
print(f"AXIS: {axis}")