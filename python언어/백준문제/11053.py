x=int(input())

y=list(map(int,input().split()))

k=y[0]
c=[k]
for i in range(1,x):
    if y[i]>k:
        c.append(y[i])
    else:
        for p in range(len(c)):
            if c[p]>=y[i]:
                c[p]=y[i]
                break
    k=c[len(c)-1]
print(len(c))
    
                
        
        

        
        
    
