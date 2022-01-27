x=list(map(int,input().rsplit(':')))
y=list(map(int,input().rsplit(':')))
hh,mm,ss="","",""
if y[2]-x[2] < 0:
    if y[1]-x[1] <= 0:
        y[0]-=1
        y[1]+=59
        y[2]+=60
    else:
        y[1]-=1
        y[2]+=60
elif y[1]-x[1] < 0:
        y[0]-=1
        y[1]+=60
s=y[2]-x[2]
m=y[1]-x[1]
h=y[0]-x[0]
if h < 0:
    h = 24+(y[0]-x[0])
if h<10:
    hh=str(0)+str(h)
else:
    hh=str(h)
if m<10:
    mm=str(0)+str(m)
else:
    mm=str(m)
if s<10:
    ss=str(0)+str(s)
else:
    ss=str(s)
print(f"{hh}:{mm}:{ss}")