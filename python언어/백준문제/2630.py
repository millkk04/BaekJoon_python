x=int(input())
y=[]
for i in range(x):
    q=list(map(int,input().split()))
    y.append(q)

c=0
nk=[]
for k in range(x):
    for n in range(x):
        if y[k][n]==1:
            c+=1
            nk.append(n)
        elif y[k][n]==0:
            if c==0:
                pass
            else:
                if k+c-1 <= x:
                    for m in range(1,c):
                        for r in range(len(nk)):
                            if y[k+m][r]==1:
                                pass
                else:
                    pass
                        
                
            
    
