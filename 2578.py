n = []
m = []
count = 0

for i in range(5) :
    n.extend(list(map(int,input().split())))    # 값 하나씩 추가
for i in range(5) :
    m.extend(list(map(int,input().split())))    # 값 하나씩 추가
#입력 끝
for i in range(len(n)):
    n[n.index(m[i])] = 0
    count += 1
    
    cw = 0
    ccw = 0
    bg = 0
    for x in range(5):
        rownum = 0
        colnum = 0
        
        for y in range(5):
            if n[(x*5)+y] == 0 :
                rownum += 1
            if n[x+(y*5)] == 0 :
                colnum += 1
            
            if rownum == 5 :
                bg += 1
            if colnum == 5 :
                bg += 1
            
        if n[x*6] == 0 :
            cw += 1
        if n[(x+1)*4] == 0:
            ccw += 1
            
        if cw == 5 :
            bg += 1
        if ccw == 5 :
            bg += 1    
                       
    if bg >= 3 :
        break        
            
print(count)            