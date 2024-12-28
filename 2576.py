x=[]
y=0
for i in range(7):
    a=int(input())
    if a%2!=0:
        x.append(a)
for i in range(len(x)):
    y+=x[i]
if len(x)==0:
    print(-1)
else:
    print(y)
    z=x[0]
    for i in range(len(x)):
        if z>x[i]:
            z=x[i]
    print(z)
        

