a,b=map(int,input().split())
x=0
y=0
for i in range(a,b+1):
    x=0
    for j in range(1,i+1):
        x+=j
    if i==a:
        y+=x
    else:
        y*=x
print(y%14579)
        
