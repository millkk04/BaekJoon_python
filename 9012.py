x=int(input())
y=[]
for i in range(x):
    y.append(input())
for i in range(x):
    a=0
    b=0
    c=0
    for k in range(len(y[i])):
        if y[i][k]=='(':
            a+=1
        else:
            b+=1
        if a==b:
            a=0
            b=0
        if b==1 and a==0:
            c=1
    if a==b and c!=1:
        y[i]='YES'
    else:
        y[i]='NO'
for i in range(x):
    print(y[i])
    
    
        
        
