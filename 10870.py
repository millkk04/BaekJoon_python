x=int(input())
y=[0,1]
if x==0:
    print(0)
elif x==1:
    print(1)
else:
    for i in range(x-1):
        c=y[i]+y[i+1]
        y.append(c)
    print(c)
    
    
